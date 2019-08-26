import argparse
import pandas as pd
import yaml


def import_player_2018_stats():
    fields = ['Rk', 'Player', 'Tm', 'FantPos',
              'FantPt', 'PPR', 'VBD', 'PosRank', 'OvRank']
    # fields = ['Rk', 'Player', 'FantPt', 'PPR', 'VBD', 'PosRank', 'OvRank']
    player_df = pd.read_csv("data/player_position.csv",
                            usecols=fields, index_col='Player')
    player_df.columns = ['2018_Rank', 'Tm', 'FantPos', '2018_standard_Pts',
                         '2018_ppr_Pts', 'VDB', '2018_Pos_Rank', '2018_Overall_Rank']

    return player_df


def import_player_2019_rank(scoring_system="standard"):
    fields = ["Rank", "Player", "Pos", "Best",
              "Worst", "Avg", "Std Dev", "ADP", "vs. ADP"]
    projected_player_df = pd.read_csv("data/2019_overall_rankings_{}.csv".format(scoring_system),
                                      usecols=fields, index_col='Player')
    projected_player_df.replace(
        {'Pos': r'\d+$'}, {'Pos': ''}, regex=True, inplace=True)

    projected_player_df.replace(
        {'ADP': r','}, {'ADP': ''}, regex=True, inplace=True)

    projected_player_df.columns = ['2019_Rank', 'Pos',
                                   'Best', 'Worst', 'Avg', 'Std Dev', 'ADP', 'vs. ADP']

    return projected_player_df


def import_player_2019_point_projections(position, scoring_system="standard"):
    fields = ["Player", "FPTS"]
    projected_player_df = pd.read_csv("data/2019_projections_{}_{}.csv".format(scoring_system, position),
                                      usecols=fields, index_col='Player')

    projected_player_df.columns = ['2019_{}_Pts'.format(scoring_system)]

    return projected_player_df


def initialize_player_stats(scoring_system, player_exclusions):
    player_df = import_player_2018_stats().join(import_player_2019_rank(scoring_system),
                                                lsuffix='_hist', rsuffix='_pred', how='right')

    player_df = exclude_players(player_df, player_exclusions['drafted'])
    player_df = exclude_players(player_df, player_exclusions['other'])

    return player_df


def get_best_player(position, player_df, ranking_system, scoring_system):
    ranking_system_lookup = {
        "Rank": "2019_Rank"
    }

    player_df = player_df[player_df['Pos'] == position].join(import_player_2019_point_projections(
        position=position, scoring_system=scoring_system))
    player_df = player_df.sort_values(
        [ranking_system_lookup[ranking_system]], axis=0, ascending=True)

    return player_df


def get_player_score_by_system_and_year(player, scoring_system, year, player_df):
    player_score = player_df.loc[player,
                                 '{}_{}_Pts'.format(year, scoring_system)]

    return player_score


def exclude_players(player_df, exclude_list):
    return player_df.drop(index=exclude_list, errors='ignore')


def get_best_player_name(player_df):
    best_player_name = player_df.head(1).index[0]
    return best_player_name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Fantasy Football Draft Picker')
    parser.add_argument('--scoring-system',
                        default='standard',
                        choices=('standard', 'ppr'),
                        help='Scoring system')
    parser.add_argument('--ranking-system',
                        default='Rank',
                        choices=['Rank'],
                        help='Ranking system (Expert Consesus, ADP, etc). Only Expert Consensus (Rank) supported.')
    parser.add_argument('--num-teams',
                        default=10,
                        help='Number of teams in the league')

    args = parser.parse_args()
    scoring_system_lookup = {
        "standard": "FantPt",
        "ppr": "PPR"
    }
    positions = [
        'QB',
        'WR',
        'RB',
        'TE'
    ]

    years = [
        '2018',
        '2019'
    ]

    # player_df = import_player_2018_stats().join(import_player_2019_rank(scoring_system=args.scoring_system),
    #                                             lsuffix='_hist', rsuffix='_pred', how='right')
    # print(player_df.head(15))
    with open("./data/player_exclusions.yaml", 'r') as stream:
        player_exclusions = yaml.safe_load(stream)

    num_players_drafted = len(player_exclusions['drafted'])

    curr_draft_round = int((num_players_drafted + 1) / args.num_teams)

    with open("./data/sleepers.yaml", 'r') as stream:
        sleepers = yaml.safe_load(stream)

    print("Current Draft Round   : {}.{}".format(int((num_players_drafted + 1) /
                                                     args.num_teams), (num_players_drafted + 1) % args.num_teams))
    print("Total Players Drafted : {}".format(num_players_drafted))

    player_df = initialize_player_stats(
        scoring_system=args.scoring_system, player_exclusions=player_exclusions)

    # player_df = exclude_players(player_df, player_exclusions['drafted'])
    # player_df = exclude_players(player_df, player_exclusions['other'])
    sleepers_df = pd.DataFrame()
    for position in positions:

        ranked_players_by_position = get_best_player(
            position, player_df, args.ranking_system, args.scoring_system)

        best_player_name = get_best_player_name(ranked_players_by_position)

        for year in years:
            best_player_points = get_player_score_by_system_and_year(
                best_player_name, args.scoring_system, year, ranked_players_by_position)

            ranked_players_by_position['{}_{}_Pts_Diff'.format(year,
                                                               args.scoring_system)] = ranked_players_by_position['{}_{}_Pts'.format(year, args.scoring_system)] - best_player_points

        ranked_players_by_position['.vs ADP'] = pd.to_numeric(ranked_players_by_position['ADP']) - len(
            player_exclusions['drafted']) - 1

        ranked_players_by_position['.vs Rank'] = pd.to_numeric(ranked_players_by_position['2019_Rank']) - len(
            player_exclusions['drafted']) - 1

        if position in sleepers.keys():
            sleepers_df = sleepers_df.append(ranked_players_by_position.loc[sleepers[position]])
        # if position in ['WR']:
        #     sleepers_df = ranked_players_by_position.loc[['Dede Westbrook']] 

        print(ranked_players_by_position[[
              'Pos', '2018_{}_Pts'.format(args.scoring_system), '2019_{}_Pts'.format(args.scoring_system), '2019_Rank', '.vs Rank', 'Best', 'Worst', 'ADP', '.vs ADP', '2018_{}_Pts_Diff'.format(args.scoring_system), '2019_{}_Pts_Diff'.format(args.scoring_system)]].head(5))

    print(sleepers_df[[
            'Pos', '2018_{}_Pts'.format(args.scoring_system), '2019_{}_Pts'.format(args.scoring_system), '2019_Rank', '.vs Rank', 'Best', 'Worst', 'ADP', '.vs ADP', '2018_{}_Pts_Diff'.format(args.scoring_system), '2019_{}_Pts_Diff'.format(args.scoring_system)]].sort_values('2019_Rank'))
