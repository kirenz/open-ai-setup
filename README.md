# OpenAI Setup

## Virtual Environment

First, we create a new environment in Anaconda:


```bash
conda create -n openai python=3.10 pip  
```

We name the environment `openai`

To activate the environment, use

```bash
conda activate openai
```

Install the openai Python module:

```bash
pip install openai
```

## Authentication


Create a Python script called `auth.py`

```python
import os
import openai
openai.organization = "org-uQSGRL01u2KZUwdB4WjvHjPa"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
```
