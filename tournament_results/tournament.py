"""Implementation of a Swiss-system tournament."""

import psycopg2

WIN = 1
LOSS = 2
TIE = 3


def connect():
    """Connect to the PostgreSQL tournament database.

    :returns: tournament database connection
    :rtype: psycopg2.connection

    """
    return psycopg2.connect("dbname=tournament")


def run_query(query, query_args=(), query_type='SELECT'):
    """Run a query against the tournament database.

    The query result will depend on the query type, although the result will
    always be contained in a dict or None. The scope of this project is small
    enough that opening and closing connections per query is acceptable.

    param str query: query string to run
    param tuple query_args: query args to pass to execute
    param query_type: query type to run (SELECT | UPDATE | DELETE | INSERT)
    :returns: query result; result type depends on query type
    :rtype: dict | None

    """
    query_type = query_type.upper()

    with connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, query_args)

            if query_type == 'SELECT':
                result = cursor.fetchall()
            elif query_type == 'INSERT' and 'RETURNING' in query:
                try:
                    # Requires RETURNING be used
                    result, = cursor.fetchone()
                except psycopg2.ProgrammingError:
                    result = None
            elif query_type in ('UPDATE', 'DELETE', 'INSERT'):
                result = cursor.rowcount
            else:
                raise ValueError(
                    "Query type %s is not supported." % query_type)

    return {'result': result}


def delete_all_from_table(table):
    """Delete all rows from a table.

    :param str table: name of the table to delete all rows from
    :returns: count of rows deleted
    :rtype: int

    """
    query = "DELETE FROM %s;" % table
    deleted = run_query(query, query_type='DELETE')
    return deleted['result']


def deleteMatches():
    """Delete all the match records from the database.

    :returns: count of rows deleted from match table
    :rtype: int

    """
    return delete_all_from_table('match')


def deletePlayers():
    """Delete all the player records from the database.

    :returns: count of rows deleted from player table
    :rtype: int

    """
    return delete_all_from_table('player')


def countPlayers():
    """Count of all players currently registered.

    :returns: count of all registered players
    :rtype: int

    """
    query = "SELECT count(id) FROM player;"
    players = run_query(query)
    return players['result'][0][0]


def registerPlayer(name):
    """Add a player to the tournament database.

    :param str name: name of player to register
    :returns: id of the registered player
    :rtype: int

    """
    query = "INSERT INTO player (name) VALUES (%s) RETURNING id;"
    inserted = run_query(query, query_args=(name,), query_type='INSERT')
    return inserted['result']


def register_tournament(name, players):
    """Add a tournament to the tournament database.

    :param str name: name of tournament to register
    :param int players: number of tournament entrants
    :returns: id of the registered tournament
    :rtype: int

    """
    query = ("INSERT INTO tournament (name, players) "
             "VALUES (%s, %s) "
             "RETURNING id;")
    inserted = run_query(
        query, query_args=(name, players), query_type='INSERT')
    return inserted['result']


def register_player_in_tournament(player, tournament):
    """Register a player in a tournament as an entrant.

    :param int player: id of the player to register
    :param int tournament: id of the tournament to register player in
    :returns: rowcount of the player inserted, 0 | 1
    :rtype: int

    """
    query = ("INSERT INTO entrant (player_id, tournament_id) "
             "VALUES (%s, %s);")
    inserted = run_query(
        query, query_args=(player, tournament), query_type='INSERT')
    return inserted['result']


def playerStandings():
    """Get a list of the players and their win records, sorted by wins.

    :returns: list of players and win records
    :rtype: list

    Return format:
        [(15, 'Bruno Walton', 2, 0), (16, "Boots O'Neal", 1, 0), ...]

    """
    query = ("SELECT id, name, wins, matches "
             "FROM player "
             "ORDER BY wins DESC;")
    standings = run_query(query)
    return standings['result']


def player_standings_by_tournament(tournament):
    """Get a list of the players and their win records by tournament.

    :param int tournament: id of tournament to get standings for
    :returns: list of players and win records
    :rtype: list

    Return format:
        [(15, 'Bruno Walton', 2, 0), (16, "Boots O'Neal", 1, 0), ...]

    """
    query = ("SELECT id, name, wins, matches "
             "FROM player p, entrant e "
             "WHERE p.id = e.player_id "
             "AND tournament_id = %s "
             "ORDER BY wins DESC;")
    standings = run_query(query, query_args=(tournament,))
    return standings['result']


def reportMatch(winner, loser, tournament):
    """Report the outcome of a single match between two players.

    :param int winner: id of the winner
    :param int loser: id of the loser
    :param int tournament: id of the tournament the match was played in
    :returns: id of the reported match
    :rtype: int

    """
    # Add winner
    query = ("INSERT INTO match "
             "(player_id, tournament_id, result_id) "
             "VALUES (%s, %s, %s) "
             "RETURNING id;")
    inserted = run_query(
        query,
        query_args=(winner, tournament, WIN), query_type='INSERT')

    match_id = inserted['result']

    # Add loser
    query = ("INSERT INTO match "
             "(id, player_id, tournament_id, result_id) "
             "VALUES (%s, %s, %s, %s);")
    run_query(
        query,
        query_args=(match_id, loser, tournament, LOSS), query_type='INSERT')

    # Update matches played for both players
    query = ("UPDATE player "
             "SET matches = matches + 1 "
             "WHERE id IN (%s, %s);")
    run_query(query, query_args=(winner, loser), query_type='UPDATE')

    # Update wins for winner
    query = ("UPDATE player "
             "SET wins = wins + 1 "
             "WHERE id = %s;")
    run_query(query, query_args=(winner,), query_type='UPDATE')

    return match_id


def swissPairings(tournament):
    """Pair players for the next round in a swiss-style tournament.

    Players are paired with an opponent with a equal or nearly-equal win
    record. A player cannot play the same opponent twice.

    :param int tournament: id of the tournament to pair the next round for
    :returns: tuples containing pairings in the format --
        (id1, name1, id2, name2)
    :rtype: list

    """
    standings = player_standings_by_tournament(tournament)

    players, opponents = [], []
    for index, standing in enumerate(standings):
        id, name = standing[:2]

        if index % 2 == 0:
            players.append((id, name))
        else:
            opponents.append((id, name))

    pairings = []
    for matchup in zip(players, opponents):
        player, opponent = matchup
        pairings.append(player + opponent)

    return pairings
