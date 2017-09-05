import React from 'react';
import ReactDOM from 'react-dom';

import './index.css';
import App from './component/App';
import * as booksAPI from './api/books-api';
import registerServiceWorker from './registerServiceWorker';

booksAPI.getAll().then(books => {
  console.log(books);
  ReactDOM.render(<App books={books} />, document.getElementById('root'));
});

// ReactDOM.render(<App books={books} />, document.getElementById('root'));
registerServiceWorker();
