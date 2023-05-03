#!/bin/bash

#https://github.com/suno-ai/bark
#https://github.com/JonathanFly/bark

python3.10 -m venv venv-bark

cd venv-bark

source bin/activate

pip install soundfile

git clone https://github.com/JonathanFly/bark

cd bark

pip install . 

python bark_perform.py --split_by_words 40 --text_temp 0.8 --waveform_temp 0.8 --text_prompt "`python ../../saludo.py`"

#Para salir:
#deactivate










