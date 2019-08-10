"""
Tests for read_player_csv.py
"""
import pytest
import read_player_csv as ffb


@pytest.mark.parametrize("test_position, test_scoring_system, expected_player",
                         [
                             ("QB", "OvRank", "Patrick Mahomes"),
                             ("QB", "FantPt", "Patrick Mahomes"),
                             ("QB", "PPR", "Patrick Mahomes"),
                             ("RB", "OvRank", "Todd Gurley"),
                             ("RB", "FantPt", "Todd Gurley"),
                             ("RB", "PPR", "Saquon Barkley"),
                             ("WR", "OvRank", "Tyreek Hill"),
                             ("WR", "FantPt", "Tyreek Hill"),
                             ("WR", "PPR", "Tyreek Hill"),
                             ("TE", "OvRank", "Travis Kelce"),
                             ("TE", "FantPt", "Travis Kelce"),
                             ("TE", "PPR", "Travis Kelce")])
def test_get_best_player_at_start_of_draft(test_position, test_scoring_system, expected_player):
    """
    Given no players have been drafted,
    it should return the overall best ranked player from
    each position
    """
    # test_data = ffb.import_player_stats
    assert ffb.get_best_player(
        test_position, ffb.import_player_stats(), scoring_system=test_scoring_system) == expected_player


@pytest.mark.parametrize("test_player,test_scoring_system,expected_score", [
    ("Patrick Mahomes", "FantPt", 417),
    ("Patrick Mahomes", "PPR", 417.1),
    ("Patrick Mahomes", "OvRank", 5),
    ("Todd Gurley", "FantPt", 313),
    ("Todd Gurley", "PPR", 372.1),
    ("Todd Gurley", "OvRank", 1)])
def test_get_player_rank_by_scoring_system(test_player, test_scoring_system, expected_score):
    """
    Given a valid player and scoring system,
    it should return the score for the player
    """
    assert ffb.get_player_score_by_system(
        test_player, test_scoring_system, ffb.import_player_stats()) == expected_score
