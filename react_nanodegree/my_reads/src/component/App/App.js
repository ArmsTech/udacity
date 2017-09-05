import React from 'react';

import './App.css';

class App extends React.Component {
  render() {
    return <div><BookList books={this.props.books} /></div>;
  }
}

class BookList extends React.Component {
  render() {
    const books = this.props.books;

    return (
      <ul className="books-grid">
        {books.map(book => (
          <li key={book.id} className="books-grid">
            <Book book={book} />
          </li>))}
      </ul>
    );
  }
}

class Book extends React.Component {
  render() {
    const book = this.props.book;

    const authors = book.authors.join(', ');
    const thumbnail = book.imageLinks.thumbnail;

    return (
      <div className="book">
        <div className="book-top">
          <div
            className="book-cover"
            style={{ backgroundImage: `url(${thumbnail})` }}
          />
          <div className="book-shelf-changer">
            <select>
              <option value="none" disabled>Move to...</option>
              <option value="currentlyReading">Currently Reading</option>
              <option value="wantToRead">Want to Read</option>
              <option value="read">Read</option>
              <option value="none">None</option>
            </select>
          </div>
        </div>
        <div className="book-title">{book.title}</div>
        <div className="book-authors">{authors}</div>
      </div>
    );
  }
}

export default App;
