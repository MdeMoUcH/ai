#reproducir audio con 
import pyaudio  
import wave  
import os
import sys

#define stream chunk   
chunk = 1024  

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
audio = sys.argv[1]
print(audio)

#open a wav format music  
#f = wave.open(r"bark_samples/saludo.wav","rb")
f = wave.open(dir_path+"/venv-bark/bark/bark_samples/"+audio,"rb")
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate() 
