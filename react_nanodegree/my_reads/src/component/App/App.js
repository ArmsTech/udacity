import React from 'react';
import { Link, Route } from 'react-router-dom'

import './App.css';
import Book from '../Book'
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

export default App;
