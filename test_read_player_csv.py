"""
Tests for read_player_csv.py
"""
import pytest
import read_player_csv as ffb


@pytest.mark.parametrize("test_position,expected_player", [("QB", "Patrick Mahomes"),
                                                           ("RB", "Todd Gurley"),
                                                           ("WR", "Tyreek Hill"),
                                                           ("TE", "Travis Kelce")])
def test_get_best_player_at_start_of_draft(test_position, expected_player):
    """
    Given no players have been drafted,
    it should return the overall best player from
    each position
    """
    # test_data = ffb.import_player_stats
    assert ffb.get_best_player(
        test_position, ffb.import_player_stats()) == expected_player


@pytest.mark.parametrize("test_player,test_scoring_system,expected_score", [
    ("Patrick Mahomes", "standard", 417),
    ("Patrick Mahomes", "ppr", 417.1),
    ("Patrick Mahomes", "rank", 5),
    ("Todd Gurley", "standard", 313),
    ("Todd Gurley", "ppr", 372.1),
    ("Todd Gurley", "rank", 1)])
def test_get_player_rank_by_scoring_system(test_player, test_scoring_system, expected_score):
    """
    Given a valid player and scoring system,
    it should return the score for the player
    """
    assert ffb.get_player_score_by_system(
        test_player, test_scoring_system, ffb.import_player_stats()) == expected_score
