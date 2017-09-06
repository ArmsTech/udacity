import React from 'react';

import './book-list.css';
import Book from '../Book';

export default function BookList(props) {
  const books =props.books;

  return (
    <ul className="books-grid">
      {books.map(book => (
        <li key={book.id} className="books-grid">
          <Book book={book} />
        </li>))}
    </ul>
  );
}
