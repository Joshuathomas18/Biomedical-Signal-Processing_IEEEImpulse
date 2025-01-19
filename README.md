<p align="right" style="margin-right: 0px;">
  <img src="th.jpg" alt="Image description" width="300"/>
</p>

# Biomedical Signal Processing - IEEE Impulse 2025



# Introduction


![maxresdefault](https://github.com/user-attachments/assets/5f5dc22a-1d8e-42d1-8629-135faf8bfa28)

<p style="text-align: justify;">Biomedical signal processing refers to the application of techniques and algorithms to analyze physiological signals from the human body, such as ECG, EEG, EMG, and others. In an era where healthcare moves to a more data-driven approach, biomedical signal processing can play an *important role in extracting meaningful information from such data. This field aims to convert such raw physiological signals to concrete insights and get an actionable diagnosis*. It not only enhances clinical decision-making but also supports the development of new medical technologies, offering the potential for real-time health monitoring, early detection of diseases, and remote patient care.</p>

<p style="text-align: justify;">For the final round of Impulse 2025, the participants are challenged to develop a robust model for classifying Electroencephalogram (EEG) seizure types from signals. Adding to it, an important aspect of it is to implement explainability techniques, promoting clinical trust in a hospital setting. The problem statement derives its motivation from the critical role of EEG in neurology, helping in diagnosing and managing neurological disorders. Manual EEG interpretation requires skill and is subjective. The integration of machine learning with explainability will make a practical and clinically accurate tool ready for use.</p>

<p style="text-align: justify;">A primary useful feature of an EEG model is to segregate seizure-containing EEGs from normal ones and secondly, in the latter, to demarcate seizure-specific regions and further classify seizure type, which helps neurologists establish a diagnosis quickly and effectively. Videographic seizure detection provides another layer of usefulness, catching rare seizures not reflected on EEGs and hence, improving the robustness of an EEG ML model.</p>


## Task 1: Basic Analysis of EEG Signals

Raw EEG signals require preprocessing and feature extraction to identify underlying patterns for classification. In this task, you will visualize EEG data and compute basic statistical metrics to derive key insights into signal characteristics.

- [**Task 1: Basic Analysis of EEG Signals**](https://github.com/Joshuathomas18/Biomedical-Signal-Processing_IEEImpulse/blob/main/task1.ipynb)

## Task 2: Extracting Frequency Domain Features

Extract frequency-based features from EEG signals to analyze brain activity. Fourier Transform and Wavelet Decomposition are key techniques used in this task to convert signals to the frequency domain and analyze them in both time and frequency.
![combined_signal](https://github.com/user-attachments/assets/53863d7e-2744-4539-bc2e-8c371cd64030)
**An example of combined plot**
![channel_2](https://github.com/user-attachments/assets/6db98132-3ab5-4b3c-81de-26577090a69d)
**An example of single plot**
- [**Task 2: Extracting Frequency Domain Features**](https://github.com/Joshuathomas18/Biomedical-Signal-Processing_IEEImpulse/blob/main/task2.ipynb)
![example_spectrogram](https://github.com/user-attachments/assets/2ef978b0-a178-42c1-b6a9-5a3f12842f6e)

![Screenshot 2025-01-19 135551](https://github.com/user-attachments/assets/2e78aea2-aa76-4623-ad96-6bff843485dd)
**All the required parameters**

## Task 3: Building the Baseline Model
![Graphical-representation-of-the-SVM-model](https://github.com/user-attachments/assets/ce92ec98-04b1-40c9-a605-b567b43c3e83)
**SVM model**

Use Fourier features and the Zero Crossing Rate to build a baseline machine learning model. This baseline will provide an initial performance metric, serving as a reference for future model improvements.

- [**Task 3: Building the Baseline Model**](https://github.com/Joshuathomas18/Biomedical-Signal-Processing_IEEImpulse/blob/main/task3.ipynb)

## Task 4: Building the Best Model

Improve upon the baseline model by experimenting with advanced techniques, hyperparameter tuning, and exploring sophisticated models beyond the SVM.

- [**Task 4: Building the Best Model**](https://github.com/Joshuathomas18/Biomedical-Signal-Processing_IEEImpulse/blob/main/task4.ipynb)

## Task 5: Interpretability of the Best Model

Ensure transparency and trust by making your model explainable. This task focuses on understanding which EEG channels are most influential in the model's predictions, which is vital for clinical acceptance.
![Screenshot 2025-01-19 140231](https://github.com/user-attachments/assets/da788597-48d4-4b70-8ad2-4ee6350197f0)


- [**Task 5: Interpretability of the Best Model**](https://github.com/Joshuathomas18/Biomedical-Signal-Processing_IEEImpulse/blob/main/task5.ipynb)
![Screenshot 2025-01-19 111150](https://github.com/user-attachments/assets/9e2829d2-aca7-435d-a480-5a793ea530d9)

![Screenshot 2025-01-19 133325](https://github.com/user-attachments/assets/16398feb-f40b-4e7f-8c68-331998d38069)
## Task 6: Denoising

Signal denoising is essential to remove noise caused by environmental factors, hardware, or motion artifacts. This task will clean the EEG data to ensure that subsequent analyses are based on high-quality, representative signals.

- [**Task 6: Denoising**](https://github.com/Joshuathomas18/Biomedical-Signal-Processing_IEEImpulse/blob/main/task6.ipynb)
![Screenshot 2025-01-19 133355](https://github.com/user-attachments/assets/c9ee0405-43f0-4543-a786-239007751fc1)

## Task 7: Generative Modeling Techniques for Synthetic EEG Data

Use generative models to create synthetic EEG data, helping augment training datasets and improve model performance. This task is essential when real-world data is limited, and it supports robust model development.

- [**Task 7: Generative Modeling Techniques for Synthetic EEG Data**](https://github.com/Joshuathomas18/Biomedical-Signal-Processing_IEEImpulse/blob/main/task7.ipynb)

![Screenshot 2025-01-19 135403](https://github.com/user-attachments/assets/b5c89242-1d6d-4072-8d1d-ffa6450a40e4)



