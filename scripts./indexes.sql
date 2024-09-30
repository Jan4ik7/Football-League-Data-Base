-- Индекс для таблицы Matches на season_id и league_id
CREATE INDEX idx_matches_season_league ON soccer_schema.Matches (season_id, league_id);

-- Индекс для таблицы Matches на match_date
CREATE INDEX idx_matches_match_date ON soccer_schema.Matches (match_date);

-- Индекс для таблицы Players на team_id и season_id
CREATE INDEX idx_players_team_season ON soccer_schema.Players (team_id, season_id);

-- Индекс для таблицы PlayerTransfer на player_id
CREATE INDEX idx_playertransfer_player_id ON soccer_schema.PlayerTransfer (player_id);

-- Индекс для таблицы PlayerTransfer на from_team_id и to_team_id
CREATE INDEX idx_playertransfer_team_id ON soccer_schema.PlayerTransfer (from_team_id, to_team_id);

-- Индекс для таблицы Punishments на match_id
CREATE INDEX idx_punishments_match_id ON soccer_schema.Punishments (match_id);

-- Индекс для таблицы Punishments на player_id
CREATE INDEX idx_punishments_player_id ON soccer_schema.Punishments (player_id);
