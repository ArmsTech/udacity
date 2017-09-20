import PropTypes from 'prop-types';
import React from 'react';
import { Card, Image } from 'semantic-ui-react';

import './book.css';

const propTypes = {
  book: PropTypes.shape({
    authors: PropTypes.array.isRequired,
    imageLinks: PropTypes.shape({
      thumbnail: PropTypes.string.isRequired,
    }).isRequired,
    shelf: PropTypes.string.isRequired,
  }).isRequired,
  onShelfChanged: PropTypes.func.isRequired,
};

class Book extends React.Component {
  state = {
    shelf: 'none',
  };

  componentWillMount() {
    this.setState({ shelf: this.props.book.shelf });
  }

  handleChange = (event) => {
    const toShelf = event.target.value;

    this.setState({ shelf: toShelf });
    this.props.onShelfChanged(this.props.book, toShelf);
  };

  render() {
    const book = this.props.book;

    const authors = book.authors.join(', ');
    const thumbnail = book.imageLinks.thumbnail;

    return (
      <div className="book">
        <Card fluid>
          <Image
            centered
            shape="rounded"
            src={thumbnail}
            width="220"
            height="220"
          />
          <Card.Content extra textAlign="center">
            <select
              className="ui dropdown"
              value={this.state.shelf}
              onChange={this.handleChange}
            >
              <option value="move" disabled>Choose a shelf ...</option>
              <option value="currentlyReading">Currently Reading</option>
              <option value="wantToRead">Want to Read</option>
              <option value="read">Finished Reading</option>
              <option value="none">No shelf</option>
            </select>
          </Card.Content>
        </Card>
      </div>
    );
  }
}

Book.propTypes = propTypes;

export default Book;
