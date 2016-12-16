# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Jorden Kreps.
#
# Distributed under the terms of the MIT License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

NLTK_DL_DIR = nltk.downloader.Downloader()._download_dir
VADER_PATH = os.path.join(NLTK_DL_DIR, 'sentiment', 'vader_lexicon.zip')
if not os.path.exists(VADER_PATH):
    nltk.download('vader_lexicon')

SIA = SentimentIntensityAnalyzer()
