from pynput import keyboard
from plyer import notification
import fasteners
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
                    title="Key Sequence Detected",
                    message="You pressed the correct sequence: " + '-'.join(self.sequence),
                    timeout=10
                )
                os.system('rundll32.exe user32.dll,LockWorkStation')

        except AttributeError:
            self.index = 0

@fasteners.interprocess_locked('/tmp/lockfile')
def run_listener():
    sequence = ['A', 'Z', 'I', 'S']
    detector = KeySequenceDetector(sequence)

    with keyboard.Listener(on_press=detector) as listener:
        listener.join()

if __name__ == "__main__":
    run_listener()