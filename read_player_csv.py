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

    projected_player_df.columns = ['2019_Rank', 'Pos',
                                   'Best', 'Worst', 'Avg', 'Std Dev', 'ADP', 'vs. ADP']

    return projected_player_df


def get_best_player(position, player_df, ranking_system):
    ranking_system_lookup = {
        "Rank": "2019_Rank"
    }

    player_df = player_df[player_df['Pos'] == position]
    player_df = player_df.sort_values(
        [ranking_system_lookup[ranking_system]], axis=0, ascending=True)

    return player_df


def get_player_score_by_system(player, scoring_system, player_df):
    player_score = player_df.loc[player, scoring_system]

    return player_score


def exclude_players(player_df, exclude_list):
    return player_df.drop(index=exclude_list, errors='ignore')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Fantasy Football Draft Picker')
    parser.add_argument('--scoring-system',
                        default='standard',
                        help='Scoring system (default: standard)')
    parser.add_argument('--ranking-system',
                        default='Rank',
                        help='Ranking system (default: Rank)')

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

    player_df = import_player_2018_stats().join(import_player_2019_rank(scoring_system=args.scoring_system),
                                                lsuffix='_hist', rsuffix='_pred', how='right')
    # print(player_df.head(15))

    with open("./data/player_exclusions.yaml", 'r') as stream:
        player_exclusions = yaml.safe_load(stream)

    player_df = exclude_players(player_df, player_exclusions['drafted'])
    player_df = exclude_players(player_df, player_exclusions['other'])

    for position in positions:
        ranked_players_by_position = get_best_player(
            position, player_df, args.ranking_system)
        print(ranked_players_by_position[[
              'Pos', '2018_{}_Pts'.format(args.scoring_system), '2019_Rank', 'Best', 'Worst', 'Avg', 'ADP', 'vs. ADP']].head(5))
