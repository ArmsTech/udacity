"""Functional testing of tournament.py using a tournament database."""

import os
import unittest
import subprocess

from tournament import *

SQL_FILE_PATH = os.path.realpath(
    os.path.join(
        os.path.abspath(__file__),
        os.pardir, os.pardir, os.pardir,
        os.pardir, 'tournament.sql'))


class TestTournament(unittest.TestCase):

    """Functional tests for tournament.py."""

    def setUp(self):
        """Create a fresh tournament database."""
        try:
            subprocess.check_call(
                ['psql', '-f', SQL_FILE_PATH],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as error:
            raise RuntimeError(
                "SQL file %s could not be executed: %s" % (
                    SQL_FILE_PATH, error))

    def tearDown(self):
        """Destroy the tournament database."""
        try:
            # DROP cannot run in a transaction block, so use psql
            subprocess.check_call(
                ['psql', '-c', "DROP DATABASE tournament;"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as error:
            raise RuntimeError(
                "The tournament database could not be dropped: %s" % (error))

    def test_delete_matches(self):
        """Test matches can be deleted."""
        tournament = register_tournament("Test Delete Matches", 2)

        player1 = register_player("Twilight Sparkle")
        player2 = register_player("Fluttershy")

        register_player_in_tournament(player1, tournament)
        register_player_in_tournament(player2, tournament)

        report_match(player1, player2, tournament)

        matches_deleted = delete_matches()
        self.assertEqual(matches_deleted, 2)
        print "* Old matches can be deleted."

    def test_delete_players(self):
        """Test players can be deleted."""
        register_player("Twilight Sparkle")
        register_player("Fluttershy")

        players_deleted = delete_players()
        self.assertEqual(players_deleted, 2)
        print "* Player records can be deleted."

    def test_count(self):
        """Test players can be counted."""
        register_player("Twilight Sparkle")
        register_player("Fluttershy")
        counted_players = count_players()

        # We should have two players that we just registered
        self.assertEqual(counted_players, 2)

        delete_players()
        counted_players = count_players()

        # count_players() should return numeric zero, not string '0'
        self.assertNotIsInstance(counted_players, str)

        # After deleting, count_players should return zero
        self.assertEqual(counted_players, 0)
        print "* After deleting, count_players() returns zero."

    def test_register(self):
        """Test players can be registered."""
        register_player("Chandra Nalaar")
        counted_players = count_players()

        # After one player registers, count_players() should be 1
        self.assertEqual(counted_players, 1)
        print "* After registering a player, count_players() returns 1."

    def test_register_tournament(self):
        """Test tournaments can be registered."""
        tournament = register_tournament('Test Tournament', 4)

        self.assertIsInstance(tournament, int)
        print "* Tournament registered."

    def test_register_player_in_tournament(self):
        """Test players can be registered in tournaments."""
        player = register_player("Chandra Nalaar")
        tournament = register_tournament('My Tournament', 4)
        registered = register_player_in_tournament(player, tournament)

        self.assertEqual(registered, 1)
        print "* Player registered in tournament."

    def test_register_count_delete(self):
        """Test players can be registered and deleted."""
        register_player("Markov Chaney")
        register_player("Joe Malik")
        register_player("Mao Tsu-hsi")
        register_player("Atlanta Hope")

        counted_players = count_players()
        # After registering four players, count_players should be 4
        self.assertEqual(counted_players, 4)

        delete_players()
        counted_players = count_players()
        # After deleting, count_players should return zero
        self.assertEqual(counted_players, 0)
        print "* Players can be registered and deleted."

    def test_standings_before_matches(self):
        """Test players standings before matches."""
        register_player("Melpomene Murray")
        register_player("Randy Schwartz")
        standings = player_standings()

        # Players should appear in player_standings before playing in matches
        # Only registered players should appear in standings
        self.assertEqual(len(standings), 2)

        # Each player_standings row should have four columns
        self.assertEqual(len(standings[0]), 4)

        # Newly registered players should have no matches or wins
        [(id1, name1, wins1, match1), (id2, name2, wins2, match2)] = standings
        for standing in (match1, match2, wins1, wins2):
            self.assertEqual(standing, 0)

        # Registered players' names should appear in standings even when
        # no matches have been played.
        self.assertEqual(
            set([name1, name2]), set(["Melpomene Murray", "Randy Schwartz"]))
        print ("* Newly registered players appear in the "
               "standings with no matches.")

    def test_report_matches(self):
        """Test reporting matches."""
        tournament = register_tournament("Test Matches Tournament", 4)
        players = (
            "Bruno Walton", "Boots O'Neal", "Cathy Burton", "Diane Grant")
        for player in players:
            register_player_in_tournament(register_player(player), tournament)

        standings = player_standings_by_tournament(tournament)
        player1, player2, player3, player4 = [row[0] for row in standings]
        report_match(player1, player2, tournament)
        report_match(player3, player4, tournament)

        standings = player_standings()
        for id, name, wins, matches in standings:
            # Each player should have one match recorded
            self.assertEqual(matches, 1)
            # Each match winner should have one win recorded
            if id in (player1, player3):
                self.assertEqual(wins, 1)
            # Each match loser should have zero wins recorded
            elif id in (player2, player4):
                self.assertEqual(wins, 0)
        print "* After a match, players have updated standings."

    def test_pairings(self):
        """Test pairing players."""
        tournament = register_tournament("Test Pairings Tournament", 4)
        players = ("Twilight Sparkle", "Fluttershy", "Applejack", "Pinkie Pie")
        for player in players:
            register_player_in_tournament(register_player(player), tournament)

        standings = player_standings_by_tournament(tournament)
        player1, player2, player3, player4 = [row[0] for row in standings]
        report_match(player1, player2, tournament)
        report_match(player3, player4, tournament)
        pairings = swiss_pairings(tournament)

        # For four players, swiss_pairings should return two pairs
        self.assertEqual(len(pairings), 2)
        # After one match, players with one win should be paired
        [(id1, name1, id2, name2), (id3, name3, id4, name4)] = pairings
        correct_pairs = set([
            frozenset([player1, player3]), frozenset([player2, player4])])
        actual_pairs = set([frozenset([id1, id2]), frozenset([id3, id4])])
        self.assertEqual(actual_pairs, correct_pairs)
        print "* After one match, players with one win are paired."


if __name__ == '__main__':
    unittest.main()
