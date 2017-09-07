import PropTypes from 'prop-types';
import React from 'react';

import './book-list.css';
import Book from '../Book';

function BookList(props) {
  const books = props.books;

  return (
    <ul className="books-grid">
      {books.map(book => (
        <li key={book.id} className="books-grid">
          <Book book={book} />
        </li>))}
    </ul>
  );
}

BookList.propTypes = {
  books: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
    }).isRequired,
  ).isRequired,
};

export default BookList;
