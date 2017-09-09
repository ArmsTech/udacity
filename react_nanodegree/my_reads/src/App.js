import React from 'react';
import { Route } from 'react-router-dom';

import './App.css';
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
