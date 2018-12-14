import numpy as np 
import matplotlib.pyplot as plt
import librosa
from scipy import signal
from scipy.io.wavfile import read, write
import pandas as pd
import os

data = pd.read_csv('ad_audio.csv')


audio_files = data['Video'].values
ad_names = data['Ad-name'].values
start_time = data['Start_time'].values
end_time = data['End_time'].values
if not os.path.exists('../mp3'):
    os.makedirs('../mp3')

msg = "Creating Database...."
print(msg)

for i in range(len(audio_files)):
	filepath = 'dataset_audio/' + str(audio_files[i]) + '.wav'
	sample_rate, y  = read(filepath)

	
	
	start_time = int(start_time[i]*sample_rate)
	end_time = int(end_time[i]*sample_rate)
	import pdb; pdb.set_trace()

	audio_segment = y[start_time:end_time]
	ad_filepath = '../mp3/' + ad_names[i] + '.mp3'
	write(ad_filepath, sample_rate, audio_segment)

msg = "Database created."
print(msg)
