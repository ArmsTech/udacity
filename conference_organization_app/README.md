Conference Organization App
===========================

About
-----

From Udacity:

> You will develop a cloud-based API server to support a provided conference organization application that exists on the web as well as a native Android application. The API supports the following functionality found within the app: user authentication, user profiles, conference information and various manners in which to query the data.

Supporting Course:

*  [Developing Scalable Apps in Python](https://www.udacity.com/course/developing-scalable-apps-in-python--ud858)

**Important Note**

The deliverable for this project is largely in the form of API endpoints for Conference Central, an application code-base provided by Udacity. These endpoints were created using `Google Cloud Endpoints` on the `Google App Engine` platform, and are only accessible using the `Google APIs Explorer`. Integrating these endpoints into the Conference Central front-end is not part of this project. 

Most of the code in this project was provided by Udacity and does not reflect my coding style or abilities. To highlight my contributions I have included references in this README to the functions, classes, etc... that I created to complete the project.

Tasks
-----

##### Add Sessions to a Conference

To support sessions I created:

* NDB Models: `Session`, `Speaker`
* Messages: `SessionRequestMessage`, `SessionResponseMessage`, `SessionsResponseMessage`, `SpeakerRequestMessage`, `SpeakerResponseMessage`
* Endpoints: `create_session`, `create_speaker`, `get_conference_sessions`, `get_conference_sessions_by_type`, `get_sessions_by_speaker`
* Helpers: `_get_entity_by_key`

Models and messages can be found in [models.py](https://github.com/brenj/udacity/blob/master/conference_organization_app/conference_central/models.py#L52), and endpoints (with related code) can be found in [conference.py](https://github.com/brenj/udacity/blob/master/conference_organization_app/conference_central/conference.py#L559).

> Explain in a couple of paragraphs your design choices for session and speaker implementation.

Sessions, in the context of this project, are blocks of time at a conference for a speaker to discuss a topic, run a workshop, etc… In a traditional RDBMS the relationship between session and conference would be one-to-many, where many sessions would relate to one, and only one, conference. To model this relationship in Google’s `Datastore` I chose to use the ancestor relationship (though other options are available e.g. `KeyProperty`). Entities can be given a hierarchical structure in `Datastore` by assigning a parent entity at the time of (child) entity creation. This allows corresponding entities to be retrieved from both sides of the relationship. So for a given session the conference that the session is scheduled in can be obtained, and similarly for a given conference, all sessions in that conference can be obtained.

A speaker is an individual who provides the content for a session at a conference. Rather than defining the speaker property as a `StringProperty`, I decided to use `KeyProperty` instead. The reason for this is that we may want to store more information about a speaker than just his or her name (e.g. for a speaker page on the `Conference Central` website), so Speaker should be defined as a separate model and associated with a session through it's unique key. 
Modeling speaker this way also means that there is a way to identify a speaker, a speakers sessions, etc… without relying on a non-unique attribute (e.g. name).

Please note that this means a new session requires a `speaker_key ` (url-safe key) to specify a speaker. To store a new speaker use the `create_speaker` endpoint (the speaker's key will be in the response).

##### Add Sessions to User Wishlist

To support a user wishlist I created:

* Properties: `sessions_wishlist` in the `Profile` model
* Endpoints: `add_session_to_wishlist`, `get_sessions_in_wishlist`, `delete_session_in_wishlist`
* Helpers: `_get_wishlist_sessions`, `_get_wishlist_sessions_as_message`

##### Work on indexes and queries

> Make sure the indexes support the type of queries required by the new Endpoints methods.

No additions to `index.yaml` are needed for my implementation of the endpoints methods in tasks one and two. Only the indexes that `Datastore` automatically predefines for each property of each kind are required.

> Think about other types of queries that would be useful for this application. Describe the purpose of 2 new queries and write the code that would perform them.

Query 1:

* To plan their day, users of the `Conference Central` application may be interested in seeing sessions available for a given conference on a particular day with results ordered by time.

```python
sessions = Session.query(ancestor=conference.key).filter(
    Session.date == request.date).order(Session.start_time).fetch()
```

This query would require the following entry in `index.yaml`:

```yaml
- kind: Session
  properties:
  - name: date
  - name: start_time
```
 
Query 2:

* `Conference Central` users may want to see all the sessions at a conference that are interactive.

```python
# Assuming `workshop`, `hackathon`, and `lab` are the only interactive
# session types
sessions = Session.query(
    Session.type_of_session.IN(
        ('workshop', 'hackathon', 'lab'))).fetch()
```

> Let’s say that you don't like workshops and you don't like sessions after 7 pm. How would you handle a query for all non-workshop sessions before 7 pm? What is the problem for implementing this query? What ways to solve it did you think of?

If you were to implement this query the straightforward way you'd recieve an error like this:

 ```python
 BadRequestError: Cannot have inequality filters on multiple properties
 ```

This error is due to a restriction on `Datastore` queries whereby inequality filters are limited to at most one property; we would be using two. The reason for this restriction has to do with how `Datastore` works (index-based query mechanism). On a basic level `Datastore` queries rely on potential results being adjacent to one another to avoid scanning an entire index (very inefficient), so operations that require this are disallowed.

Here are some ways to work around this restriction:

* Create a `BooleanProperty` on `Session` to show whether the session occurs before or after 7 PM. That way you would only need to query for one inequality.

```python
sessions = Session.query().filter(
    Session.type_of_session != 'workshop').filter(
        Session.is_after_7pm == True).fetch()
```

* Query for all sessions that are not workshops, then filter those results programmatically by comparing each session’s time.

```python
sessions = Session.query().filter(
    Session.type_of_session != 'workshop').fetch()
seven_pm = datetime.strptime('19:00', '%H:%M').time()
sessions = [session for session in sessions if session.start_time <= seven_pm]
```

* Determine all non-workshop session types (by hard-coding or querying), and then search for all sessions where type of session is in non-workshop types and occurs before or at 7 PM.

```python
seven_pm = datetime.strptime('19:00', '%H:%M').time()
sessions = Session.query(
    Session.type_of_session.IN(NON_WORKSHOP_TYPES)).filter(
        Session.start_time <= seven_pm).fetch()
```

This solution also requires an additional index:

```yaml
- kind: Session
  properties:
  - name: type_of_session
  - name: start_time
```

This solution is implemented in the endpoint: `get_sessions_nonworkshop_before_7pm`

##### Add a Task

To support a featured speaker I created:

* Endpoints: `get_featured_speaker`
* Handlers: `StoreFeaturedSpeaker`

This solution also requires an additional index:

```yaml
- kind: Session
  ancestor: yes
  properties:
  - name: speaker_key
  - name: name
```

Install
-------

* Pending

Requirements
------------

* Pending

Grading (by Udacity)
--------------------

Criteria       |Highest Grade Possible  |Grade Recieved
---------------|------------------------|--------------
App Architecture  |Meets Specifications  |TBD
Design Choices (Implementation)  |Exceeds Specifications  |TBD
Design Choices (Response)  |Exceeds Specifications  |TBD
Session Wishlist  |Meets Specifications  |TBD
Additional Queries  |Meets Specifications  |TBD
Query Problem  |Exceeds Specifications  |TBD
Featured Speaker  |Meets Specifications  |TBD
Code Quality   |Meets Specifications    |TBD
Comments       |Exceeds Specifications  |TBD
Documentation  |Meets Specifications    |TBD
