"""Render Fresh Tomatoes webpage content."""

import os
import re
import webbrowser

# Styles and scripting for the page
MAIN_PAGE_HEAD = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href='http://fonts.googleapis.com/css?family=Lobster' rel='stylesheet' type='text/css'>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .table-borderless td,
        .table-borderless tr {
            border: 0 !important;
        }
        .font-bold {
            font-weight: bold;
        }
        .movie-title {
            font-family: 'Lobster', cursive;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
MAIN_PAGE_CONTENT = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
MOVIE_TILE_CONTENT = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <h1 class="movie-title">{movie_title}</h1>
    <img src="{poster_image_url}" width="220" height="342">
    <table class="table table-condensed table-borderless">
        <tbody>
            <tr>
                <td><div class="text-right font-bold">Genre:</div></td>
                <td>{movie_genre}</td>
            </tr>
            <tr>
                <td><div class="text-right font-bold">Box Office:</div></td>
                <td>{movie_box_office}</td>
            </tr>
            <tr>
                <td><div class="text-right font-bold">In Theaters:</div></td>
                <td>{movie_theater_date}</td>
            </tr>
        </tbody>
    </table>
</div>
'''


YOUTUBE_URL_RE = re.compile(r'(?<=v=)[^&#]+')
YOUTUBE_SHORTURL_RE = re.compile(r'(?<=be/)[^&#]+')


def create_movie_tiles_content(movies):
    """Create movie tiles for the Fresh Tomatoes webpage.

    :param list movies: a list of movie_trailer_website.Movie objects
    :returns: HTML content for Fresh Tomatoes main page
    :rtype: str

    """
    html_content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(YOUTUBE_URL_RE, movie.trailer_youtube_url)

        youtube_id_match = (
            youtube_id_match or
            re.search(YOUTUBE_SHORTURL_RE, movie.trailer_youtube_url))

        trailer_youtube_id = (
            youtube_id_match.group(0) if youtube_id_match else None)

        # Append the tile for the movie with its content filled in
        html_content += MOVIE_TILE_CONTENT.format(
            movie_title=movie.title,
            movie_genre=movie.genre,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_box_office=movie.box_office_earnings,
            movie_theater_date=movie.date_in_theaters
        )
    return html_content


def open_movies_page(movies):
    """Open Fresh Tomatoes movies webpage.

    :param list movies: a list of movie_trailer_website.Movie objects
    :returns: None

    """
    with open('fresh_tomatoes.html', 'w') as output_file:
        # Replace the placeholder for the movie tiles with the actual
        # dynamically generated content
        rendered_content = MAIN_PAGE_CONTENT.format(
            movie_tiles=create_movie_tiles_content(movies))

        output_file.write(MAIN_PAGE_HEAD + rendered_content)

    local_url = ''.join(['file://', os.path.abspath(output_file.name)])
    webbrowser.open_new_tab(local_url)
