import os
import numpy as np
import pandas as pd
from scipy.fftpack import fft
from scipy.signal import welch
import pywt

# Function to compute Zero-Crossing Rate (ZCR)
def zero_crossing_rate(signal):
    return ((signal[:-1] * signal[1:]) < 0).sum() / len(signal)

# Function to compute FFT features
def compute_fft_features(signal, sampling_rate):
    fft_values = np.abs(fft(signal))
    fft_freq = np.fft.fftfreq(len(fft_values), d=1/sampling_rate)
    positive_fft = fft_values[:len(fft_values)//2]
    positive_freq = fft_freq[:len(fft_freq)//2]
    return {
        "fft_mean": np.mean(positive_fft),
        "fft_std": np.std(positive_fft),
        "mean_freq": np.sum(positive_fft * positive_freq) / np.sum(positive_fft),
        "median_freq": positive_freq[np.argsort(positive_fft.cumsum())[len(positive_fft)//2]]
    }

# Function to compute Power Spectral Density (PSD)
def compute_psd(signal, sampling_rate):
    freqs, psd = welch(signal, fs=sampling_rate)
    return np.mean(psd)  # Return mean PSD as a single value

# Function to compute Wavelet Decomposition features
def compute_wavelet_features(signal, wavelet='db4'):
    coeffs = pywt.wavedec(signal, wavelet, level=4)
    approx = coeffs[0]
    details = coeffs[1:]
    return {
        "approx_mean": np.mean(approx),
        "approx_std": np.std(approx),
        **{f"detail{i+1}_mean": np.mean(details[i]) for i in range(len(details))},
        **{f"detail{i+1}_std": np.std(details[i]) for i in range(len(details))}
    }

# Main function to process all `.npy` files
def process_npy_files(directory, sampling_rate=256, wavelet='db4', output_file="output/features.csv"):
    feature_list = []
    for file_name in os.listdir(directory):
        if file_name.endswith(".npy"):
            file_path = os.path.join(directory, file_name)
            data = np.load(file_path)  # Assuming `.npy` contains a 2D array (channels x samples)

            # Iterate through channels
            for channel_idx, signal in enumerate(data):
                # Extract features
                zcr = zero_crossing_rate(signal)
                fft_features = compute_fft_features(signal, sampling_rate)
                psd = compute_psd(signal, sampling_rate)
                wavelet_features = compute_wavelet_features(signal, wavelet)

                # Combine all features into a dictionary
                features = {
                    "file": file_name,
                    "channel": channel_idx,
                    "zcr": zcr,
                    **fft_features,
                    "psd": psd,
                    **wavelet_features
                }
                feature_list.append(features)

    # Convert to DataFrame and save to CSV
    features_df = pd.DataFrame(feature_list)
    features_df.to_csv(output_file, index=False)
    print(f"Feature extraction complete. Saved to {output_file}")

# Directory containing `.npy` files
npy_directory = "C:/Users/User/Desktop/Hackathon/Impulse/test_data/"  # Ensure this path is correct
output_csv = "output/standardized_features_traindata1.csv"  # Output file path

# Process `.npy` files
process_npy_files(npy_directory, sampling_rate=256, wavelet='db4', output_file=output_csv)
