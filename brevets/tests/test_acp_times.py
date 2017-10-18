from acp_times import *

import nose
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

brevet_start_time = "2017-01-0100:00"
brevet_dist_kms = [200, 400, 600, 1000]
control_dist_km = [0, 100, 200, 400, 600, 1000]
