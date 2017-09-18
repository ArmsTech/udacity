import React from 'react';
import { Link } from 'react-router-dom';
import { Button, Container, Dropdown, Menu } from 'semantic-ui-react';

import './navbar.css';

export default class NavBar extends React.Component {
  state = { activeItem: 'home' };

  handleItemClick = (e, { name }) => {
    this.setState({ activeItem: name });
  }

  render() {
    const { activeItem } = this.state;

    return (
      <div className="navbar">
        <Menu pointing inverted size="small">
          <Container>
            <Menu.Item>
              <Menu.Item header>MyReads</Menu.Item>
            </Menu.Item>
            <Menu.Item
              name="home"
              as={Link}
              to="/"
              active={activeItem === 'home'}
              onClick={this.handleItemClick}
            />
            <Menu.Item
              name="search"
              as={Link}
              to="/search"
              active={activeItem === 'search'}
              onClick={this.handleItemClick}
            />
            <Menu.Menu position="right">
              <Dropdown item text="About">
                <Dropdown.Menu>
                  <Dropdown.Item>
                    <a href="https://www.udacity.com/course/react-nanodegree--nd019">Project</a>
                  </Dropdown.Item>
                  <Dropdown.Item>
                    <a href="https://github.com/brenj">Source</a>
                  </Dropdown.Item>
                  <Dropdown.Item>
                    <a href="https://www.linkedin.com/in/brenj/">Connect</a>
                  </Dropdown.Item>
                </Dropdown.Menu>
              </Dropdown>
              <Menu.Item>
                <Button
                  name="search"
                  primary
                  content="Add Book"
                  as={Link}
                  to="/search"
                  onClick={this.handleItemClick}
                />
              </Menu.Item>
            </Menu.Menu>
          </Container>
        </Menu>
      </div>
    );
  }
}
