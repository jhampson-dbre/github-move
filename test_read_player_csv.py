"""
Tests for read_player_csv.py
"""
import pytest
import pandas as pd
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


@pytest.mark.parametrize("test_excluded_players_list", [[],
                                                        ["Todd Gurley"],
                                                        ["Patrick Mahomes", "Tyreek Hill", "Saquon Barkley"]])
def test_exclude_players(test_excluded_players_list):
    """
    Given a list of players that have been drafted,
    it should remove the drafted players from analysis
    """
    # Get the original set of player data
    test_player_df = ffb.import_player_stats()

    # Remove the players that have already been drafted
    result_player_df = ffb.exclude_players(
        test_player_df, test_excluded_players_list)

    # They drafted player should not be in the data
    assert not result_player_df.index.intersection(
        test_excluded_players_list).size

    # The number of players left should be the original
    # number of players minus the number of players that
    # have been drafted
    assert test_player_df.index.size - \
        len(test_excluded_players_list) == result_player_df.index.size


@pytest.mark.parametrize("test_excluded_players_list,num_excluded_in_data", [(["Chicago Bears DST"], 0),
                                                                             (["Greg Zuerlein",
                                                                               "Harrison Butker"], 0),
                                                                             (["Todd Gurley", "Greg Zuerlein", "Harrison Butker", "Patrick Mahomes"], 2)])
def test_no_errors_if_excluded_player_is_not_in_data(test_excluded_players_list, num_excluded_in_data):
    """
    Given a list of players that have been drafted,
    when a drafted player does not exist in the data
    it should remove the drafted players that exist from 
    analysis and not error on players that do not exist
    """
    # Get the original set of player data
    test_player_df = ffb.import_player_stats()

    # Remove the players that have already been drafted
    result_player_df = ffb.exclude_players(
        test_player_df, test_excluded_players_list)

    # They drafted player should not be in the data
    assert not result_player_df.index.intersection(
        test_excluded_players_list).size

    # The number of players left should be the original
    # number of players minus the number of players that
    # have been drafted that exist in the data
    assert test_player_df.index.size - \
        num_excluded_in_data == result_player_df.index.size
