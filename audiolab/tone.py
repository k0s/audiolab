"""
Generate a tone (sine wave) at a given frequency.
"""

import argparse
import numpy as np
import struct
import wave


class Tone:
    def __init__(self, frequency: float):
        self.frequency = frequency

    def generate(self) -> np.ndarray:
        """
        Generate a tone (sine wave) at a given frequency.
        """
        raise NotImplementedError("TODO")
        # return np.sin(2 * np.pi * self.frequency * t)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--frequency", type=float, default=440.)
    parser.add_argument("--duration", type=float, default=2.)
    parser.add_argument("--sample-rate", type=int, default=44100)
    parser.add_argument("-o", "--output", type=str, required=True)
    options = parser.parse_args()

    num_channels = 1
    sample_width = 2
    frame_rate = options.sample_rate
    num_frames = 0
    comp_type = "NONE"
    comp_name = "not compressed"

    with wave.open(options.output, 'wb') as wav_file:
        wav_file.setparams((num_channels, sample_width, frame_rate, num_frames, comp_type, comp_name))
    #tone = Tone(args.frequency)
    #tone.generate()

        duration = 5
        frequency = 440
        time = np.linspace(0, duration, int(frame_rate * duration), False)
        amplitude = np.int16(32767 * np.sin(2 * np.pi * frequency * time))

        for sample in amplitude:
            wav_file.writeframes(struct.pack('h', sample))