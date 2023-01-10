# OpenAI 


## OpenAI API 





## Setup

### Virtual Anaconda environment

Create a new environment in Anaconda:


```bash
conda create -n openai python=3.10 pip  
```

To activate the environment, use

```bash
conda activate openai
```

Install the `openai` Python module into the environment:

```bash
pip install openai
```

This package provides the IPython kernel for Jupyter:


```bash
pip install ipykernel
```


### OpenAI key

Create a python file called `key.py`. The file only contains the following line:

```bash
OPENAI_API_KEY = 'insertyourkey'
```
If you use GitHub, make sure to add the file `key.py` to gitgnore.


## Text generation with GPT3

Turn a product description into ad copy: `copy-text.ipynb`

Important model parameters:

- `model`: The OpenAI API is powered by a [family of models](https://beta.openai.com/docs/models/gpt-3) with different capabilities and [price points](https://openai.com/api/pricing/). While *Davinci* is generally the most capable, the other models can perform certain tasks extremely well with significant speed or cost advantages. For example, *Curie* can perform many of the same tasks as Davinci, but faster and for 1/10th the cost.

- `prompt`: some user input.

- `temperature`: What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.

- `max_tokens` (maximum length) - Does not control the length of the output, but a hard cutoff limit for token generation. Ideally you won’t hit this limit often, as your model will stop either when it thinks it’s finished, or when it hits a stop sequence you defined.


## Image creation with DALL-E2

The [Images API](https://beta.openai.com/docs/guides/images/image-generation-beta) provides three methods for interacting with images:

1. Creating images from scratch based on a text prompt
2. Creating edits of an existing image based on a new text prompt
3. Creating variations of an existing image

Each image can be returned as either a URL or Base64 data, using the response_format parameter. URLs will expire after an hour.

We use option 1. to generate an image: `image-creation.ipynb`


## More examples

Explore what's possible with these [example applications](https://beta.openai.com/examples/)