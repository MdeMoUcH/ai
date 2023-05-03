#!/bin/bash

#https://github.com/JonathanFly/bark

#--text_prompt                Text prompt. If not provided, a set of default prompts will be used defined in this file.
#--history_prompt             Optional. Choose a speaker from the list of languages. Use --list_speakers to see all available options.
#--text_temp                  Text temperature. Default is 0.7.
#--waveform_temp              Waveform temperature. Default is 0.7.
#--filename                   Output filename. If not provided, a unique filename will be generated based on the text prompt and other parameters.
#--output_dir                 Output directory. Default is 'bark_samples'.
#--list_speakers              List all preset speaker options instead of generating audio.
#--use_smaller_models         Use for GPUs with less than 10GB of memory, or for more speed.
#--iterations                 Number of iterations. Default is 1.
#--split_by_words             Breaks text_prompt into <14 second audio clips every x words.
#--split_by_lines             Breaks text_prompt into <14 second audio clips every x lines.
#--stable_mode                Choppier and not as natural sounding, but much more stable for very long audio files.
#--confused_travolta_mode     Just for fun. Try it, and you'll understand. 

#--prompt_file                Optional. The path to a file containing the text prompt. Overrides the --text_prompt option if provided.
#--prompt_file_separator      Optional. The separator used to split the content of the prompt_file into multiple text prompts.

python3.10 -m venv venv-bark

cd venv-bark

source bin/activate

cd bark

fecha=`date +"%Y%m%d%H%M%S"`

python bark_perform.py --text_temp 0.8 --waveform_temp 0.8 --history_prompt es_speaker_2 --filename "saludo1_$fecha.wav" --text_prompt "`python ../../saludo.py`"

#Dependencias para reproducir audio:
#Sistema:
#sudo apt install libasound2-dev portaudio19-dev libportaudio2 ffmpeg
#venv:
#pip install pyaudio
python ../../play.py "saludo1_$fecha.wav" & python bark_perform.py --text_temp 0.8 --waveform_temp 0.8 --history_prompt es_speaker_2 --filename "saludo2_$fecha.wav" --text_prompt "Esto es un mensaje de prueba para comprobar el funcionamiento del modelo de inteligencia artificial bark."

python ../../play.py "saludo2_$fecha.wav"


#Para salir:
#deactivate










