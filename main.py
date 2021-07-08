import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import logging
from trading_bot.bot import trading_bot
if __name__ == '__main__':
    print("Init the MT5 trading bot")
    bot = trading_bot()


