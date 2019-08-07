"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

longest_num = None
longest_duration = 0
tel_num_duration = {}

for record in calls:
    for i in range(2):
        tel_num = record[i]
        duration = int(record[-1])

        tel_num_duration[tel_num] =  tel_num_duration.get(tel_num, 0) + duration

        if tel_num_duration[tel_num] > longest_duration:
            longest_duration = tel_num_duration[tel_num]
            longest_num = tel_num

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_num, longest_duration))
