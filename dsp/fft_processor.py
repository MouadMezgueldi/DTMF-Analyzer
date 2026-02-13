import numpy as np


class FFTProcessor:

    def __init__(self,
                 sample_rate=44100,
                 block_size=4096,
                 fmax=2000):

        self.sample_rate = sample_rate
        self.block_size = block_size
        self.fmax = fmax

        self.freqs = np.fft.fftshift(
            np.fft.fftfreq(block_size, 1/sample_rate)
        )

        self.window = np.hamming(block_size)

        self.filter_mask = np.abs(self.freqs) < fmax # low pass filter


    def compute_fft(self, signal):

        
        signal_windowed = signal * self.window

       
        S = np.fft.fftshift(np.fft.fft(signal_windowed) / self.block_size)
        
        # Amplitude
        A = np.abs(S)

        # Application du filtre passe-bas
        A_filtered = A * self.filter_mask

        return self.freqs, A_filtered