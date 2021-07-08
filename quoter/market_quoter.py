import pandas as pd
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import threading
import time
import schedule
class market_quoter(threading.Thread):
    def __init__(self):
        super(market_quoter, self).__init__()
