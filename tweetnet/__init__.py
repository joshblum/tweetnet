"""
API that we can develop behind
"""

from tweetnet import BaseTweetnet
from twitter_mixins import *
from realistic_mixins import *
from flags_mixins import *


class Tweetnet(MockTwitterMixin, ConstantRealisticMixin, WebappFlagsMixin, BaseTweetnet):
    pass

