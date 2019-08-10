import pandas as pd

# drafted_players = [
#     'Todd Gurley',
#     'Christian McCaffrey'
# ]

fields = ['Rk', 'Player', 'Tm', 'FantPos',
          'FantPt', 'PPR', 'VBD', 'PosRank', 'OvRank']
# fields = ['Rk', 'Player', 'FantPt', 'PPR', 'VBD', 'PosRank', 'OvRank']
player_df = pd.read_csv("data/player_position.csv",
                        usecols=fields, index_col='Player')

# player_df = player_df[~player_df.Player.isin(drafted_players)]
# player_df = player_df[~player_df.isin(drafted_players)]
# print(player_df.head(200).groupby('FantPos').describe()[['PPR']])
# player_df.head(5).diff(periods=-1)
positions = [
    'QB',
    'WR',
    'RB',
    'TE'
]

for position in positions:
    player_df[player_df.FantPos == position].head()
# player_df.head(200).groupby('FantPos').mean()[['FantPt']]
# player_df.head(200).groupby('FantPos').median()[['FantPt']]
# player_df.groupby('FantPos').count()
# player_df.head(200).groupby('FantPos').count()
