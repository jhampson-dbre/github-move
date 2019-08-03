"""
Test get_player_game_stats.py
"""
import get_player_game_stats as ff_team

def test_get_player_stats_from_game():
    """
    Given a player and a game, it should return
    the player's stats from that game
    """
    team = "Titans"
    year = "2018"
    week = "1"
    expected_team_stats = {}

    assert ff_team.get_player_stats_from_game(team, year, week) == expected_team_stats