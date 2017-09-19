import PropTypes from 'prop-types';
import React from 'react';
import { Card } from 'semantic-ui-react';

import './book-list.css';
import Book from '../Book';

function BookList(props) {
  const books = props.books;

  return (
    <div className="book-list">
      <Card.Group>
        {books.map(book => (
          <Book
            book={book}
            onShelfChanged={props.onShelfChanged}
            key={book.id}
          />
        ))}
      </Card.Group>
    </div>
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
