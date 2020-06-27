import os.path
import sys
import random
import smtplib
from email.mime.text import MIMEText

#Checking if the text file exists
if not os.path.exists("jokes.txt"):
    sys.exit("No jokes.txt found")

#Reading the text file
txt_file = open("jokes.txt", "r")

#Counting the number of lines in the file
lines_number = len(open("jokes.txt").readlines(  ))
if lines_number == 0:
    sys.exit("File jokes.txt is empty")

#Reading the random line
random_line = random.randrange(0, lines_number)
all_lines = txt_file.readlines()
chosen_joke = all_lines[random_line - 1]
txt_file.close()

#Sending the line via email. Use your data here (be aware that email providers might block outgoing mail as spam).
print("Sending Email...")
msg = MIMEText("This is automatically sent message.")
msg['Subject'] = chosen_joke
msg['From'] = 'YourName <you@email.com>'
msg['To'] = 'FriendsName <friend@email.net>'

#From, To, and SMTP credentials
sender = 'you@email.com'
receiver = 'friend@email.net'
login = 'smtp_email_login' #your login
password = 'smtp_email_password' #your password

#Sending it. If it doesn't work try "smtplib.SMTP" instead of "smtplib.SMTP_SSL"
with smtplib.SMTP_SSL('smtp.server.com', port) as server: #port is usually 465
    server.login(login, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("Mail sent")
