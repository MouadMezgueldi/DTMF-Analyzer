import threading
import numpy as np
from audio.audio_stream import AudioStream

import queue
import time

class AudioThread(threading.Thread):
    def __init__(self, audio_queue):
        super().__init__()
        self.audio_queue = audio_queue
        self.audio = AudioStream()
        self.running = True

    def run(self):
        self.audio.start()
        while self.running:
            block = self.audio.get_audio_block()
            if block is not None:
                try:
                    self.audio_queue.put_nowait(block)
                except queue.Full:
                    pass
            else:
                time.sleep(0.0001)

    def stop(self):
        self.running = False
        self.audio.stop()
    def is_running(self):
        return self.running
    def set_running(self, state):
        self.running = state
