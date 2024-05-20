import pandas as pd
import time as t

# String Constants
WELCOME_MESSAGE = "Welcome to WhatsApp Chat Processor"
LINE_BREAK = "--------------"
FILE_NAME = "input.txt"

# Welcome and Reading File
print(LINE_BREAK)
print(WELCOME_MESSAGE)

f = open(FILE_NAME, "r", encoding="utf-8")
lines = f.readlines()
f.close()

data = []
start_time = t.time()

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

    if date_split_index == - 1 or time_split_index == - 1 or sender_split_index == - 1 or line.find(": ") == - 1 or line.find("M") == - 1 or line.find(' - ') == - 1:
        continue

    data.append({"date": date,
                 "time": time,
                 "am_pm": am_pm,
                 "sender": sender,
                 "message": message
                 })


myDF = pd.DataFrame(data)
end_time = t.time()
print("File Processing Completed in", round((end_time - start_time) * 1000, 3), "milliseconds")

senders = []
for user in myDF["sender"]:
    if user not in senders:
        senders.append(user)

