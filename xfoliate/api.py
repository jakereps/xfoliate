# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the MIT License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import facebook

from .fb import Profile

FB_GRAPH = None


def run():
    global FB_GRAPH

    print(__initial_message)
    fb_at = input('>> ')

    FB_GRAPH = facebook.GraphAPI(fb_at, version='2.6')
    for post in Profile.scrape_posts(FB_GRAPH):
        print(post)


__initial_message = """
    Welcome to xfoliate! To get started grab a Facebook access token from:
        https://developers.facebook.com/tools/explorer
    Click 'Get Token' > 'Get User Access Token'
    In the top right change the API version number to 2.6
    You can deselect everything but 'user_posts' for permissions

    Copy and paste the access token below:
"""
