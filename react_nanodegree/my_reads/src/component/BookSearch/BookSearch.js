import PropTypes from 'prop-types';
import React from 'react';
import { Input, Message } from 'semantic-ui-react';

import './book-search.css';
import * as booksAPI from '../../api/books-api';
import BookList from '../BookList';

const propTypes = {
  onShelfChanged: PropTypes.func.isRequired,
};

class BookSearch extends React.Component {
  state = {
    books: [],
    loading: false,
    query: '',
  };

  handleChange = (event) => {
    const query = event.target.value;

    this.setState({ query, loading: true });
    this.searchBooks(query);
  };

  handleSubmit = (event) => {
    this.searchBooks(this.state.query);
    event.preventDefault();
  };

  searchBooks = (query) => {
    booksAPI.search(query).then((booksData) => {
      console.log(booksData);
      this.setState({ books: booksData, loading: false });
    });
  };

  render() {
    const { books, loading, query } = this.state;

    let noBooksFoundMessage = <Message hidden />;
    if (query && !loading && books.length <= 0) {
      noBooksFoundMessage = (
        <Message
          info
          size="small"
          content={`No books were found for the keyword: ${query}`}
        />
      );
    }

    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <div className="book-search">
            <Input
              autoFocus
              fluid
              loading={loading}
              icon="search"
              iconPosition="left"
              type="text"
              value={query}
              onChange={this.handleChange}
              placeholder="Search books by keyword (e.g. react, javascript)"
              size="huge"
            />
          </div>
        </form>
        <div className="book-search-message">
          {noBooksFoundMessage}
        </div>
        <BookList
          books={books}
          onShelfChanged={this.props.onShelfChanged}
        />
      </div>
    );
  }
}

BookSearch.propTypes = propTypes;

export default BookSearch;
