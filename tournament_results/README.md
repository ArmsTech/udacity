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

This tournament database meets (and exceeds) all requirements for the [Tournament Results](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) project,
and demonstrates familiarity with:

* Database design and normalization
* SQL statements (DML and DDL)
* PostgreSQL and the Python adapter Psycopg2
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

Quick Start
-----------

1. Clone vagrant environment: `git clone https://github.com/udacity/fullstack-nanodegree-vm.git fullstack`
2. Navigate to fullstack: `cd fullstack`
3. Bring up vagrant VM: `vagrant up`
4. SSH into vagrant VM: `vagrant ssh`
5. Install dependencies: `sudo apt-get install libpq-dev python-dev`
6. Upgrade psycopg2 (>= 2.5): `sudo pip install -U psycopg2`
7. Clone tournament repo (in VM): `git clone https://github.com/ArmsTech/udacity.git`
8. Navigate to tournament_results `cd udacity/tournament_results`
9. Add tournament package to path: `PYTHONPATH=/vagrant/udacity/tournament_results/tournament`
10. Run test suite: `python tournament/functional_tests/tournament/test_tournament.py`

Requirements
------------

* Vagrant
* VirtualBox
* Python >= 2.7
* Linux, Mac OS X

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
