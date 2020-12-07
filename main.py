import logging
import sys
import datetime

from app.models.candle import UsJpyBaseCandle1M
import settings

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == "__main__":
    import app.models

    now1 = datetime.datetime(2020, 1, 2, 3, 4, 5)
    UsJpyBaseCandle1M.create(now1, 1.0, 2.0, 3.0, 4.0, 5)
    candle = UsJpyBaseCandle1M.get(now1)
    print(candle.time)
    print(candle.open)
    candle.open = 100.0
    candle.save()

    updated_candle = UsJpyBaseCandle1M.get(now1)
    print(updated_candle.open)


