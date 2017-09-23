import PropTypes from 'prop-types';
import React from 'react';
import { Segment } from 'semantic-ui-react';

import './shelf.css';
import BookList from '../BookList';

const propTypes = {
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
  onShelfChanged: PropTypes.func.isRequired,
};

function Shelf(props) {
  const { books, name } = props;

  return (
    <div className="shelf">
      <Segment basic size="big" className="light-text">{name}</Segment>
      <BookList books={books} onShelfChanged={props.onShelfChanged} />
    </div>
  );
}

Shelf.propTypes = propTypes;

export default Shelf;
