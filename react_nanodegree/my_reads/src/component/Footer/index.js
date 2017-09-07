import React from 'react';

import './footer.css';
import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <div className="open-search">
      <Link to='/search'>Add a book</Link>
    </div>
  );
}
