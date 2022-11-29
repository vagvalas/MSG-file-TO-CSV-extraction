import os
import extract_msg
import csv

with open(r'Data.csv', mode='w') as file:
    writer = csv.writer(file)

    msgdata = []

    for f in os.listdir('.'):
        if not f.endswith('.msg'):
            continue

        msg = extract_msg.Message(f)
        msg_sender = msg.sender
        msg_date = msg.date
        msg_subj = msg.subject
        msg_message = msg.body
        msgdata = msg_message.split()
        writer.writerow(msgdata)