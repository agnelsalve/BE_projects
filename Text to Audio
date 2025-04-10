pip install gTTS pygame

from gtts import gTTS
import pygame

audio = 'speech.mp3'
language = 'en'

spp = gTTS(text="Hello World, Welcome", lang=language, slow=False)
spp.save(audio)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(audio)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy(): 
    continue
