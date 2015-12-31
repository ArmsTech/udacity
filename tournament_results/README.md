Tournament Results
==================

About
-----
From Udacity:
> In this project, you’ll be writing a Python module that uses the PostgreSQL
> database to keep track of players and matches in a game tournament. The
> game tournament will use the Swiss system for pairing up players in each
> round: players are not eliminated, and each player should be paired with
> another player with the same number of wins, or as close as possible.

Supporting course:

* [Intro to Relational Databases](https://www.udacity.com/course/intro-to-relational-databases--ud197)

This tournament database meets (and exceeds) all requirements for the [Tournament Results](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) project,
and demonstrates familiarity with:

* Database design and normalization
* SQL statements (DML and DDL)
* PostgreSQL and the Python adapter `psycopg2`
* Development of an API backed by a database
* Use of functional tests to validate results

Tournament rules and design:

1. Players compete against other players of similar rank
2. Players cannot play the same opponent more than once
3. Players can receive byes (a free win), but only once per tournament
4. Individual games in a round can result in a tie (win for both players)
5. Players with the same number of wins are ranked by Opponent Match Wins
6. Players can play in multiple tournaments

_More on Swiss-style tournament system:_ http://en.wikipedia.org/wiki/Swiss-system_tournament

The `original_files` folder contains the files provided by Udacity for this
project, unchanged. Changes were made to conform to Python's standards and best
practices.

Model
-----

![ER Model](https://raw.githubusercontent.com/brenj/udacity/master/tournament_results/docs/erd.png)

Install
-------

1. `git clone https://github.com/brenj/fullstack-nanodegree-vm.git fullstack && cd fullstack/vagrant`
2. `vagrant up`
3. `vagrant ssh`
4. `cd /vagrant/udacity/tournament_results/`
5. `virtualenv venv && . venv/bin/activate`
6. `pip install -r requirements.txt`
7. `export PYTHONPATH=/vagrant/udacity/tournament_results/tournament` (add package to path)
8. `python tournament/functional_tests/tournament/test_tournament.py` (run the test suite)

Requirements
------------

* [Vagrant](http://www.vagrantup.com/downloads.html)

Grading (by Udacity)
--------------------

Criteria       |Highest Grade Possible  |Grade Recieved
---------------|------------------------|--------------
Functionality  |Exceeds Specifications  |Exceeds Specifications
Table Design   |Exceeds Specifications  |Exceeds Specifications
Column Design  |Exceeds Specifications  |Exceeds Specifications
Code Quality   |Exceeds Specifications  |Exceeds Specifications
Comments       |Exceeds Specifications  |Exceeds Specifications
Documentation  |Meets Specifications    |Meets Specifications
