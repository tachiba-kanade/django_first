
GameHub Dashboard

Players        Games Played       Highest Score

   24                86                 9500
-------------------------------------------------

🏆 Leaderboard

1. Alex       9500
2. John       8700
3. Sudo       8200
4. Maya       7600

-------------------------------------------------

Recent Scores

Sudo     Mario Kart     8200
Alex     Valorant       9500
Maya     FIFA           7600


GameHub Leaderboard
You have games like:
- Chess
- FIFA
- Valorant
- Mario Kart
- Table Tennis
- Anything you want
  

Each player submits a score/result.

Your dashboard could show:
- 🏆 Top 5 players
- 🎮 Total games played
- 👤 Total players
- 🔥 Highest score
- 📊 Scores by game
- 🕒 Recent matches
- Leaderboard table

so summing up leaderboards updates if someone tops scores meaning  we have to divide the project

- setup the database with primary key as id
- other fields - name, game (dropdown option), score, total games played(that particular game )




- 
django-admin startproject my_project .

 Notice the  . (space followed by a period) at the end of the command. This tells Django to install the project files directly into your current folder instead of nesting them inside a secondary, redundant subdirectory.


1. pip install psycopg2-binary
Django requires a Python database adapter to talk to PostgreSQL

2. Configure Django settings.py:
   Open your Django project's main settings.py file. Look for the DATABASES dictionary (which uses SQLite by default) and replace it with your PostgreSQL

3. python manage.py migrate

4. Once the tables successfully populate, your connection is fully active. You can optionally run python manage.py createsuperuser to set up an administrative login.