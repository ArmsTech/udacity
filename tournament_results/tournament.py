"""Implementation of a Swiss-system tournament."""

import psycopg2


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
            elif query_type in ('UPDATE', 'DELETE'):
                result = cursor.rowcount
            elif query_type == 'INSERT':
                try:
                    # Requires RETURNING be used
                    result, = cursor.fetchone()
                except psycopg2.ProgrammingError:
                    result = None
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
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


