MyReads: A Book Lending App
===========================

About
-----
From Udacity:
> Create a React application from scratch and utilize React components to
> manage the user interface. You’ll create a virtual bookcase to store your
> books and track what you're reading. Using the provided Books API, you’ll
> search for books and add them to a bookshelf as a React component. Use
> React's setState to build the functionality to move books from one shelf to
> another.

Supporting courses:
* React Fundamentals

MyReads was created using `create-react-app`, and the only starter code provided
was the interface to Udacity's books API. I chose to modify this interface
slightly to fix some inconsistencies in the data.

Requirements
------------
* Node
* Node Package Manager (npm)

Install
-------
1. `npm install`
2. `npm start`

Code Quality
------------
This code base adheres to the [Airbnb JavaScript/React/JSX Style Guide](https://github.com/airbnb/javascript)  
Use `npm run lint` to check syntax and style.

Code Organization (src)
-----------------------

``` console
├── App.css                                                                                      │
├── App.js                                                                                       │
├── api                                                                                          │
│   └── books-api.js                                                                             │
├── component                                                                                    │
│   ├── Book                                                                                     │
│   │   ├── book.css                                                                             │
│   │   └── index.js                                                                             │
│   ├── BookDetails                                                                              │
│   │   └── index.js                                                                             │
│   ├── BookList                                                                                 │
│   │   ├── book-list.css                                                                        │
│   │   └── index.js                                                                             │
│   ├── BookSearch                                                                               │
│   │   ├── book-search.css                                                                      │
│   │   └── index.js                                                                             │
│   ├── Footer                                                                                   │
│   │   ├── footer.css                                                                           │
│   │   └── index.js                                                                             │
│   ├── NavBar                                                                                   │
│   │   └── index.js                                                                             │
│   └── Shelf                                                                                    │
│       ├── index.js                                                                             │
│       └── shelf.css                                                                            │
├── index.css                                                                                    │
├── index.js                                                                                     │
└── registerServiceWorker.js
```

Grading (by Udacity)
--------------------

Criteria           |Highest Grade Possible  |Grade Recieved
-------------------|------------------------|--------------
Application Setup  |Meets Specifications    |
Main Page          |Meets Specifications    |
Search Page        |Meets Specifications    |
Routing            |Meets Specifications    |
Code Functionality |Meets Specifications    |
