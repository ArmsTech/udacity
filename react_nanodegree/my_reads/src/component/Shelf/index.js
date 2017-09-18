import PropTypes from 'prop-types';
import React from 'react';
import { Segment } from 'semantic-ui-react';

import './shelf.css';
import BookList from '../BookList';

function Shelf(props) {
  const books = props.books;
  const name = props.name;

  return (
    <div>
      <Segment basic size="massive">{name}</Segment>
      <BookList books={books} onShelfChanged={props.onShelfChanged} />
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
