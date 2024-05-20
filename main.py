import pandas as pd
import threading as th
import time as t

# String Constants
WELCOME_MESSAGE = "Welcome to WhatsApp Chat Processor"
LINE_BREAK = "--------------"
FILE_NAME = "input.txt"

# Welcome and Reading File
print(WELCOME_MESSAGE)
print(LINE_BREAK)

f = open(FILE_NAME, "r", encoding="utf-8")
lines = f.readlines()
f.close()

data = []

for line in lines:
    # Processing Each Line
    date_split_index = line.find(", ")
    date = line[:date_split_index]

    time_split_index = line[date_split_index:].find("M")
    time = line[date_split_index + len(", "): date_split_index + time_split_index - 1]

    am_pm = line[date_split_index + time_split_index - 1: date_split_index + time_split_index + 1]

    sender_split_index = line.find(' - ')
    sender = line[sender_split_index + len(' - '):line.find(": ")]

    message = line[line.find(": ") + 2:]

    data.append({"date" : date,
                 "time" : time,
                 "am_pm" : am_pm,
                 ""
                 })