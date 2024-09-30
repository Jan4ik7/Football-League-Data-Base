# Запросы для тестов
queries = {
    1: """
        SELECT team_name, COUNT(player_id) AS total_players
        FROM soccer_schema.Players
        JOIN soccer_schema.Teams USING (team_id)
        GROUP BY team_name;
    """,
    2: """
        SELECT p.player_id, p.first_name, p.last_name, AVG(p.the_goals) AS avg_goals
        FROM soccer_schema.Players p
        GROUP BY p.player_id, p.first_name, p.last_name
        ORDER BY avg_goals DESC;
    """,
    3: """
        SELECT p.first_name, p.last_name, SUM(p.the_goals) AS total_goals
        FROM soccer_schema.Players p
        JOIN soccer_schema.Season s ON p.season_id = s.season_id
        WHERE s.season_name = '2024-2025'
        GROUP BY p.first_name, p.last_name
        ORDER BY total_goals DESC
        LIMIT 5;
    """,
    4: """
        SELECT t.team_name, COUNT(m.match_id) AS total_matches
        FROM soccer_schema.Teams t
        LEFT JOIN soccer_schema.Matches m ON t.team_id = m.first_team_id OR t.team_id = m.second_team_id
        GROUP BY t.team_name
        HAVING COUNT(m.match_id) > 0;
    """,
    5: """
        SELECT t.team_name, AVG(m.first_team_score + m.second_team_score) AS avg_goals_per_match
        FROM soccer_schema.Teams t
        LEFT JOIN soccer_schema.Matches m ON t.team_id = m.first_team_id OR t.team_id = m.second_team_id
        GROUP BY t.team_name
        HAVING AVG(m.first_team_score + m.second_team_score) IS NOT NULL;
    """,
    6: """
        SELECT m.match_id, m.first_team_id, m.second_team_id, m.first_team_score, m.second_team_score
        FROM soccer_schema.Matches m
        JOIN soccer_schema.League l ON m.league_id = l.league_id
        WHERE m.first_team_score + m.second_team_score > (
            SELECT AVG(first_team_score + second_team_score) 
            FROM soccer_schema.Matches 
            WHERE league_id = m.league_id
        )
        ORDER BY m.match_date;
    """,
    7: """
        SELECT t.team_name, SUM(
            CASE 
                WHEN m.first_team_score > m.second_team_score THEN 3
                WHEN m.first_team_score = m.second_team_score THEN 1
                ELSE 0 
            END) AS total_points
        FROM soccer_schema.Teams t
        LEFT JOIN soccer_schema.Matches m ON t.team_id = m.first_team_id OR t.team_id = m.second_team_id
        GROUP BY t.team_name;
    """,
    8: """
        SELECT p.first_name, p.last_name, p.position
        FROM soccer_schema.Players p
        JOIN soccer_schema.Matches m ON p.team_id = m.first_team_id OR p.team_id = m.second_team_id
        WHERE m.match_id = 1;
    """,
    9: """
        SELECT l.league_name, AVG(t.rating) AS avg_team_rating
        FROM soccer_schema.Teams t
        JOIN soccer_schema.League l ON t.league_id = l.league_id
        GROUP BY l.league_name;
    """,
    10: """
        SELECT p.first_name, p.last_name, p.position, pun.punish_type, pun.punish_reason
        FROM soccer_schema.Players p
        JOIN soccer_schema.Punishments pun ON p.player_id = pun.player_id
        JOIN (
            SELECT Min(match_id) AS last_match_id
            FROM soccer_schema.Matches
        ) last_match ON pun.match_id = last_match.last_match_id;
    """
}