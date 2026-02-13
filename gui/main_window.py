import numpy as np
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer,Qt
import pyqtgraph as pg
import pyttsx3
import threading

from dsp.fft_processor import FFTProcessor
from dsp.dtmf_decoder import DTMFDecoder
from utils.config import N, Fe


class MainWindow(QMainWindow):

    def __init__(self, result_queue=None): 
        super().__init__()
        self.engine = pyttsx3.init()
        self.setWindowTitle("DTMF Analyzer")

        self.result_queue = result_queue   

        # UI Layout
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        # Label DTMF
        self.label = QLabel("DTMF: ---")
        self.label.setStyleSheet("font-size: 30px;")
        layout.addWidget(self.label)

        # Plot Time
        self.plot_time = pg.PlotWidget(title="Signal Temporel")
        layout.addWidget(self.plot_time)

        # Plot FFT
        self.plot_fft = pg.PlotWidget(title="Spectre FFT")
        layout.addWidget(self.plot_fft)

        # Courbes
        self.curve_time = self.plot_time.plot(pen='y')
        self.curve_fft = self.plot_fft.plot(pen='c')

        # Axes
        self.plot_time.setYRange(-0.2, 0.2)
        self.plot_fft.setXRange(0, 2000)

        # Timer update
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_loop)
        self.timer.start(30)  # ms
    # Update Loop
    def update_loop(self):
        if self.result_queue is None:
            return

        try:
            block, freqs, spectrum, key = self.result_queue.get_nowait()
        except Exception:
            return

        # Update DTMF label
        if key is not None:
            self.label.setText(f"DTMF: {key}")
            self.speak_text(key)

        # Update plots
        t = np.arange(len(block)) /Fe
        mask = freqs > 0
        f_pos = freqs[mask]
        s_pos = spectrum[mask]

        self.curve_time.setData(t, block)
        self.curve_fft.setData(f_pos, s_pos)
    def speak_text(self, text):
     threading.Thread(target=lambda: self.engine.say(text) or self.engine.runAndWait(), daemon=True).start()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape: 
            self.close()
        elif event.key() == Qt.Key.Key_Q:    
            self.close()
        else:
            super().keyPressEvent(event)