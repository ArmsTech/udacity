import React from 'react';
import { Icon, Segment } from 'semantic-ui-react';

import './footer.css';

export default function Footer() {
  return (
    <div className="footer">
      <Segment inverted textAlign="center" size="small">
        <span className="footer-text">
          Created and maintained by @brenj on
          <Icon name="github" size="big" />
        </span>
      </Segment>
    </div>
  );
}
