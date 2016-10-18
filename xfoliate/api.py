# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the MIT License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os

import click
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from .fb import FacebookHandler


__initial_message = """
    Welcome to xfoliate! To get started grab a Facebook access token from:
        https://developers.facebook.com/tools/explorer
    Click 'Get Token' > 'Get User Access Token'
    In the top right change the API version number to 2.6
    You can deselect everything but 'user_posts' for permissions

    Copy and paste the access token below:
"""


@click.command()
def run():
    nltk_dl_dir = nltk.downloader.Downloader()._download_dir
    vader_path = os.path.join(nltk_dl_dir, 'sentiment', 'vader_lexicon.zip')
    if not os.path.exists(vader_path):
        nltk.download('vader_lexicon')

    sia = SentimentIntensityAnalyzer()
    fb_at = click.prompt(__initial_message, type=str, prompt_suffix='>> ')

    for post in FacebookHandler(fb_at).get_posts():
        try:
            ps = sia.polarity_scores(post['message'])
            click.echo('%s:\n%s\n' % (post['message'], ps))
        except KeyError:
            pass
