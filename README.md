This repository focuses on evaluating various techniques for identifying text duplicates within datasets. We are using Twitter data as an exsample. The main objective is to explore and compare different methods to determine the most effective approach for detecting and handling duplicates within a dataset.

The goal is to determine if a system has already received a particular piece of information, even if the text is structured differently. You can view the notebook [here](https://nbviewer.org/github/asmaatbaeen/duplicate_reports/blob/main/duplicate_reports.ipynb).

**Dataset Used:**
The dataset used consists of transport-related incident tweets, which can be found in the tweets_data folder. To ensure a sufficient number of duplicate tweets with information on the same incident, chatGPT was utilized to restructure the tweet text.

**Getting Started:**

*Python 3.11*
You will need Python 3.11 installed on your machine.

*Poetry:*
To manage the packages, Poetry is used. If you haven't already, install Poetry first. Then, follow these steps to install the dependencies:
```
$ poetry shell    # activate the virtual environment
$ poetry install  # install dependencies
```

*OpenAI:*
To run the notebook where duplicates are generated, you need an API key from [OpenAI](https://platform.openai.com/account/api-keys). Please note that OpenAI currently offers only a paid version.

To run the notebook LOCALLY, open the `duplicate_reports.ipynb` file using [VS Code](https://code.visualstudio.com/) or [Jupyter Labs](https://jupyterlab.readthedocs.io).

**Methods Used to Identify Duplicates:**
- Cosine similarity using TFIDF
- Levenshtein
- Fuzzy matching
- Embeddings 
    - Sentence transformers ('distilbert-base-nli-mean-tokens')
    - Sentence transformers ('all-MiniLM-L6-v2')



**Results:**
The results, including any graphs or visualizations, can be found in the notebook.