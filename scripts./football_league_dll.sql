-- Создание схемы
CREATE SCHEMA soccer_schema;

-- Таблица League
CREATE TABLE soccer_schema.League (
    league_id INT PRIMARY KEY,
    league_name VARCHAR(255) NOT NULL,
    logo BYTEA,
    sponsors VARCHAR(1024),
    rating FLOAT CHECK (rating >= 0 AND rating <= 10)
);
-- Таблица Teams
CREATE TABLE soccer_schema.Teams (
    team_id SERIAL PRIMARY KEY,
    players_count INT,
    team_name VARCHAR(255) NOT NULL,
    team_logo BYTEA,
    league_id INT,
    rating FLOAT CHECK (rating >= 0 AND rating <= 10),
    FOREIGN KEY (league_id) REFERENCES soccer_schema.League(league_id)
);

-- Таблица Season
CREATE TABLE soccer_schema.Season (
    season_id SERIAL PRIMARY KEY,
    season_name VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    league_id INT,
    games_count INT,
    win_score INT,
    lose_score INT,
    draw_score INT,
    final_score INT,
    team_id INT,
    FOREIGN KEY (league_id) REFERENCES soccer_schema.League(league_id),
    FOREIGN KEY (team_id) REFERENCES  soccer_schema.Teams(team_id)
);

-- Таблица Players
CREATE TABLE soccer_schema.Players (
    player_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    the_goals INT,
    the_assists INT,
    the_saves INT,
    position VARCHAR(255) NOT NULL,
    team_id INT,
    season_id INT,
    FOREIGN KEY (team_id) REFERENCES soccer_schema.Teams(team_id),
    FOREIGN KEY (season_id) REFERENCES soccer_schema.Season(season_id)
);

-- Таблица Matches
CREATE TABLE soccer_schema.Matches (
    match_id SERIAL PRIMARY KEY,
    first_team_id INT,
    second_team_id INT,
    first_team_score INT,
    second_team_score INT,
    first_team_ball_possession FLOAT,
    second_team_ball_possession FLOAT,
    match_date DATE NOT NULL,
    season_id INT,
    league_id INT,
    FOREIGN KEY (first_team_id) REFERENCES soccer_schema.Teams(team_id),
    FOREIGN KEY (second_team_id) REFERENCES soccer_schema.Teams(team_id),
    FOREIGN KEY (season_id) REFERENCES soccer_schema.Season(season_id),
    FOREIGN KEY (league_id) REFERENCES soccer_schema.League(league_id)
);

-- Таблица Punishments
CREATE TABLE soccer_schema.Punishments (
    punish_id SERIAL PRIMARY KEY,
    punish_type VARCHAR(255) NOT NULL,
    punish_reason VARCHAR(255),
    match_id INT,
    player_id INT,
    FOREIGN KEY (match_id) REFERENCES soccer_schema.Matches(match_id),
    FOREIGN KEY (player_id) REFERENCES soccer_schema.Players(player_id)
);

-- Таблица PlayerTransfer
CREATE TABLE soccer_schema.PlayerTransfer (
    transfer_id SERIAL PRIMARY KEY,
    player_id INT,
    from_team_id INT,
    date_from_team DATE,
    to_team_id INT,
    date_to_team DATE,
    FOREIGN KEY (player_id) REFERENCES soccer_schema.Players(player_id),
    FOREIGN KEY (from_team_id) REFERENCES soccer_schema.Teams(team_id),
    FOREIGN KEY (to_team_id) REFERENCES soccer_schema.Teams(team_id)
);
