import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import logging
import os
import threading
import time
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
class trading_bot(threading.Thread):
    def __init__(self):
        super(trading_bot, self).__init__()
        self.is_trading = False
        mt5.initialize()
        self._login()

    def _get_account_info(self):
        pass

    def _login(self):
        account_info =  mt5.account_info()
        if account_info == None: #Need to login again
            #authorized = mt5.login(25115284, password="gqz0343lbdm")
            account_info =  mt5.account_info()
            if account_info == None:
                raise Exception
                os.kill()
        else:
            self.is_trading = True
            logging.info("Login Success")
            self.account_info = mt5.account_info()._asdict()
            #print(self.account_info)
            symbols = mt5.symbols_total()
            #group_symbols = mt5.symbols_get(group="*USD*")._asdict() #*,!*USD*,!*EUR*,!*JPY*,!*GBP*
            #print(group_symbols)
            #df = pd.DataFrame(group_symbols)
            #print(df)
            while True:
                ticker = mt5.symbol_info_tick("USDJPY")._asdict()
                print(ticker)
                time.sleep(1)