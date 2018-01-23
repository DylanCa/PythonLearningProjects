"""
Challenge 177 - Morse Code
https://www.reddit.com/r/dailyprogrammer/comments/2er1v0/8272014_challenge_177_intermediate/

On standard console input, you should enter a phrase of your choosing.
This will then be parsed into morse code and finally outputted as
a valid audio file (WAV, MP3, OGG, as long as it can play it's fine).
In that audio should be an audio translation of your input.

1. Length of a dot : 1 Unit
2. Length of a dash : 3 Units
3. Space between parts of same letter : 1 Unit
4. Space between letters : 3 Units
5. Space between words : 7 Units
"""

import wave
import struct
import math


def write_signal(wavef, duration, volume=0, rate=44100.0,
                 frequency=1240.0):
    """
    rate = 44100.0 Sample rate in Hertz
    duration = 0.1       seconds
    frequency = 1240.0    hertz
    """
    for i in range(int(duration * rate * duration)):

        value = int(volume * math.sin(frequency * math.pi * float(i) / float(rate)))
        data = struct.pack('<h', value)
        wavef.writeframesraw(data)


# S = Short dot - L = Long Dash
morse_alphabet = {"a": ".-",
                  "b": "-...",
                  "c": "-.-.",
                  "d": "-..",
                  "e": ".",
                  "f": "..-.",
                  "g": "--.",
                  "h": "....",
                  "i": "..",
                  "j": ".---",
                  "k": "-.-",
                  "l": "-.--",
                  "m": "--",
                  "n": "-.",
                  "o": "---",
                  "p": ".--.",
                  "q": "--.-",
                  "r": ".-.",
                  "s": "...",
                  "t": "-",
                  "u": "..-",
                  "v": "...-",
                  "w": ".--",
                  "x": "-..-",
                  "y": "-.--",
                  "z": "--..",
                  ".": ".-.-.-",
                  ",": "--..--",
                  "?": "..--..",
                  "/": "-..-.",
                  "@": ".--.-.",
                  "1": ".----",
                  "2": "..---",
                  "3": "...--",
                  "4": "....-",
                  "5": ".....",
                  "6": "-....",
                  "7": "--...",
                  "8": "---..",
                  "9": "----.",
                  "0": "-----"}
char2signal = {'.': 0.3, '-': 0.5}

fname = wave.open("177 - Intermediate/morse.wav", "w")
fname.setparams((1, 2, 44100, 10000, "NONE", "not compressed"))

for word in input("What is your sentence ! ").split():
    for letter in word:
        for char in morse_alphabet[letter.lower()]:
            write_signal(fname, char2signal[char], volume=32767)
            write_signal(fname, 0.3, volume=0)
        write_signal(fname, 0.5, volume=0)
    write_signal(fname, 0.7, volume=0)
fname.close()
