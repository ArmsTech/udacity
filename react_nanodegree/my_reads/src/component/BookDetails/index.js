import React from 'react';
import { Button, Header, Icon, Modal } from 'semantic-ui-react';

const bookDetailsIcon = <Icon name="info" size="big" />;
const bookDetailsButton = (
  <Button circular color="blue" icon={bookDetailsIcon} />
);

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

export default BookDetails;
