## Authentification

import os
import openai
openai.organization = "org-uQSGRL01u2KZUwdB4WjvHjPa"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()