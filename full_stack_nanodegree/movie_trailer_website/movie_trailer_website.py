"""Allow page visitors to review movie details and watch trailers."""

import fresh_tomatoes

# MOVIE_STORE is meant to resemble a database relation. The keys do not imply
# any order. They are only intended to represent a surrogate/auto key.
MOVIE_STORE = {
    1: {'title': 'Boyhood',
        'poster_url': 'http://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg',
        'trailer_url': 'https://www.youtube.com/watch?v=IiDztHS3Wos',
        'genre': 'Drama',
        'box_office_earnings': '$25.0M',
        'date_in_theaters': 'Jul 11, 2014'},
    2: {'title': 'The LEGO Movie',
        'poster_url': 'http://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg',
        'trailer_url': 'https://www.youtube.com/watch?v=fZ_JOBCLF-I',
        'genre': 'Kids & Family',
        'box_office_earnings': '$257.8M',
        'date_in_theaters': 'Feb 7, 2014'},
    3: {'title': 'Whiplash',
        'poster_url': 'http://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg',
        'trailer_url': 'https://www.youtube.com/watch?v=aHDEZXoh4-c',
        'genre': 'Drama',
        'box_office_earnings': '$8.7M',
        'date_in_theaters': 'Oct 10, 2014'},
    4: {'title': 'Life Itself',
        'poster_url': 'http://upload.wikimedia.org/wikipedia/en/thumb/d/db/Life_Itself_doc_poster.jpg/220px-Life_Itself_doc_poster.jpg',
        'trailer_url': 'https://www.youtube.com/watch?v=j9ud1HUHgug',
        'genre': 'Documentary',
        'box_office_earnings': '$0.8M',
        'date_in_theaters': 'Jul 4, 2014'},
    5: {'title': 'Gloria',
        'poster_url': 'http://upload.wikimedia.org/wikipedia/en/0/05/Gloria_poster.jpg',
        'trailer_url': 'https://www.youtube.com/watch?v=KO52-rdTX-M',
        'genre': 'Drama',
        'box_office_earnings': '$2.1M',
        'date_in_theaters': 'Jan 24, 2014'}
}


class Movie(object):
    """Represent a movie.

    :param str title: title of the movie
    :param str genre: genre of the movie
    :param str poster_url: URL path to poster image
    :param str trailer_url: URL path to youtube trailer
    :param str box_office: box office earnings of the movie
    :param str release_date: release date in theaters

    """
    def __init__(
            self, title, genre, poster_url,
            trailer_url, box_office, release_date):

        self.title = title
        self.genre = genre

        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

        self.box_office_earnings = box_office
        self.date_in_theaters = release_date


def main():
    """Control "serving" of movies page."""
    movies = []
    for movie in MOVIE_STORE.values():
        movies.append(
            Movie(
                movie['title'],
                movie['genre'],
                movie['poster_url'],
                movie['trailer_url'],
                movie['box_office_earnings'],
                movie['date_in_theaters']))

    movies_sorted_by_title = sorted(movies, key=lambda m: m.title.lower())
    fresh_tomatoes.open_movies_page(movies_sorted_by_title)


if __name__ == '__main__':
    main()
