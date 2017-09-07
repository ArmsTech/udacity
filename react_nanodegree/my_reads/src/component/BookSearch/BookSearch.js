import React from 'react';
import { Link } from 'react-router-dom';

import './book-search.css';

class BookSearch extends React.Component {
  render() {
    return (
      <div>
        <Link className="close-search" to="/">Close</Link>
        <form>
          <div className="search-books-input-wrapper">;
            <input type="text" placeholder="Search by title or author" />
          </div>
        </form>
      </div>
    );
  }
}

export default BookSearch;
