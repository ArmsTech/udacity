import React from 'react';
import { Route, Switch } from 'react-router-dom';
import { Container, Header, Message } from 'semantic-ui-react';

import './App.css';
import * as booksAPI from './api/books-api';
import BookSearch from './component/BookSearch';
import Footer from './component/Footer';
import NavBar from './component/NavBar';
import Shelf from './component/Shelf';

const PageNotFound = () => (
  <div>
    <NavBar activeMenuItem="none" />
    <Container textAlign="center" className="not-found-message">
      <Header content="404" size="huge" />
      <Header size="large">Page Not Found</Header>
    </Container>
    <Footer />
  </div>
);

class App extends React.Component {
  state = {
    books: {
      currentlyReading: [],
      read: [],
      wantToRead: [],
    },
    welcomeVisible: true,
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
      this.setState({ books });
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

    booksAPI.update(specifiedBook, toShelf);
  }

  handleDismissWelcome = () => {
    this.setState({ welcomeVisible: false });
  }

  render() {
    const books = this.state.books;

    return (
      <div>
        <Switch>
          <Route
            exact
            path="/"
            render={() => (
              <div>
                <NavBar activeMenuItem="home" />
                <Container>
                  {this.state.welcomeVisible &&
                    <div className="welcome-message">
                      <Message
                        onDismiss={this.handleDismissWelcome}
                        header="Welcome to Udacity MyReads!"
                        content="A bookshelf app for finding and organizing your favorite books."
                        size="big"
                        color="blue"
                      />
                    </div>
                  }
                  <Shelf
                    books={books.currentlyReading}
                    name="Books you're currently reading"
                    onShelfChanged={this.onShelfChanged}
                  />
                  <Shelf
                    books={books.wantToRead}
                    name="Books you want to read"
                    onShelfChanged={this.onShelfChanged}
                  />
                  <Shelf
                    books={books.read}
                    name="Books you've finished reading"
                    onShelfChanged={this.onShelfChanged}
                  />
                </Container>
              </div>
            )}
          />
          <Route
            exact
            path="/search"
            render={() => (
              <div>
                <NavBar activeMenuItem="search" />
                <Container>
                  <BookSearch onShelfChanged={this.onShelfChanged} />
                </Container>
              </div>
            )}
          />
          <Route component={PageNotFound} />
        </Switch>
        <Footer />
      </div>
    );
  }
}

export default App;
