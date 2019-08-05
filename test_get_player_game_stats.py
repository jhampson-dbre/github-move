"""
Test get_player_game_stats.py
"""
import pytest
import get_player_game_stats as ff_team

@pytest.mark.xfail
def test_get_player_stats_from_game():
    """
    Given a player and a game, it should return
    the player's stats from that game
    """
    team = "Titans"
    year = "2018"
    week = "1"
    expected_team_stats = {}

    assert ff_team.get_player_stats_from_game(
        team, year, week) == expected_team_stats


def test_get_urls():
    """
    Given a year and week, it should return
    a dictionary of teams and their game
    stats URL
    """

    year = "2018"
    week = "1"

    assert ff_team.get_game_urls(year, week).get(
        'Atlanta Falcons') == "https://www.pro-football-reference.com/boxscores/201809060phi.htm"
