"""
1 character per tweet
"""
import sys
import time

from tweetnet import Tweetnet
from botmaster import SingleCharBotMaster

TYPES = {
    'SingleCharBotMaster': SingleCharBotMaster,
}

if __name__ == "__main__":
    round_id = sys.argv[1]
    user = sys.argv[2]
    botmaster_type = sys.argv[3]
    api = Tweetnet(round_id, role='admin')

    master = TYPES[botmaster_type](user, api)

    last_check = 0

    while True:
        print "Checking for new flags..."
        flags = api.get_flags(since=last_check)
        last_check = int(time.time()) - 1
        if flags:
            for flag in flags:
                flag_id = flag['flag_id']
                print "Submitting flag %s" % flag_id
                master.submit_flag(flag_id)
        time.sleep(3)
