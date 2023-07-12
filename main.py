# https://github.com/embedchain/embedchain
# ----------------------------------------
# How does it work?
# Creating a chatbot over any dataset needs the following steps to happen

# load the data
# create meaningful chunks
# create embeddings for each chunk
# store the chunks in vector database
# Whenever a user asks any query, following process happens to find the answer for the query

# create the embedding for query
# find similar documents for this query from vector database
# pass similar documents as context to LLM to get the final answer.
# The process of loading the dataset and then querying involves multiple steps and each steps has nuances of it is own.

# How should I chunk the data? What is a meaningful chunk size?
# How should I create embeddings for each chunk? Which embedding model should I use?
# How should I store the chunks in vector database? Which vector database should I use?
# Should I store meta data along with the embeddings?
# How should I find similar documents for a query? Which ranking model should I use?
# These questions may be trivial for some but for a lot of us, it needs research, experimentation and time to find out the accurate answers.

# embedchain is a framework which takes care of all these nuances and provides a simple interface to create bots over any dataset.

# In the first release, we are making it easier for anyone to get a chatbot over any dataset up and running in less than a minute. All you need to do is create an app instance, add the data sets using .add function and then use .query

# Tech Stack
# ------------------------------------------
# embedchain is built on the following stack:

# Langchain as an LLM framework to load, chunk and index data
# OpenAI's Ada embedding model to create embeddings
# OpenAI's ChatGPT API as LLM to get answers given the context
# Chroma as the vector database to store embeddings