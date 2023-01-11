# OpenAI API  


### Anaconda environment


- Create a new environment in Anaconda:

```bash
conda create -n openai python=3.10 pip  
```

- To activate the environment, use:

```bash
conda activate openai
```

- Use pip to install the `openai` Python module into the environment:


```bash
pip install openai
```

- This package provides the IPython kernel for Jupyter:


```bash
pip install ipykernel
```


### API key


- In your code editor, create a new file with the name `key.py` (save it as `.py` file, not `.ipynb`) and insert this line:


```bash
OPENAI_API_KEY = 'foo'
```

- Now go to your OpenAI account and navigate to "[View API keys](https://beta.openai.com/account/api-keys)"

- Select "Create new secret key"

- Copy the key and insert it into your file `key.py` (replace `foo` with your API):

```bash
OPENAI_API_KEY = 'your-API'
```

- Save the changes


*Note: If you use a public GitHub-repo, make sure to add `key.py` to gitgnore. Review [this information about API safety]( https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)*


### Text generation with GPT3

Let's turn a product description into ad copy.

Open the file `copy-text.ipynb`.


In the file, you could change the following model parameters:

- `model`: The OpenAI API is powered by a [family of models](https://beta.openai.com/docs/models/gpt-3) with different capabilities and [price points](https://openai.com/api/pricing/). While *Davinci* is generally the most capable, the other models can perform certain tasks extremely well with significant speed or cost advantages. For example, *Curie* can perform many of the same tasks as Davinci, but faster and for 1/10th the cost.

- `prompt`: some user text input (a description of the task the model should perform).

- `temperature`: What sampling temperature to use. Higher values means the model will take more risks (this means it will generate more creative output). Try 0.9 for more creative applications, and 0 for ones with a well-defined answer.

- `max_tokens` (maximum length) - Does not control the length of the output, but a hard cutoff limit for token generation. 


## Image creation with DALL-E2

The [Images API](https://beta.openai.com/docs/guides/images/image-generation-beta) provides three methods for interacting with images:

1. Creating images from scratch based on a text prompt
2. Creating edits of an existing image based on a new text prompt
3. Creating variations of an existing image

Each image can be returned as either a URL or Base64 data, using the response_format parameter. URLs will expire after an hour.

We use option 1. to generate an image: `image-creation.ipynb`


## More examples

Explore what's possible with these [example applications](https://beta.openai.com/examples/)
