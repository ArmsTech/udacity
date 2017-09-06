import React from 'react';
import { Link, Route } from 'react-router-dom'

import './App.css';
import BookSearch from '../BookSearch'

class App extends React.Component {
  render() {
    const books = this.props.books;

    return (
      <div>
        <Route exact path='/' render={() => (
          <div>
            <Header />
            <Shelf books={books.currentlyReading} name='Currently Reading' />
            <Shelf books={books.wantToRead} name='Want to Read' />
            <Shelf books={books.read} name='Read' />
            <Footer />
          </div>
        )} />
        <Route exact path='/search' component={BookSearch} />
      </div>
    );
  }
}

function Header() {
  return (
    <div>
      <h1>MyReads</h1>
      <hr />
    </div>
    );
}

function Footer() {
  return (
    <div className="open-search">
      <Link to='/search'>Add a book</Link>
    </div>
    );
}

class Shelf extends React.Component {
  render() {
    const books = this.props.books;
    const name = this.props.name;

    return (
      <div>
        <h2 className="bookshelf-title">{name}</h2>
        <BookList books={books} />
      </div>
    );
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
