"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""



both_fixed_bgl = 0 # the count of fixed phone numbers from both calling and answering of Bangalore
from_bgl = 0 # the count of fixed phone numbers calling from Bangalore
phone_list = set() # store phone numbers called by people in Bangalore

for record in calls:
    if record[0].find("(080)") != -1 and record[1].find("(080)") != -1:
        both_fixed_bgl += 1
        from_bgl += 1
        phone_list.add(record[1])
    elif record[0].find("(080)") != -1 and record[1].find(")") != -1:
        from_bgl += 1
        phone_list.add(record[1])
    elif record[0].find("(080)") != -1 and (record[1][0] == "7" or record[1][0] == "8" or record[1][0] == "9"):
        from_bgl += 1
        phone_list.add(record[1])

print("The numbers called by people in Bangalore have codes:")

codes = set() # store special codes from area codes and mobile phone numbers

for phone in phone_list:
    if phone.find(")") != -1: # locate area code length
        place = phone.find(")")
        codes.add(phone[:place+1])
    else:
        codes.add(phone[:4]) # first four digits from mobile phone numbers

for code in sorted(codes):
    print(code)

perc = round((both_fixed_bgl / from_bgl * 100), 2) # keep only 2 decimal digits
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(str(perc)))

    
