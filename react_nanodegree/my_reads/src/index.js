import React from 'react';
import ReactDOM from 'react-dom';

import './index.css';
import App from './component/App';
import * as booksAPI from './api/books-api';
import registerServiceWorker from './registerServiceWorker';

booksAPI.getAll().then((books) => {
  const booksByShelf = {
    currentlyReading: [],
    read: [],
    wantToRead: [],
  };
  books.forEach((book) => {
    booksByShelf[book.shelf].push(book);
  });
  console.log(booksByShelf);
  ReactDOM.render(<App books={booksByShelf} />, document.getElementById('root'));
});

// ReactDOM.render(<App books={books} />, document.getElementById('root'));
registerServiceWorker();
