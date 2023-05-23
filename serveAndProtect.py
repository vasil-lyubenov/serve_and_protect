from pynput import keyboard
from plyer import notification
import os

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
                    title="Serve And Protect Activated!",
                    message="BEZSRAMNIK! You pressed the sequence: " + '-'.join(self.sequence),
                    timeout=10
                )
                os.system('rundll32.exe user32.dll,LockWorkStation')

        except AttributeError:
            self.index = 0

sequence = ['A', 'Z', 'I', 'S']
detector = KeySequenceDetector(sequence)

with keyboard.Listener(on_press=detector) as listener:
    listener.join()



