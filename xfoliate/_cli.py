# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the MIT License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import click
# from tqdm import tqdm

# from .fb import FBXfoliant
# from .sentiment import SIA

__initial_message = """
    Welcome to xfoliate! To get started grab a Facebook access token from:
        https://developers.facebook.com/tools/explorer
    Click 'Get Token' > 'Get User Access Token'
    You can deselect everything but 'user_posts' for permissions

    Copy and paste the access token below:
"""


class CommandLine(click.MultiCommand):

    def list_commands(self, ctx):
        return ['TODO']

    def get_command(self, ctx, name):
        return click.Command('TODO')


@click.command(cls=CommandLine)
def cli():
    pass
