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


def exclude_players(player_df, exclude_list):
    return player_df.drop(index=exclude_list)

# print(player_df.head(200).groupby('FantPos').describe()[['PPR']])
# player_df.head(5).diff(periods=-1)


if __name__ == "__main__":
    positions = [
        'QB',
        'WR',
        'RB',
        'TE'
    ]

    player_df = import_player_stats()

    for position in positions:
        player = get_best_player(position, player_df)
        overall_rank = player_df.loc[player, 'OvRank']
        print("{} - {} - {}".format(player, position, overall_rank))

# player_df.head(200).groupby('FantPos').mean()[['FantPt']]
# player_df.head(200).groupby('FantPos').median()[['FantPt']]
# player_df.groupby('FantPos').count()
# player_df.head(200).groupby('FantPos').count()
