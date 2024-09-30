-- Представление для таблицы Teams
CREATE VIEW soccer_schema.TeamsView AS
SELECT
    t.team_id,
    t.players_count,
    t.team_name,
    t.team_logo,
    t.league_id,
    l.league_name,
    l.rating AS league_rating
FROM
    soccer_schema.Teams t
INNER JOIN
    soccer_schema.League l ON t.league_id = l.league_id;

-- Представление для таблицы Players
CREATE VIEW soccer_schema.PlayersView AS
SELECT
    p.player_id,
    p.first_name,
    p.last_name,
    p.birth_date,
    p.the_goals,
    p.the_assists,
    p.the_saves,
    p.position,
    t.team_name,
    s.season_name
FROM
    soccer_schema.Players p
INNER JOIN
    soccer_schema.Teams t ON p.team_id = t.team_id
INNER JOIN
    soccer_schema.Season s ON p.season_id = s.season_id;

-- Представление для таблицы Matches
CREATE VIEW soccer_schema.MatchesView AS
SELECT
    m.match_id,
    m.first_team_id,
    t1.team_name AS first_team_name,
    m.second_team_id,
    t2.team_name AS second_team_name,
    m.first_team_score,
    m.second_team_score,
    m.first_team_ball_possession,
    m.second_team_ball_possession,
    m.match_date,
    s.season_name,
    l.league_name
FROM
    soccer_schema.Matches m
INNER JOIN
    soccer_schema.Teams t1 ON m.first_team_id = t1.team_id
INNER JOIN
    soccer_schema.Teams t2 ON m.second_team_id = t2.team_id
INNER JOIN
    soccer_schema.Season s ON m.season_id = s.season_id
INNER JOIN
    soccer_schema.League l ON m.league_id = l.league_id;
