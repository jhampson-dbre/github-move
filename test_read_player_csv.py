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
