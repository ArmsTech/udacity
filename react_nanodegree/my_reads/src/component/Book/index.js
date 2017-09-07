import React from 'react';

import './book.css';

export default function Book(props) {
  const book = props.book;

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
