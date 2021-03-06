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


class FBXfoliant(facebook.GraphAPI):

    def __init__(self, fb_at):
        super().__init__(fb_at, version='2.6')
        self.post_data = []

    def get_posts(self):
        try:
            response = self.get_connections('me', 'posts')
            while True:
                yield from response['data']
                response = requests.get(response['paging']['next']).json()
                time.sleep(1)
        except KeyError:
            pass
        except facebook.GraphAPIError:
            raise
