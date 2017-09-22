import PropTypes from 'prop-types';
import React from 'react';
import { Button, Header, Icon, Modal } from 'semantic-ui-react';

const bookDetailsButton = (
  <Button attached="right" color="blue" icon={<Icon name="info" />} />
);

const propTypes = {
  book: PropTypes.shape({
    authors: PropTypes.array.isRequired,
    description: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    subtitle: PropTypes.string.isRequired,
  }).isRequired,
};

function BookDetails(props) {
  const { book } = props;

  const authors = book.authors.join(', ');
  let title = book.title;

  if ('subtitle' in book) {
    title = [title, book.subtitle].join(': ');
  }

  return (
    <Modal trigger={bookDetailsButton}>
      <Modal.Header>{title}</Modal.Header>
      <Modal.Content scrolling>
        <Modal.Description>
          <Header as="h5" color="grey">{authors}</Header>
          <p>{book.description}</p>
        </Modal.Description>
      </Modal.Content>
    </Modal>
  );
}

BookDetails.propTypes = propTypes;

export default BookDetails;
