import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow
import queue
from threads.audio_thread import AudioThread
from threads.dsp_thread import DSPThread

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Queues
    audio_q = queue.Queue(maxsize=20)
    result_q = queue.Queue(maxsize=20)

    # Threads
    audio_thread = AudioThread(audio_q)
    dsp_thread = DSPThread(audio_q, result_q)

    audio_thread.start()
    dsp_thread.start()

    # GUI
    window = MainWindow(result_queue=result_q)
    window.show()

    exit_code = app.exec()

    # Stop threads
    audio_thread.stop()
    dsp_thread.stop()

    audio_thread.join()
    dsp_thread.join()

    sys.exit(exit_code)
