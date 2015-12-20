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

To support Sessions I created:

* NDB Models: `Session`, `Speaker`
* Messages: `SessionMessage`, `SessionsMessage`, `SpeakerMessage`
* Endpoints: `create_session`, `get_conference_sessions`, `get_conference_sessions_by_type`, `get_sessions_by_speaker`
* Helpers: `_get_entity_by_key`

Models and messages can be found in [models.py](https://github.com/brenj/udacity/blob/master/conference_organization_app/conference_central/models.py#L52), and endpoints (with related code) can be found in [conference.py](https://github.com/brenj/udacity/blob/master/conference_organization_app/conference_central/conference.py#L559).

> Explain in a couple of paragraphs your design choices for session and speaker implementation.

Sessions, in the context of this project, are blocks of time at a conference for a speaker to discuss a topic, run a workshop, etc… In a traditional RDBMS the relationship between session and conference would be one-to-many, where many sessions would relate to one, and only one, conference. To model this relationship in Google’s `Datastore` I chose to use the ancestor relationship (though other options are available e.g. `ReferenceProperty`). Entities can be given a hierarchical structure in `Datastore` by assigning a parent entity at the time of (child) entity creation. This allows corresponding entities to be retrieved from both sides of the relationship. So for a given session the conference that the session is scheduled in can be obtained, and similarly for a given conference, all sessions in that conference can be obtained.

A speaker is an individual who provides the content for a session at a conference. Rather than defining the speaker property as a `StringProperty`, I decided to use `StructuredProperty` instead. The reason for this is that we may want to store more information about a speaker than just his or her name (e.g. for a speaker page on the `Conference Central` website). Also, a speaker may participate in more than one session at a conference, and storing/updating a `StringProperty` across multiple sessions is less efficient and more error-prone.

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
