import argparse
import pandas as pd
# drafted_players = [
#     'Todd Gurley',
#     'Christian McCaffrey'
# ]


def import_player_stats():
    fields = ['Rk', 'Player', 'Tm', 'FantPos',
              'FantPt', 'PPR', 'VBD', 'PosRank', 'OvRank']
    # fields = ['Rk', 'Player', 'FantPt', 'PPR', 'VBD', 'PosRank', 'OvRank']
    player_df = pd.read_csv("data/player_position.csv",
                            usecols=fields, index_col='Player')

    return player_df


def get_best_player(position, player_df):
    best_player = player_df[player_df['FantPos'] == position].head(1).index[0]

    return best_player


def get_player_score_by_system(player, scoring_system, player_df):
    scoring_system_lookup = {
        "standard": "FantPt",
        "ppr": "PPR",
        "rank": "OvRank"
    }
    player_score = player_df.loc[player, scoring_system_lookup[scoring_system]]

    return player_score
# player_df = player_df[~player_df.Player.isin(drafted_players)]
# player_df = player_df[~player_df.isin(drafted_players)]
# print(player_df.head(200).groupby('FantPos').describe()[['PPR']])
# player_df.head(5).diff(periods=-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Fantasy Football Draft Picker')
    parser.add_argument('--scoring-system',
                        default='rank',
                        help='Scoring system (default: Overall rank)')

    args = parser.parse_args()
    positions = [
        'QB',
        'WR',
        'RB',
        'TE'
    ]

    player_df = import_player_stats()

    for position in positions:
        player = get_best_player(position, player_df)
        player_score = get_player_score_by_system(
            player, args.scoring_system, player_df)
        print("{} - {} - {}".format(player, position, player_score))

# player_df.head(200).groupby('FantPos').mean()[['FantPt']]
# player_df.head(200).groupby('FantPos').median()[['FantPt']]
# player_df.groupby('FantPos').count()
# player_df.head(200).groupby('FantPos').count()
