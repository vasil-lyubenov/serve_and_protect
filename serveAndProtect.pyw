import configparser
import os
import yagmail
from pynput import keyboard
from plyer import notification

class KeySequenceDetector:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __call__(self, key):
        try:
            if key.char.upper() == self.sequence[self.index]:
                self.index += 1
            else:
                self.index = 0

            if self.index == len(self.sequence):
                self.index = 0
                print('Sequence entered. Sending notification...')
                notification.notify(
                    title="Key Sequence Detected",
                    message="You pressed the correct sequence: " + '-'.join(self.sequence),
                    timeout=10
                )
                os.system('rundll32.exe user32.dll,LockWorkStation')

                # Send email notification
                send_email_notification()

        except AttributeError:
            self.index = 0


def send_email_notification():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Check if EMAIL and GMAIL sections exist in the config file
    if 'EMAIL' in config and 'GMAIL' in config:
        email_address = config['EMAIL']['address']
        gmail_address = config['GMAIL']['address']
        gmail_password = config['GMAIL']['password']

        # Sending email
        yag = yagmail.SMTP(gmail_address, gmail_password)
        yag.send(
            to=email_address,
            subject="Banned Key Sequence Detected!",
            contents="You pressed the following banned sequence: " + '-'.join(sequence),
        )
    else:
        print('Required sections or fields are missing in config.ini')


sequence = ['A', 'Z', 'I', 'S']
detector = KeySequenceDetector(sequence)

with keyboard.Listener(on_press=detector) as listener:
    listener.join()
