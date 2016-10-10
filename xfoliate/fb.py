# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the MIT License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import time

import facebook
import requests


class Profile:

    @staticmethod
    def scrape_posts(FB_GRAPH):
        try:
            response = FB_GRAPH.get_connections('me', 'posts')
            while True:
                time.sleep(2)
                if response is not None:
                    for post in response['data']:
                        if 'message' in post:
                            data = 'https://facebook.com/%s: %s' % \
                                   (post['id'], post['message'])
                            yield data
                response = requests.get(response['paging']['next']).json()
        except KeyError:
            pass
        except facebook.GraphAPIError as e:
            raise


__invalid_fb_at = 'The access token supplied was invalid. Please try again, '\
                  'and make sure to follow the above steps! (v2.6 GraphAPI!!)'
