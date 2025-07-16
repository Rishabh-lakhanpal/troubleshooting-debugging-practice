#!/usr/bin/env python3
import sys

def usage():
    print("Usage: send_reminders.py '<date>|<title>|<emails>'", file=sys.stderr)

def message_template(date, title):
    return f"Reminder:\n\nMeeting Title: {title}\nDate: {date}\nDon't miss it!"

def send_message(message, emails):
    for email in emails.split(','):
        print(f"Sending to {email.strip()}:\n{message}\n")

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message = message_template(date, title)
        send_message(message, emails)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print(f"Failure to send email: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
