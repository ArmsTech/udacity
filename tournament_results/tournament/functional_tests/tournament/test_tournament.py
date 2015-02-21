"""Conduct a functional testing of tournament.py using a live database."""

import unittest

from tournament import *


class TestTournament(unittest.TestCase):

    """Functional tests for tournament.py"""

    def test_delete_matches(self):
        delete_matches()
        print "* Old matches can be deleted."

    def test_delete(self):
        delete_matches()
        delete_players()
        print "* Player records can be deleted."

    def test_count(self):
        delete_matches()
        delete_players()
        c = count_players()
        if c == '0':
            raise TypeError(
                "count_players() should return numeric zero, not string '0'.")
        if c != 0:
            raise ValueError("After deleting, count_players should return zero.")
        print "* After deleting, count_players() returns zero."

    def test_register(self):
        delete_matches()
        delete_players()
        register_player("Chandra Nalaar")
        c = count_players()
        if c != 1:
            raise ValueError(
                "After one player registers, count_players() should be 1.")
        print "* After registering a player, count_players() returns 1."

    def test_register_tournament(self):
        tournament = register_tournament('My Tournament', 4)
        if not isinstance(tournament, int):
            raise ValueError("Tournament was not registered.")
        print "* Tournament registered."

    def test_register_player_in_tournament(self):
        delete_matches()
        delete_players()
        player = register_player("Chandra Nalaar")
        tournament = register_tournament('My Tournament', 4)
        registered = register_player_in_tournament(player, tournament)
        if registered != 1:
            raise ValueError("Player was not registered in tournament.")
        print "* Player registered in tournament."

    def test_register_count_delete(self):
        delete_matches()
        delete_players()
        register_player("Markov Chaney")
        register_player("Joe Malik")
        register_player("Mao Tsu-hsi")
        register_player("Atlanta Hope")
        c = count_players()
        if c != 4:
            raise ValueError(
                "After registering four players, count_players should be 4.")
        delete_players()
        c = count_players()
        if c != 0:
            raise ValueError("After deleting, count_players should return zero.")
        print "* Players can be registered and deleted."

    def test_standings_before_matches(self):
        delete_matches()
        delete_players()
        register_player("Melpomene Murray")
        register_player("Randy Schwartz")
        standings = player_standings()
        if len(standings) < 2:
            raise ValueError("Players should appear in player_standings even before "
                            "they have played any matches.")
        elif len(standings) > 2:
            raise ValueError("Only registered players should appear in standings.")
        if len(standings[0]) != 4:
            raise ValueError("Each player_standings row should have four columns.")
        [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
        if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
            raise ValueError(
                "Newly registered players should have no matches or wins.")
        if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
            raise ValueError("Registered players' names should appear in standings, "
                            "even if they have no matches played.")
        print "* Newly registered players appear in the standings with no matches."

    def test_report_matches(self):
        delete_matches()
        delete_players()
        tournament = register_tournament("Report Matches Tournament", 4)
        register_player_in_tournament(register_player("Bruno Walton"), tournament)
        register_player_in_tournament(register_player("Boots O'Neal"), tournament)
        register_player_in_tournament(register_player("Cathy Burton"), tournament)
        register_player_in_tournament(register_player("Diane Grant"), tournament)
        standings = player_standings()
        [id1, id2, id3, id4] = [row[0] for row in standings]
        report_match(id1, id2, tournament)
        report_match(id3, id4, tournament)
        standings = player_standings()
        for (i, n, w, m) in standings:
            if m != 1:
                raise ValueError("Each player should have one match recorded.")
            if i in (id1, id3) and w != 1:
                raise ValueError("Each match winner should have one win recorded.")
            elif i in (id2, id4) and w != 0:
                raise ValueError("Each match loser should have zero wins recorded.")
        print "* After a match, players have updated standings."

    def test_pairings(self):
        delete_matches()
        delete_players()
        tournament = register_tournament("Test Pairings Tournament", 4)
        register_player_in_tournament(register_player("Twilight Sparkle"), tournament)
        register_player_in_tournament(register_player("Fluttershy"), tournament)
        register_player_in_tournament(register_player("Applejack"), tournament)
        register_player_in_tournament(register_player("Pinkie Pie"), tournament)
        standings = player_standings_by_tournament(tournament)
        [id1, id2, id3, id4] = [row[0] for row in standings]
        report_match(id1, id2, tournament)
        report_match(id3, id4, tournament)
        pairings = swiss_pairings(tournament)
        if len(pairings) != 2:
            raise ValueError(
                "For four players, swiss_pairings should return two pairs.")
        [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
        correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
        actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
        if correct_pairs != actual_pairs:
            raise ValueError(
                "After one match, players with one win should be paired.")
        print "* After one match, players with one win are paired."


if __name__ == '__main__':
    unittest.main()
