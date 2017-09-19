import React from 'react';
import { Input, Message } from 'semantic-ui-react';

import './book-search.css';
import * as booksAPI from '../../api/books-api';
import BookList from '../BookList';

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
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <div className="book-search">
            <Input
              fluid
              loading={loading}
              icon='search'
              iconPosition='left'
              type="text"
              value={query}
              onChange={this.handleChange}
              placeholder="Search books by keyword (e.g. react, javascript)"
              size="huge"
            />
          </div>
        </form>
        <BookList
          books={books}
          onShelfChanged={this.props.onShelfChanged}
        />
      </div>
    );
  }
}

export default BookSearch;
