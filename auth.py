## 
import os
import openai
from key import *


## Authentification
openai.organization = "org-uQSGRL01u2KZUwdB4WjvHjPa"
openai.api_key = OPENAI_API_KEY

# Create product names from examples words.


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Product description: A home milkshake maker\nSeed words: fast, healthy, compact.\nProduct names: HomeShaker, Fit Shaker, QuickShake, Shake Maker\n\nProduct description: A pair of shoes that can fit any foot size.\nSeed words: adaptable, fit, omni-fit.",
  temperature=0.8,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)