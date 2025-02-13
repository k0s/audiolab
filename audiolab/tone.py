"""
Generate a tone (sine wave) at a given frequency.
"""

import argparse
import numpy as np
import struct
import wave


class Tone:
    """
    Sine tone
    """

    def __init__(self, frequency: float):
        self.frequency = frequency
        # self.offset = TODO : offset phase

    def generate(self, t: np.ndarray) -> np.ndarray:
        """
        Generate a tone (sine wave) at a given frequency.
        """
        return np.sin(2 * np.pi * self.frequency * t)
    __call__ = generate


def writewav(output: str, amplitude: np.ndarray, frame_rate: int, sample_width=2):
    """
    Write a wave file from a discrete array
    """

    # Variables for this wave file
    num_channels = 1  # TODO: compute from PCM
    num_frames = 0
    comp_type = "NONE"
    comp_name = "not compressed"

    with wave.open(output, 'wb') as wav_file:
        wav_file.setparams((num_channels, sample_width, frame_rate, num_frames, comp_type, comp_name))
        for sample in amplitude:
            wav_file.writeframes(struct.pack('h', sample))    


def main():
    """CLI"""

    # Parse command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--frequency", type=float, default=440.)
    parser.add_argument("--duration", type=float, default=5.)
    parser.add_argument("--sample-rate", type=int, default=44100)
    parser.add_argument("-o", "--output", type=str, required=True)
    options = parser.parse_args()

    # Compute the PCM amplitude
    time = np.linspace(0, options.duration, int(options.sample_rate * options.duration), False)
    tone = Tone(options.frequency)
    amplitude = np.int16(32767*tone(time))

    # Write the wave file
    writewav(options.output, amplitude, options.sample_rate)
