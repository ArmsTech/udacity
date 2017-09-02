import React from 'react';
import ReactDOM from 'react-dom';

import './index.css';
import MyReads from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<MyReads />, document.getElementById('root'));
registerServiceWorker();
