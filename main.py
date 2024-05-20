import pandas as pd
import time as t

# String Constants
FILE_NAME = "input.txt"

# Welcome and Reading File
print("--------------")
print("Welcome to WhatsApp Chat Processor")

f = open(FILE_NAME, "r", encoding="utf-8")
lines = f.readlines()
f.close()

data = []
senders = []
words = {}
start_time = t.time()
instagram_count = 0 

for line in lines:
    date_split_index = line.find(", ")
    if date_split_index == -1:
        continue
    date = line[:date_split_index]

    time_split_index = line[date_split_index:].find("M")
    if time_split_index == - 1 or line.find("M") == - 1:
        continue
    time = line[date_split_index + len(", "): date_split_index + time_split_index - 2]

    am_pm = line[date_split_index + time_split_index - 1: date_split_index + time_split_index + 1]

    sender_split_index = line.find(' - ')
    if line.find(" - ") == - 1:
        continue
    sender = line[sender_split_index + len(' - '):line.find(": ")]
    if sender not in senders:
        senders.append(sender)

    message = line[line.find(": ") + 2:]
    word_list = message.split(" ")
    for word in word_list:
        if word in words and "<" not in word and ">" not in word:
            words[word] += 1
            if "www.instagram" in word:
                instagram_count += 1
        else:
            words[word.strip()] = 1

    data.append({"date": date,
                 "time": time,
                 "am_pm": am_pm,
                 "sender": sender,
                 "message": message
                 })

myDF = pd.DataFrame(data)
end_time = t.time()

if len(senders) == 2:
    print("DM Between", senders[0], "and", senders[1])
else:
    print("GC Among:", ", ".join(senders))

print("--------------")

print(FILE_NAME, "| File Processing Completed in", round((end_time - start_time) * 1000, 3), "milliseconds")
print("Handled", len(myDF), "messages |", myDF["date"][0], "at", myDF["time"][0], myDF["am_pm"][0], "to",
      myDF["date"][len(myDF) - 1], "at", myDF["time"][len(myDF) - 1], myDF["am_pm"][len(myDF) - 1])

sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)

count = 1
w = open("output.txt", "w", encoding="utf-8")
for i in range(len(sorted_words) - 1):
    w.write(str(count) + " | uses: " + str(sorted_words[i][1]) + " | " + sorted_words[i][0] + "\n")
    count += 1

w.close()

print("Instagram Count:", instagram_count)
