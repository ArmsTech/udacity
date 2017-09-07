import React from 'react';
import { Link, Route } from 'react-router-dom';

import './App.css';
import BookSearch from '../BookSearch';
import Header from '../Header';
import Shelf from '../Shelf';

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

function Footer() {
  return (
    <div className="open-search">
      <Link to='/search'>Add a book</Link>
    </div>
    );
}

export default App;
