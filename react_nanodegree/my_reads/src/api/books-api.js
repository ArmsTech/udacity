
const api = "https://reactnd-books-api.udacity.com"


// Generate a unique token for storing your bookshelf data on the backend server.
let token = localStorage.token
if (!token)
  token = localStorage.token = Math.random().toString(36).substr(-8)

const headers = {
  'Accept': 'application/json',
  'Authorization': token
}

const cleanBooksData = (booksData) => {
  // Fix inconsistencies in book data returned by API
  return booksData.map((bookData) => {
    return {
      authors: [],
      description: '',
      shelf: 'none',
      subtitle: '',
      imageLinks: {
        thumbnail: '',
        smallThumbnail: '',
      },
      ...bookData,
    }
  })
}

export const get = (bookId) =>
  fetch(`${api}/books/${bookId}`, { headers })
    .then(res => res.json())
    .then(data => data.book)

export const getAll = () =>
  fetch(`${api}/books`, { headers })
    .then(res => res.json())
    .then(data => cleanBooksData(data.books))

export const update = (book, shelf) =>
  fetch(`${api}/books/${book.id}`, {
    method: 'PUT',
    headers: {
      ...headers,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ shelf })
  }).then(res => res.json())

export const search = (query, maxResults) =>
  fetch(`${api}/search`, {
    method: 'POST',
    headers: {
      ...headers,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ query, maxResults })
  }).then(res => res.json())
    .then(data => {
      // Honor maxResults parameter because API doesn't
      const booksData = data.books.slice(0, maxResults);
      return cleanBooksData(booksData);
    })
    // No search results shouldn't be an error
    .catch(error => [])
