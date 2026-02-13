import threading
import time
from dsp.fft_processor import FFTProcessor
from dsp.dtmf_decoder import DTMFDecoder
import queue

from utils.config import TOLERANCE , FMAX, N, Fe

class DSPThread(threading.Thread):
    def __init__(self, audio_queue, result_queue):
        super().__init__()
        self.audio_queue = audio_queue
        self.result_queue = result_queue
        self.fft = FFTProcessor(fmax=FMAX, block_size=N, sample_rate=Fe)
        self.decoder = DTMFDecoder(TOLERANCE)
        self.running = True

    def run(self):
        while self.running:
            try:
                block = self.audio_queue.get(timeout=0.1)
                freqs, spectrum = self.fft.compute_fft(block)
                key = self.decoder.decode(freqs, spectrum)
                self.result_queue.put((block, freqs, spectrum, key))
            except queue.Empty:
                continue

    def stop(self):
        self.running = False
        
    def is_running(self):
        return self.running
    def set_running(self, state):
        self.running = state
