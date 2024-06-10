import librosa
import  os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def plot_waveform_with_peak(file_path,filename,username):
    # Load audio file
    y, sr = librosa.load(file_path)

    # Calculate time array
    t = np.arange(0, len(y)) / sr

    # Find peak value and its index
    peak_value = np.max(np.abs(y))
    peak_index = np.argmax(np.abs(y))

    # Plot waveform
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, color='blue')
    plt.scatter(t[peak_index], y[peak_index], color='red', label=f'Peak Value: {peak_value:.2f}', zorder=5)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Audio Waveform with Peak Value')
    plt.legend()
    plt.grid(True)
    plot_filename = f"{username}_{filename}_waveform_with_peak.png"
    output_path = os.path.join('static', plot_filename)
    plt.savefig(output_path)
    plt.close()
    return output_path
