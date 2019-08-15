"""
Tests for read_player_csv.py
"""
import pytest
import pandas as pd
import read_player_csv as ffb


@pytest.mark.parametrize("test_position, test_ranking_system, expected_player",
                         [
                             ("QB", "Rank", "Patrick Mahomes"),
                             ("RB", "Rank", "Saquon Barkley"),
                             ("WR", "Rank", "DeAndre Hopkins"),
                             ("TE", "Rank", "Travis Kelce")
                         ])
def test_get_best_player_at_start_of_draft(test_position, test_ranking_system, expected_player):
    """
    Given no players have been drafted,
    it should return the overall best ranked player from
    each position
    """
    # test_data = ffb.import_player_stats
    assert ffb.get_best_player(
        test_position, ffb.import_player_2018_stats().join(ffb.import_player_2019_rank(), how='right'), ranking_system=test_ranking_system).index[0] == expected_player


@pytest.mark.skip(reason="get_player_score_by_system is not currently used")
@pytest.mark.parametrize("test_player,test_scoring_system,expected_score", [
    ("Patrick Mahomes", "FantPt", 417),
    ("Patrick Mahomes", "PPR", 417.1),
    ("Todd Gurley", "FantPt", 313),
    ("Todd Gurley", "PPR", 372.1)])
def test_get_player_rank_by_scoring_system(test_player, test_scoring_system, expected_score):
    """
    Given a valid player and scoring system,
    it should return the score for the player
    """
    assert ffb.get_player_score_by_system(
        test_player, test_scoring_system, ffb.import_player_2018_stats()) == expected_score


@pytest.mark.parametrize("test_excluded_players_list", [[],
                                                        ["Todd Gurley"],
                                                        ["Patrick Mahomes", "Tyreek Hill", "Saquon Barkley"]])
def test_exclude_players(test_excluded_players_list):
    """
    Given a list of players that have been drafted,
    it should remove the drafted players from analysis
    """
    # Get the original set of player data
    test_player_df = ffb.import_player_2018_stats().join(
        ffb.import_player_2019_rank(), how='right')

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
                                                                             (["Titans DST",
                                                                               "Vikings DST"], 0),
                                                                             (["Todd Gurley", "Falcons DST", "Redskins DST", "Patrick Mahomes"], 2)])
def test_no_errors_if_excluded_player_is_not_in_data(test_excluded_players_list, num_excluded_in_data):
    """
    Given a list of players that have been drafted,
    when a drafted player does not exist in the data
    it should remove the drafted players that exist from
    analysis and not error on players that do not exist
    """
    # Get the original set of player data
    test_player_df = ffb.import_player_2018_stats().join(
        ffb.import_player_2019_rank(), how='right')

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
