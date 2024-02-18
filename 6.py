import time
from datetime import datetime

import schedule


def print_phrase(phrase):
    current_hour = datetime.now().hour
    repetitions = 1 + current_hour % 12
    print(phrase * repetitions)


schedule.every(1).hour.at(":07").do(lambda: print_phrase("Ку"))

while True:
    schedule.run_pending()
    time.sleep(1)