import React from 'react';
import ReactDOM from 'react-dom';

import './index.css';
import MyReadsApp from './component/MyReadsApp/MyReadsApp';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<MyReadsApp />, document.getElementById('root'));
registerServiceWorker();
