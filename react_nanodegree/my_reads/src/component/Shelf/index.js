import PropTypes from 'prop-types';
import React from 'react';

import './shelf.css';
import BookList from '../BookList';

function Shelf(props) {
  const books = props.books;
  const name = props.name;

  return (
    <div>
      <h2 className="bookshelf-title">{name}</h2>
      <BookList books={books} />
    </div>
  );
}

Shelf.propTypes = {
  books: PropTypes.arrayOf(
    PropTypes.shape({
      authors: PropTypes.array.isRequired,
      id: PropTypes.string.isRequired,
      imageLinks: PropTypes.shape({
        thumbnail: PropTypes.string.isRequired,
      }).isRequired,
    }).isRequired,
  ).isRequired,
  name: PropTypes.string.isRequired,
};

export default Shelf;
