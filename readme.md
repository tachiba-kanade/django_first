# Project Title

Game Leaderboard Dashboard

## Problem Statement

Build a web-based leaderboard and game statistics dashboard using Django and PostgreSQL.

The application should allow players, games, and game scores to be stored in a PostgreSQL database. Users should be able to view a dashboard containing overall statistics, recent scores, and a leaderboard showing the highest-performing players.

The main purpose of the project is to learn the fundamentals of Django by building a small but complete application from scratch.

---

## Primary Goal

Create a Django application that:

- Uses PostgreSQL as its database.
- Stores players, games, and scores.
- Displays a leaderboard.
- Displays basic dashboard statistics.
- Allows new scores to be submitted through the website.
- Uses Django Admin for managing data.

---

# Core Entities

## Player

Represents a person who participates in games.

Think about storing information such as:

- Name
- Username or nickname
- Date joined

You should decide which fields are actually necessary.

---

## Game

Represents a game in which players can receive scores.

Examples:

- Chess
- FIFA
- Valorant
- Mario Kart
- Table Tennis

Think about storing:

- Game name
- Category
- Date added

---

## Score

Represents a score achieved by a player in a particular game.

A score must belong to:

- One Player
- One Game

It should also contain:

- Score value
- Date/time the score was recorded

---

# Functional Requirements

## 1. Homepage Dashboard

Create a dashboard at:

`/`

The dashboard should display at least:

- Total number of players
- Total number of games
- Total number of recorded scores
- Highest score recorded

The page should also show:

- Top players
- Recent score submissions

---

## 2. Leaderboard Page

Create a page at:

`/leaderboard/`

Display score information in a table.

Example:

| Rank | Player | Game | Score |
| --- | --- | --- | --- |
| 1 | Alex | Mario Kart | 9500 |
| 2 | Maya | FIFA | 8800 |
| 3 | John | Valorant | 8200 |

The results should be ordered from highest score to lowest score.

---

## 3. Submit Score

Create a page at:

`/scores/add/`

Users should be able to:

- Select a player
- Select a game
- Enter a score
- Submit the form

After submitting successfully, the score should be stored in PostgreSQL.

---

## 4. Player List

Create:

`/players/`

Display all registered players.

Each player should show some basic information such as:

- Name
- Number of scores submitted
- Highest score

---

## 5. Game List

Create:

`/games/`

Display all available games.

Each game should show something like:

- Game name
- Category
- Number of recorded scores

---

# Django Admin Requirements

Register your models with Django Admin.

Through the admin panel, you should be able to:

- Add players
- Edit players
- Delete players
- Add games
- Edit games
- Delete games
- Add scores
- View submitted scores

Try to make the admin list pages useful rather than leaving everything completely default.

---

# Database Requirement

Use PostgreSQL instead of SQLite.

The application should have its own PostgreSQL:

- Database
- Database user

Django should connect to PostgreSQL through its database configuration.

Database credentials should not be committed directly into version control.

---

# UI Requirements

Keep the UI simple.

You do not need React, Next.js, or any frontend framework.

Use:

- Django templates
- HTML
- CSS

You may optionally use Bootstrap later.

Create a reusable base template containing common elements such as:

- Navigation
- Page layout
- Styles

Other pages should extend that template.

---

# Suggested Navigation

Your website could have:

`Dashboard | Leaderboard | Players | Games | Add Score | Admin`

---

# Project Phases

## Phase 1 — Django Setup

Goal:

Get Django running.

Complete when:

- Django project exists
- One Django app exists
- Development server runs
- Homepage responds successfully

---

## Phase 2 — PostgreSQL Setup

Goal:

Connect Django to PostgreSQL.

Complete when:

- PostgreSQL database exists
- PostgreSQL application user exists
- Django successfully connects
- Django migrations run successfully

---

## Phase 3 — Data Models

Create the models required to represent:

- Players
- Games
- Scores

Complete when:

- Models are created
- Relationships are correct
- Migrations succeed
- Database tables exist

---

## Phase 4 — Django Admin

Register all models.

Add some test data manually through Django Admin.

For example:

5 players

3 games

15–20 scores

This data will help you build the rest of the application.

---

## Phase 5 — Leaderboard

Build `/leaderboard/`.

Retrieve scores using the Django ORM.

Order them from highest to lowest.

Display them using a Django template.

Do not hard-code leaderboard data.

---

## Phase 6 — Dashboard

Build `/`.

Calculate statistics using Django ORM queries.

Display:

- Player count
- Game count
- Score count
- Highest score
- Recent scores
- Top scores

---

## Phase 7 — Score Submission Form

Build a Django form that allows new scores to be submitted.

Validate the data before saving it.

After a successful submission, redirect the user to an appropriate page.

---

## Phase 8 — Player and Game Pages

Build:

`/players/`

and:

`/games/`

Use related database information to calculate useful statistics.

---

# Optional Features

Only start these after the basic application is complete.

Possible upgrades:

- Player profile page
- Game detail page
- Search
- Filter leaderboard by game
- Pagination
- Authentication
- Player accounts
- Charts using Chart.js
- Win/loss tracking
- Achievements or badges
- Score history
- REST API using Django REST Framework

---

# Constraints

For the first version:

Do not use:

- React
- Next.js
- Django REST Framework
- Docker
- Redis
- Celery
- Microservices

The purpose is to understand Django itself first.

---

# Main Concepts You Should Learn

By finishing this project, you should understand:

- Django project structure
- Django apps
- URLs
- Views
- Templates
- Template inheritance
- Models
- Migrations
- PostgreSQL integration
- Django ORM
- Foreign keys
- Forms
- Validation
- Django Admin
- Static files
- Query ordering
- Aggregations
- Relationships between database tables

---

# Definition of Done

The project is complete when a user can:

1. Open the website.
2. See dashboard statistics.
3. Browse players.
4. Browse games.
5. View a leaderboard.
6. Submit a new score.
7. Refresh the leaderboard and see the new score.
8. Manage players, games, and scores through Django Admin.
9. Confirm that all application data is stored in PostgreSQL.

---

# First Task

Do not start with the models.

Your first task is simply:

Create the Django project, create the Django application, connect it to PostgreSQL, run the initial migrations, and verify that the development server works.

Once that works, move on to the data models.