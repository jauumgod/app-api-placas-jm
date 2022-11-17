import apps.replicate as replicate
import os
import sys



fotos = []

for fotos in 

model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("8abccf52e7cba9f6e82317253f4a3549082e966db5584e92c808ece132037776")
output = version.predict(prompt="...")