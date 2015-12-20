Conference Organization App
===========================

About
-----

From Udacity:

> You will develop a cloud-based API server to support a provided conference organization application that exists on the web as well as a native Android application. The API supports the following functionality found within the app: user authentication, user profiles, conference information and various manners in which to query the data.

Supporting Course:

*  [Developing Scalable Apps in Python](https://www.udacity.com/course/developing-scalable-apps-in-python--ud858)

**Important Note**

The deliverable for this project is largely in the form of API endpoints for Conference Central, an application code-base provided by Udacity. These endpoints were created using Google Cloud Endpoints on the Google App Engine platform, and are only accessible using the Google API explorer. Integrating these endpoints into the Conference Central front-end is not part of this project. 

Most of the code in this project was provided by Udacity and does not reflect my coding style or abilities. To highlight my contributions I have included references in this README to the functions, classes, etc... that I created to complete the project.

Tasks
-----

##### Add Sessions to a Conference

To support Sessions I created:

* NDB Models: `Session`, `Speaker`
* Messages: `SessionMessage`, `SessionsMessage`, `SpeakerMessage`
* Endpoints: `create_session`, `get_conference_sessions`, `get_conference_sessions_by_type`, `get_sessions_by_speaker`
* Helpers: `_get_entity_by_key`

Models and Messages can be found in [models.py](https://github.com/brenj/udacity/blob/master/conference_organization_app/conference_central/models.py#L52), and endpoints (with related code) can be found in [conference.py](https://github.com/brenj/udacity/blob/master/conference_organization_app/conference_central/conference.py#L559).

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
