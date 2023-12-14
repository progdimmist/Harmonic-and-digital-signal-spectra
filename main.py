import numpy as np
import matplotlib.pyplot as plt


def plot(signal, sampling_rate, i):
    signal_shifted = signal - np.mean(signal)
    spectrum = np.fft.fft(signal_shifted)
    freq = np.fft.fftfreq(len(signal_shifted), 1 / sampling_rate)

    graphic[i, 0].plot(t, signal, color='green')
    graphic[i, 0].set_title('1ГЦ')
    graphic[i, 1].plot(np.abs(spectrum[:51]))
    graphic[i, 1].set_title('Спектр')


def harmonic_signal(freq, duration, sampling_rate):
    time = np.linspace(0, duration, int(sampling_rate * duration))
    signal = np.sin(2 * np.pi * freq * time)
    return time, signal


def digital_signal(freq, duration, sampling_rate):
    time = np.linspace(0, duration, int(sampling_rate * duration))
    signal = np.where(np.sin(2 * np.pi * freq * time) >= 0, 1, 0)
    return time, signal


if __name__ == '__main__':
    sampling_rate = 1000
    duration = 1.0
    frequencies = [1, 2, 4, 8]

    fig, graphic = plt.subplots(4, 2, figsize=(10, 10))
    i = 0

    for freq in frequencies:
        t, square_wave = digital_signal(freq, duration, sampling_rate)
        plot(square_wave, sampling_rate, i)
        i = i + 1

    fig, graphic = plt.subplots(4, 2, figsize=(10, 10))
    i = 0

    for freq in frequencies:
        t, harmonic = harmonic_signal(freq, duration, sampling_rate)
        plot(harmonic, sampling_rate, i)
        i = i + 1
    plt.show()
