# audiolab
experiments in audio

## Overview

This repo is a collection of experiments in audio.
While I will start in Python, I will try to port to C++, Rust, and Haskell going forward.

The basic idea is to develop a signal path chain that can be used to generate and process audio.

For example, here's a simple signal path chain that generates a sine wave and applies a low-pass filter to it:

```
sine_wave = SineWave(frequency=440)
low_pass_filter = LowPassFilter(cutoff_frequency=1000)
audio_signal = sine_wave.process()
filtered_signal = low_pass_filter.process(audio_signal)

# Write the filtered signal to a WAV file
import scipy.io.wavfile as wavfile
sample_rate = 44100  # Standard audio sample rate
wavfile.write('output.wav', sample_rate, filtered_signal)
```

## Goals

- [x] Simple Sine Wave:  given a frequency (tone), generate a sine wave
- [ ] FFT: given a WAV file, what is the fundamental frequency? Use this as a test to validate tone generation (see https://numpy.org/doc/stable/reference/generated/numpy.fft.fftfreq.html and perhaps https://stackoverflow.com/questions/57251454/how-to-find-the-fundamental-frequency-of-a-wav-file )
- [ ] FM Synthesis: https://www.javelinart.com/FM_Synthesis_of_Real_Instruments.pdf

## Installation

Ensure you have Python 3.9 or higher installed.

```
# python --version
Python 3.9.21
```

Make a virtual environment and install the dependencies.

```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -e .
```

## Run the tests.

> TODO: Add `tox` to run the tests.

Ensure you have the dev dependencies installed.

```
pip install -e .[dev]
```

Run the tests.

```
pytest
```


