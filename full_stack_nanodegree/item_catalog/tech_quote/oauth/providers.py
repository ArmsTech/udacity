"""OAuth sign in services for supported providers."""

import os

from rauth.service import OAuth2Service


class GitHubSignIn(object):

    """A GitHub OAuth2 sign in."""

    def __init__(self):
        """Initialize a new GitHubSignIn instance."""
        self.service = OAuth2Service(
            client_id=os.environ['GITHUB_ID'],
            client_secret=os.environ['GITHUB_SECRET'],
            name='github',
            authorize_url='https://github.com/login/oauth/authorize',
            access_token_url='https://github.com/login/oauth/access_token',
            base_url='https://api.github.com/')
