import psycopg2
import queries
import pytest

def establish_connection():
    return psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="postgres",
        user="postgres",
        password="password"
    )

def create_cursor(connection):
    return connection.cursor()

def close_cursor(cursor):
    cursor.close()

def close_connection(connection):
    connection.close()

def test_query_1():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[1])
    results = cursor.fetchall()
    assert len(results) > 0, "No teams found"
    assert all(len(row) == 2 for row in results), "Incorrect result format for Test 1"
    print("Test 1 passed")

    for team_name, total_players in results:
        if team_name == 'Ураган':
            assert total_players == 3, "Total players count for team Ураган is not equal to 3"
            print("Total players count for team Ураган is 3")
            break
    else:
        assert False, "Team Ураган not found in the results"

    close_cursor(cursor)
    close_connection(connection)

def test_query_2():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[2])
    results = cursor.fetchall()
    assert len(results) > 0, "No player goal averages found"
    assert all(len(row) == 4 for row in results), "Incorrect result format for Test 2"

    if len(results) >= 2:
        first_player_avg_goals = results[0][3]
        second_player_avg_goals = results[1][3]
        assert first_player_avg_goals > second_player_avg_goals, "First player's average goals should be higher than second player's"
        print("First player's average goals are higher than second player's")
    else:
        print("Insufficient data to compare average goals of players")
    print("Test 2 passed")

    close_cursor(cursor)
    close_connection(connection)

def test_query_3():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[3])
    results = cursor.fetchall()
    assert len(results) > 0, "No players found for the season"
    assert all(len(row) == 3 for row in results), "Incorrect result format for Test 3"

    assert len(results) == 5, "Number of teams in the season does not match the limit"
    print("Number of teams in the season matches the limit")
    print("Test 3 passed")

    close_cursor(cursor)
    close_connection(connection)

def test_query_4():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[4])
    results = cursor.fetchall()
    assert len(results) > 0, "No matches found for any team"
    assert all(len(row) == 2 for row in results), "Incorrect result format for Test 4"

    for team_name, total_matches in results:
        assert total_matches > 0, f"Team {team_name} has no matches"
    print("Each team has at least one match")
    print("Test 4 passed")

    close_cursor(cursor)
    close_connection(connection)

def test_query_5():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[5])
    results = cursor.fetchall()
    assert len(results) > 0, "No average goals found for any team"
    assert all(len(row) == 2 for row in results), "Incorrect result format for Test 5"

    for team_name, avg_goals_per_match in results:
        assert avg_goals_per_match is not None and avg_goals_per_match >= 2, f"Team {team_name} has less than 2 goal in matches"
    print("Each team has scored at least two goals in matches")
    print("Test 5 passed")

    close_cursor(cursor)
    close_connection(connection)

def test_query_6():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[6])
    results = cursor.fetchall()
    assert len(results) > 0, "No matches found with above average goals"
    assert all(len(row) == 5 for row in results), "Incorrect result format for Test 6"

    for match_id, first_team_id, second_team_id, first_team_score, second_team_score in results:
        assert first_team_score + second_team_score > 0, f"Match {match_id} has less than 1 goal"
    print("Each match has more than 0 goals")
    print("Test 6 passed")

    close_cursor(cursor)
    close_connection(connection)

def test_query_7():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[7])
    results = cursor.fetchall()
    assert len(results) > 0, "No points found for any team"
    assert all(len(row) == 2 for row in results), "Incorrect result format for Test 7"

    for team_name, total_points in results:
        assert total_points is not None and total_points >= 0, f"Team {team_name} has negative points"
    print("Each team has non-negative total points")
    print("Test 7 passed")

    close_cursor(cursor)
    close_connection(connection)

def test_query_8():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[8])
    results = cursor.fetchall()
    assert len(results) > 0, "No players found for the match"
    assert all(len(row) == 3 for row in results), "Incorrect result format for Test 8"

    for first_name, last_name, position in results:
        assert position.strip(), f"Player {first_name} {last_name} has no position"
    print("Each player has a position")
    print("Test 8 passed")

    close_cursor(cursor)
    close_connection(connection)

def test_query_9():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[9])
    results = cursor.fetchall()
    assert len(results) > 0, "No average ratings found for any league"
    assert all(len(row) == 2 for row in results), "Incorrect result format for Test 9"

    for league_name, avg_team_rating in results:
        assert avg_team_rating is not None and avg_team_rating >= 5, f"League {league_name} has negative average rating"
    print("Each league has an average rating of 5")
    print("Test 9 passed")

    close_cursor(cursor)
    close_connection(connection)

def test_query_10():
    connection = establish_connection()
    cursor = create_cursor(connection)

    cursor.execute(queries.queries[10])
    results = cursor.fetchall()
    assert len(results) > 0, "No punishments found for any player"
    assert all(len(row) == 5 for row in results), "Incorrect result format for Test 10"

    for first_name, last_name, position, punish_type, punish_reason in results:
        assert first_name.strip() and last_name.strip() and position.strip() and punish_type.strip() and punish_reason.strip(), "Missing player information or punishment details"
    print("All players have complete information about their punishment")
    print("Test 10 passed")

    close_cursor(cursor)
    close_connection(connection)


