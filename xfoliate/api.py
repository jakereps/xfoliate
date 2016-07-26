# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the MIT License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import facebook

FB_GRAPH = None


def run(fb_at):
    global FB_GRAPH
    response = None
    try:
        FB_GRAPH = facebook.GraphAPI(fb_at, version='2.6')
        # apparently .GraphAPI doesn't validate anything, so moving this here
        # in order to get an exception raised if the access token is invalid
        response = FB_GRAPH.get_connections('me', 'posts')
    except facebook.GraphAPIError:
        raise ValueError(__invalid_fb_at) from None

    if response is not None:
        for post in response['data']:
            if 'message' in post:
                print('https://facebook.com/%s: %s' %
                      (post['id'], post['message']))


__invalid_fb_at = 'The access token supplied was invalid. Please try again, '\
                  'and make sure to follow the above steps! (v2.6 GraphAPI!!)'
