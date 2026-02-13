import sounddevice as sd
import numpy as np
import queue


class AudioStream:
    def __init__(self,
                 sample_rate=44100,
                 block_size=4096,
                 channels=1):

        self.sample_rate = sample_rate
        self.block_size = block_size
        self.channels = channels

        self.audio_queue = queue.Queue(maxsize=20)

        self.stream = None


  
    def _audio_callback(self, indata, frames, time, status):

        if status:
            print(status)

        # copie pour éviter overwrite mémoire
        signal = indata[:, 0].copy()

        try:
            self.audio_queue.put_nowait(signal)
        except queue.Full:
            # si queue pleine → on drop (temps réel prioritaire)
            pass


    # Start Stream
    def start(self):

        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            blocksize=self.block_size,
            channels=self.channels,
            callback=self._audio_callback
        )

        self.stream.start()


    # Stop Stream
    def stop(self):

        if self.stream:
            self.stream.stop()
            self.stream.close()


    # Get Audio Block
    def get_audio_block(self):

        try:
            return self.audio_queue.get_nowait()
        except queue.Empty:
            return None
