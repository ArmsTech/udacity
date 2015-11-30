Item Catalog
============

About
-----
From Udacity:
> You will develop an application that provides a list of items within a
> variety of categories as well as provide a user registration and
> authentication system. Registered users will have the ability to post,
> edit, and delete their own items.

Tech Quote (TQ) hosts technology-related quotes, specifically quotes relating
to programming languages. The TQ application meets all requirements for
the Item Catalog project by implementing the following:

* JSON API endpoint at `quote/api/v1/quotes`
* Data is read from a PostgreSQL database using SQLAlchemy
* Forms exist for adding/editing data with validation and CSRF protection
  with WTForms
* Data created by a user can can be deleted by (only) that user as a POST
  request and with CSRF protection
* OAuth2 login via GitHub
* Code is well organized and self-documenting adhering to both PEP8 and PEP257

The following Flask extensions and patterns were leveraged:

* Flask-Assets
* Flask-Login
* Flask-Migrate
* Flask-Script
* Flask-SQLAlchemy
* Flask-Uploads
* Flask-WTF

* Packages
* Blueprints
* Application factory
* View decorators (login & template rendering)
* Template inheritance
* Message flashing
* Custom error pages

Requirements
------------

* [Vagrant](http://www.vagrantup.com/downloads.html)

Configuration
-------------

All configuration is accomplished by environmental variables.
The following variables are available:

*APP_SETTINGS* 
- Configuration object to be used to run application.

*DATABASE_URI*
- Database connection string to connect to application database.

*GITHUB_ID*
- OAuth2 client id provided by GitHub for access to API.

*GITHUB_SECRET*
- OAuth2 client secret provided by GitHub for access to API.

*TQ_SECRET*
- A byte string which is the master key by which all values are encoded.
  Set to a sufficiently long string of characters that is difficult to
  guess or bruteforce (recommended at least 16 characters) for example
  the output of os.urandom(16).

Quick Start
-----------

1. `git clone https://github.com/brenj/fullstack-nanodegree-vm.git fullstack && cd fullstack/vagrant`
2. `vagrant up`
3. `vagrant ssh`
4. `cd /vagrant/udacity/item_catalog/`
5. `virtualenv venv && . venv/bin/activate`
6. `. bin/set-env-vars.sh` (after updating configuration values in `.env`, see Configuration)
7. `make install`
8. `make prod`

Grading (by Udacity)
--------------------

Criteria       |Highest Grade Possible  |Grade Recieved
---------------|------------------------|--------------
API Endpoints  |Exceeds Specifications  |TBD
CRUD: Create   |Exceeds Specifications  |TBD
CRUD: Read     |Exceeds Specifications  |TBD
CRUD: Update   |Exceeds Specifications  |TBD
CRUD: Delete   |Exceeds Specifications  |TBD
Authentication & Authorization   |Exceeds Specifications  |TBD
Code Quality   |Meets Specifications  |TBD
Comments       |Meets Specifications  |TBD
Documentation  |Meets Specifications    |TBD
