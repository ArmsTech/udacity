import PropTypes from 'prop-types';
import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Container, Dropdown, Icon, Menu } from 'semantic-ui-react';

const UDACITY_URL = 'https://www.udacity.com/course/react-nanodegree--nd019';
const GITHUB_URL = (
  'https://github.com/brenj/udacity/tree/master/react_nanodegree/my_reads');
const LINKEDIN_URL = 'https://www.linkedin.com/in/brenj';

const propTypes = {
  activeMenuItem: PropTypes.string.isRequired,
};

function NavBar(props) {
  const { activeMenuItem } = props;

  return (
    <Menu pointing inverted size="small">
      <Container>
        <Menu.Item>
          <Menu.Item header>
            <Icon name="book" size="big" color="blue" />
            MyReads
          </Menu.Item>
        </Menu.Item>
        <Menu.Item
          name="home"
          as={Link}
          to="/"
          active={activeMenuItem === 'home'}
        />
        <Menu.Item
          name="search"
          as={Link}
          to="/search"
          active={activeMenuItem === 'search'}
        />
        <Menu.Menu position="right">
          <Dropdown
            item
            icon={<Icon name="ellipsis horizontal" size="big" />}
          >
            <Dropdown.Menu>
              <Dropdown.Item
                onClick={() => {
                  window.location = UDACITY_URL;
                }}
              >
                <Icon name="info circle" />
                React Nanodegree
              </Dropdown.Item>
              <Dropdown.Item
                onClick={() => {
                  window.location = GITHUB_URL;
                }}
              >
                <Icon name="github alternate" />
                Source Code
              </Dropdown.Item>
              <Dropdown.Item
                onClick={() => {
                  window.location = LINKEDIN_URL;
                }}
              >
                <Icon name="linkedin square" />
                Connect on LinkedIn
              </Dropdown.Item>
            </Dropdown.Menu>
          </Dropdown>
          <Menu.Item>
            <Button
              primary
              content="Add Book"
              as={Link}
              to="/search"
            />
          </Menu.Item>
        </Menu.Menu>
      </Container>
    </Menu>
  );
}

NavBar.propTypes = propTypes;

export default NavBar;
