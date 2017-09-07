import React from 'react';

import './shelf.css';
import BookList from '../BookList';

export default function Shelf(props) {
  const books = props.books;
  const name = props.name;

  return (
    <div>
      <h2 className="bookshelf-title">{name}</h2>
      <BookList books={books} />
    </div>
  );
}
