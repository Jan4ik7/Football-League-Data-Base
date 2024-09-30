
Таблицы в Markdown:

1. Таблица Punishments:

| Название | Описание | Тип данных | Ограничения |
|---|---|---|---|
| punish_id | Идентификатор наказания | INT | PRIMARY KEY |
| punish_type | Тип наказания | VARCHAR(255) | NOT NULL |
| punish_reason | Причина наказания | VARCHAR(255) | NULL |
| match_id | ID матча | INT | FOREIGN KEY REFERENCES Matches(match_id) |
| player_id | ID игрока | INT | FOREIGN KEY REFERENCES Players(player_id) |


2. Таблица Matches:

| Название | Описание | Тип данных | Ограничения |
|---|---|---|---|
| match_id | ID матча | INT | PRIMARY KEY |
| first_team_id | ID первой команды | INT | FOREIGN KEY REFERENCES Teams(team_id) |
| second_team_id | ID второй команды | INT | FOREIGN KEY REFERENCES Teams(team_id) |
| first_team_score | Счет первой команды | INT | NULL |
| second_team_score | Счет второй команды | INT | NULL |
| first_team_ball_possession | Владение мячом первой команды | FLOAT | NULL |
| second_team_ball_possession | Владение мячом второй команды | FLOAT | NULL |
| match date | Дата матча | DATE | NOT NULL |
| season_id | ID сезона | INT | FOREIGN KEY REFERENCES Season(season_id) |
| league_id | ID лиги | INT | FOREIGN KEY REFERENCES League(league_id) |


3. Таблица Teams:

| Название | Описание | Тип данных | Ограничения |
|---|---|---|---|
| team_id | ID команды | INT | PRIMARY KEY |
| players_count | Количество игроков | INT | NULL |
| team_name | Название команды | VARCHAR(255) | NOT NULL |
| team_logo | Логотип команды | BLOB | NULL |
| rating       | Рейтинг лиги   | FLOAT      | CHECK (rating >= 0 AND rating <= 10) |
| league_id | ID лиги | INT | FOREIGN KEY REFERENCES Leagues(league_id) 


4. Таблица  Players:

| Название | Описание | Тип данных | Ограничения |
|---|---|---|---|
| player_id | ID игрока | INT | PRIMARY KEY |
| first_name | Имя | VARCHAR(255) | NOT NULL |
| last_name| Фамилия | VARCHAR(255) | NOT NULL |
| birth_date | Дата рождения | DATE | NOT NULL |
| the_goals | Забитые мячи   | INT | NULL |
| the_assists | Голевые передачи | INT | NULL |
| the_saves | Cпасение ворот | INT | NULL |
| position | Позиция | VARCHAR(255) | NOT NULL |
| team_id | ID команды | INT | FOREIGN KEY REFERENCES Teams(team_id) |
| season_id | ID сезона | INT | FOREIGN KEY REFERENCES Season(season_id) |


5. Таблица PlayerTransfer:

| Название | Описание | Тип данных | Ограничения |
|---|---|---|---|
| transfer_id | ID трансфера | INT | PRIMARY KEY |
| player_id | ID игрока | INT | FOREIGN KEY REFERENCES Players(player_id) |
| from_team_id | ID команды, из которой ушел | INT | FOREIGN KEY REFERENCES Teams(team_id) |
| date_from_team | Дата ухода из команды | DATE | NULL |
| to_team_id | ID команды, в которую пришел | INT | FOREIGN KEY REFERENCES Teams(team_id) |
| date_to_team | Дата прихода в команду | DATE | NULL |


6. Таблица League:

| Название     | Описание       | Тип данных  | Ограничения  |
|--------------|----------------|------------|--------------|
| league_id    | ID лиги        | INT        | PRIMARY KEY  |
| league_name  | Название лиги  | VARCHAR(255) | NOT NULL  |
| logo         | Логотип лиги   | BLOB       | NULL         |
| sponsors     | Спонсоры лиги  | VARCHAR(1024) |              |
| rating       | Рейтинг лиги   | FLOAT      | CHECK (rating >= 0 AND rating <= 10) |



7.  Таблица Season:


| Название | Описание | Тип данных | Ограничения |
|---|---|---|---|
| season_id | ID сезона | INT | PRIMARY KEY |
| season_name | Название сезона | VARCHAR(255) | NOT NULL |
| start_date | Дата начала | DATE | NOT NULL |
| end_date | Дата окончания | DATE | NOT NULL |
| games_count | Количество игр | INT | NULL |
| win_score | Средний счет победителя | INT | NULL |
| lose_score | Средний счет проигравшего | INT | NULL |
| draw_score | Средний счет ничьих | INT | NULL |
| final_score | Средний итоговый счет | INT | NULL |
| team_id | ID команды | INT | FOREIGN KEY REFERENCES Teams(team_id) |
| league_id | ID лиги | INT | FOREIGN KEY REFERENCES League(league_id) |