# app_DTMF — Real-time DTMF Decoder (Python)

A lightweight Python application for decoding DTMF (Dual-Tone Multi-Frequency) tones from audio input. The project includes real-time audio capture, FFT-based signal processing, a DTMF detection module, threading for concurrent audio/DSP processing, and a simple GUI to visualize and control the decoder.

## Key Features
- Real-time audio capture and buffering (`audio/audio_stream.py`).
- FFT-based frequency analysis (`dsp/fft_processor.py`).
- DTMF tone detection and decoding (`dsp/dtmf_decoder.py`).
- Threaded architecture separating audio I/O and DSP (`threads/`).
- Minimal GUI for monitoring and interaction (`gui/main_window.py`).
- Configuration and helper utilities (`utils/config.py`).

## Repository Layout

- `main.py` — Application entry point (starts GUI or CLI runner).
- `test.py` — Quick test harness and examples for running decoder logic.
- `requirements.txt` — Python dependencies.
- `audio/` — Audio I/O and streaming helpers.
  - `audio_stream.py` — Captures audio from the default device and exposes frames/buffers.
- `dsp/` — Digital signal processing and DTMF decoding.
  - `fft_processor.py` — Lightweight FFT wrapper and windowing utilities.
  - `dtmf_decoder.py` — Implements the DTMF detection algorithm and mapping of frequency pairs to keys.
- `gui/` — GUI components and windows.
  - `main_window.py` — Simple PyQt-based window to start/stop capture and display detected keys.
- `threads/` — Threaded workers for audio capture and DSP pipeline.
  - `audio_thread.py` — Runs audio capture in a background thread.
  - `dsp_thread.py` — Processes audio frames and runs the decoder concurrently.
- `utils/` — Configuration and small helpers.
  - `config.py` — Central configuration (sample rates, block sizes, thresholds).
- `dtmf_env/` — Optional included virtual environment (useful for offline setups on Windows).

## Installation (Windows)

A prebuilt virtual environment exists in `dtmf_env/` (Windows). You can use it, or create a fresh virtualenv and install dependencies.

To use the included environment (PowerShell):

```powershell
# Activate prebuilt venv (PowerShell)
.\dtmf_env\Scripts\Activate.ps1
# or cmd:
.\dtmf_env\Scripts\activate.bat
```

To create and use a fresh virtual environment (recommended):

```powershell
# create venv
python -m venv .venv
# activate
.\.venv\Scripts\Activate.ps1
# install deps
pip install -r requirements.txt
```

Note: This project uses audio libraries (e.g. `sounddevice`, `PyAudio`, `numpy`, `scipy`). On Windows, installing wheels or using the included `dtmf_env` can avoid build-tool issues.

## Usage

Run the GUI (if PyQt is available):

```powershell
python main.py
```

Run the CLI/test harness to decode from the default audio device or from a recorded file:

```powershell
python test.py
```

Common runtime caveats:
- Ensure your microphone or line-in is available and set as default input.
- If you see permission errors on Windows, run PowerShell as Administrator or check microphone privacy settings.

## How it works (high level)

1. `audio/audio_stream.py` captures audio frames in a callback and queues them for processing.
2. `threads/audio_thread.py` and `threads/dsp_thread.py` separate I/O from CPU-bound DSP work.
3. `dsp/fft_processor.py` performs windowing and FFT to produce a frequency magnitude spectrum.
4. `dsp/dtmf_decoder.py` inspects spectral peaks around the DTMF row/column frequencies and decides which key (if any) is present, producing a timestamped event.
5. The GUI or the test harness subscribes to decoded events and displays/logs them.

## Configuration

Edit `utils/config.py` to adjust:
- `SAMPLE_RATE` — audio sampling rate.
- `BLOCK_SIZE` — audio frame size for FFT.
- `DTMF_THRESHOLD` — detection threshold for spectral peaks.

## Development and Testing

- Run `python -m pip install -r requirements.txt` in an activated venv.
- Use `test.py` to validate detection with simulated audio or file inputs.
- Add unit tests that import `dsp.dtmf_decoder` and feed synthetic tones to verify mapping accuracy.

## Troubleshooting
- No sound / no device: verify OS audio settings and that `sounddevice` or `pyaudio` can list devices.
- Incorrect detections: adjust `DTMF_THRESHOLD` and `BLOCK_SIZE` in `utils/config.py`.
- GUI not starting: ensure `PyQt6` (or the GUI backend used) is installed.

## Notes
- This project aims to be a compact reference implementation for learning DTMF decoding and real-time DSP in Python; it is not hardened for production telephony systems.
- The repository includes a local `dtmf_env/` for convenience on Windows; you can remove it and use a per-project venv.

## Next steps
- Add automated unit tests for `dsp/dtmf_decoder.py`.
- Add an option to read audio from WAV files for offline analysis.

---

If you want, I can also: update `requirements.txt` from `dtmf_env`, add example WAV test vectors, or create unit tests for `dsp/dtmf_decoder.py`.
Parfait ! 😄 Voici **tout le contenu que tu peux copier directement dans ton `README.md`**. Tu n’as plus qu’à créer le fichier et coller ceci :

````markdown
# app_DTMF — Real-time DTMF Decoder (Python)

A lightweight Python application for decoding DTMF (Dual-Tone Multi-Frequency) tones from audio input. The project includes real-time audio capture, FFT-based signal processing, a DTMF detection module, threading for concurrent audio/DSP processing, a simple GUI to visualize and control the decoder, and an HTML-based simulator for testing DTMF input.

## Key Features
- Real-time audio capture and buffering (`audio/audio_stream.py`).
- FFT-based frequency analysis (`dsp/fft_processor.py`).
- DTMF tone detection and decoding (`dsp/dtmf_decoder.py`).
- Threaded architecture separating audio I/O and DSP (`threads/`).
- Minimal GUI for monitoring and interaction (`gui/main_window.py`).
- Configuration and helper utilities (`utils/config.py`).
- **HTML simulator (`index.html`)** to generate DTMF tones with virtual keys or your own phone.
- MATLAB version of the DTMF decoding algorithm included (`matlab/`).

## Repository Layout

- `main.py` — Application entry point (starts GUI or CLI runner).
- `test.py` — Quick test harness and examples for running decoder logic.
- `requirements.txt` — Python dependencies.
- `index.html` — Browser-based DTMF simulator (click keys or use your phone to send tones).
- `audio/` — Audio I/O and streaming helpers.
  - `audio_stream.py` — Captures audio from the default device and exposes frames/buffers.
- `dsp/` — Digital signal processing and DTMF decoding.
  - `fft_processor.py` — Lightweight FFT wrapper and windowing utilities.
  - `dtmf_decoder.py` — Implements the DTMF detection algorithm and mapping of frequency pairs to keys.
- `gui/` — GUI components and windows.
  - `main_window.py` — Simple PyQt-based window to start/stop capture and display detected keys.
- `threads/` — Threaded workers for audio capture and DSP pipeline.
  - `audio_thread.py` — Runs audio capture in a background thread.
  - `dsp_thread.py` — Processes audio frames and runs the decoder concurrently.
- `utils/` — Configuration and small helpers.
  - `config.py` — Central configuration (sample rates, block sizes, thresholds).
- `matlab/` — MATLAB version of the DTMF decoder for reference and testing.
- `dtmf_env/` — Optional included virtual environment (useful for offline setups on Windows).

## Installation (Windows)

A prebuilt virtual environment exists in `dtmf_env/` (Windows). You can use it, or create a fresh virtualenv and install dependencies.

To use the included environment (PowerShell):

```powershell
# Activate prebuilt venv (PowerShell)
.\dtmf_env\Scripts\Activate.ps1
# or cmd:
.\dtmf_env\Scripts\activate.bat
````

To create and use a fresh virtual environment (recommended):

```powershell
# create venv
python -m venv .venv
# activate
.\.venv\Scripts\Activate.ps1
# install deps
pip install -r requirements.txt
```

On Linux/Ubuntu:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
sudo apt install portaudio19-dev
```

> Note: This project uses audio libraries (e.g. `sounddevice`, `PyAudio`, `numpy`, `scipy`). On Windows, installing wheels or using the included `dtmf_env` can avoid build-tool issues.

---

## Usage

Run the GUI (if PyQt is available):

```bash
python main.py
```

Run the CLI/test harness to decode from the default audio device or from a recorded file:

```bash
python test.py
```

Use the HTML simulator:

1. Open `index.html` in a web browser.
2. Click the virtual keys or use your phone to generate DTMF tones.
3. The Python application can detect and display these tones in real-time.

Common runtime caveats:

* Ensure your microphone or line-in is available and set as default input.
* If you see permission errors on Windows, run PowerShell as Administrator or check microphone privacy settings.

---

## How it works (high level)

1. `audio/audio_stream.py` captures audio frames in a callback and queues them for processing.
2. `threads/audio_thread.py` and `threads/dsp_thread.py` separate I/O from CPU-bound DSP work.
3. `dsp/fft_processor.py` performs windowing and FFT to produce a frequency magnitude spectrum.
4. `dsp/dtmf_decoder.py` inspects spectral peaks around the DTMF row/column frequencies and decides which key (if any) is present, producing a timestamped event.
5. The GUI, HTML simulator, or the test harness subscribes to decoded events and displays/logs them.

---

## Configuration

Edit `utils/config.py` to adjust:

* `SAMPLE_RATE` — audio sampling rate.
* `BLOCK_SIZE` — audio frame size for FFT.
* `DTMF_THRESHOLD` — detection threshold for spectral peaks.

---

## MATLAB Version

* The `matlab/` folder contains a version of the DTMF decoding algorithm implemented in MATLAB.
* Useful for educational purposes or comparing Python and MATLAB results.
* Can generate plots of FFT spectra and DTMF detection visually.

---

## Development and Testing

* Run `python -m pip install -r requirements.txt` in an activated venv.
* Use `test.py` to validate detection with simulated audio or file inputs.
* Add unit tests that import `dsp.dtmf_decoder` and feed synthetic tones to verify mapping accuracy.

---

## Troubleshooting

* No sound / no device: verify OS audio settings and that `sounddevice` or `pyaudio` can list devices.
* Incorrect detections: adjust `DTMF_THRESHOLD` and `BLOCK_SIZE` in `utils/config.py`.
* GUI not starting: ensure `PyQt6` (or the GUI backend used) is installed.

---

## Notes

* This project is intended as a compact reference for learning DTMF decoding and real-time DSP in Python.
* HTML simulator (`index.html`) allows quick testing without needing a phone.
* MATLAB version included for comparison and educational purposes.
* Repository includes a local `dtmf_env/` for convenience on Windows; you can remove it and use a per-project venv.

---


