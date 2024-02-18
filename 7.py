import schedule
import time
from datetime import datetime


def print_phrase(phrase, silence_hours):
    start_hour, end_hour = map(int, silence_hours.split('-'))
    print(start_hour, end_hour)
    current_hour = datetime.now().hour
    if start_hour <= current_hour <= end_hour:
        return
    repetitions = 1 + current_hour % 12
    print(phrase * repetitions)


message = input("Введите сообщение для вывода в консоль: ")
silence_hours = input("Введите диапазон времени (часы, когда программа должна молчать) в формате '00-07': ")

schedule.every().hour.at(":29").do(lambda: print_phrase(message, silence_hours))

while True:
    schedule.run_pending()
    time.sleep(1)