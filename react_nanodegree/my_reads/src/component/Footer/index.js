import React from 'react';

import { Link } from 'react-router-dom';
import './footer.css';

export default function Footer() {
  return (
    <div className="open-search">
      <Link to="/search">Add a book</Link>
    </div>
  );
}
