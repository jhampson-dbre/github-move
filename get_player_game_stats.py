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
    """
    base_url = "https://www.pro-football-reference.com"
    url = "https://www.pro-football-reference.com/years/{}/week_{}.htm".format(
        year, week)

    response = get(url)

    week_summary = BeautifulSoup(response.content, 'html.parser')

    week_summary_games = week_summary.find_all(
        attrs={"class": "game_summary expanded nohover"})

    losing_teams = []
    winning_teams = []
    game_link = []

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

    losing_game_urls = dict(zip(losing_teams, game_link))
    winning_game_urls = dict(zip(winning_teams, game_link))

    losing_game_urls.update(winning_game_urls)

    return losing_game_urls
