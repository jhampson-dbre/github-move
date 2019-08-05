"""
Get player stats from a given game
"""
import re
from requests import get
from bs4 import BeautifulSoup


def get_player_stats_from_game(team, year, week):
    """
    Get player stats for a particular game
    """

def get_game_urls(year, week):
    """
    Get the box score URL for each game by team

    returns a dictionary with the team as the key
    and the link to the detailed game stats
    """
    base_url = "https://www.pro-football-reference.com"

    # URL for the summary of all games for a given week
    # This page has the each match up for the week and
    # a link to the detailed game stats 
    url = "https://www.pro-football-reference.com/years/{}/week_{}.htm".format(
        year, week)

    response = get(url)

    week_summary = BeautifulSoup(response.content, 'html.parser')

    # Get just the game summary content
    week_summary_games = week_summary.find_all(
        attrs={"class": "game_summary expanded nohover"})

    losing_teams = []
    winning_teams = []
    game_link = []

    # For each game played, extract the losing team,
    # the winning team, and the detailed game stats link
    for game in week_summary_games:
        try:
            losing_team_strings = [text for text in game.find(
                attrs={"class": "loser"}).stripped_strings]
            losing_teams.append(losing_team_strings[0])
        except AttributeError:
            pass

        try:
            winning_team_strings = [text for text in game.find(
                attrs={"class": "winner"}).stripped_strings]
            winning_teams.append(winning_team_strings[0])
        except AttributeError:
            pass

        for link in game.find_all(href=re.compile("boxscores")):
            game_link.append(base_url + link.get('href'))


    game_urls = dict(zip(losing_teams, game_link))
    game_urls.update(dict(zip(winning_teams, game_link)))

    return game_urls 
