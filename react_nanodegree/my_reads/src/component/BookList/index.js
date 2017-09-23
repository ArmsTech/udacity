import PropTypes from 'prop-types';
import React from 'react';
import { Card } from 'semantic-ui-react';

import './book-list.css';
import Book from '../Book';

const propTypes = {
  books: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
    }).isRequired,
  ).isRequired,
  onShelfChanged: PropTypes.func.isRequired,
};

function BookList(props) {
  const { books } = props;

  return (
    <div className="book-list">
      <Card.Group itemsPerRow="4">
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

BookList.propTypes = propTypes;

export default BookList;
