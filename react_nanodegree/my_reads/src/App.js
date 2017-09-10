import React from 'react';
import { Route } from 'react-router-dom';

import './App.css';
import * as booksAPI from './api/books-api';
import BookSearch from './component/BookSearch';
import Footer from './component/Footer';
import Header from './component/Header';
import Shelf from './component/Shelf';

class App extends React.Component {
  state = {
    books: {
      currentlyReading: [],
      read: [],
      wantToRead: [],
    },
  };

  componentDidMount() {
    booksAPI.getAll().then((booksData) => {
      const books = {
        currentlyReading: [],
        read: [],
        wantToRead: [],
      };
      booksData.forEach((bookData) => {
        books[bookData.shelf].push(bookData);
      });
      this.setState({
        books,
      });
      console.log(books);
    });
  }

  onShelfChanged = (book, toShelf) => {
    const fromShelf = book.shelf;
    const specifiedBook = { ...book, shelf: toShelf };

    this.setState((prevState) => {
      const newState = { ...prevState };

      // Add specified book to new, valid shelf
      if (toShelf !== 'none') {
        newState.books[toShelf] = [
          ...newState.books[toShelf], specifiedBook];
      }

      // Remove specified book from old, valid shelf
      if (fromShelf !== 'none') {
        newState.books[fromShelf] = newState.books[fromShelf].filter(
          bookOnFromShelf => bookOnFromShelf.id !== specifiedBook.id);
      }
    });
  };


  render() {
    const books = this.state.books;

    return (
      <div>
        <Route
          exact
          path="/"
          render={() => (
            <div>
              <Header />
              <Shelf books={books.currentlyReading} name="Currently Reading" />
              <Shelf books={books.wantToRead} name="Want to Read" />
              <Shelf books={books.read} name="Read" />
              <Footer />
            </div>
          )}
        />
        <Route exact path="/search" component={BookSearch} />
      </div>
    );
  }
}

export default App;
