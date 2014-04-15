"""
API that we can develop behind
"""

from tweetnet import BaseTweetnet
from twitter_mixins import *
from realistic_mixins import *
from submission_mixins import *


class Tweetnet(JankyTwitterMixin, ConstantRealisticMixin, WebappSubmissionMixin, BaseTweetnet):
    pass

