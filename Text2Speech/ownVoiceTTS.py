# pip3 install -U scipy

# git clone https://github.com/jnordberg/tortoise-tts.git
# %cd tortoise-tts
# !pip3 install transformers==4.19.0
# !pip3 install -r requirements.txt
# !python3 setup.py install




# import torch
# import torchaudio
# import torch.nn as nn
# import torch.nn.functional as F

# import IPython

# from tortoise.api import TextToSpeech
# from tortoise.utils.audio import load_audio, load_voice, load_voices

# # This will download all the models used by Tortoise from the HuggingFace hub.
# tts = TextToSpeech()




# # Define your own voice folder
# VOICE_NAME='gareth'
# text='Hello from this tutorial, I hope you enjoy it'

# # Generate with your own voice
# voice_samples, conditioning_latents = load_voice(VOICE_NAME)
# gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, 
#                           preset=preset)
# torchaudio.save(f'generated-{VOICE_NAME}.wav', gen.squeeze(0).cpu(), 24000)
# IPython.display.Audio(f'generated-{VOICE_NAME}.wav')