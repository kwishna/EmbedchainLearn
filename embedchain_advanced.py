import os
from embedchain import App
from embedchain.config import InitConfig, AddConfig, QueryConfig
from chromadb.utils import embedding_functions

# Example: use your own embedding function
config = InitConfig(ef=embedding_functions.OpenAIEmbeddingFunction(
  api_key=os.getenv("OPENAI_API_KEY"),
  organization_id=os.getenv("OPENAI_ORGANIZATION"),
  model_name="text-embedding-ada-002"))
naval_chat_bot = App(config)

# Example: define your own chunker config for `youtube_video`
youtube_add_config = {
  "chunker": {
    "chunk_size": 1000,
    "chunk_overlap": 100,
    "length_function": len,
  }
}
naval_chat_bot.add("youtube_video",
                   "https://www.youtube.com/watch?v=3qHkcs3kG44",
                   AddConfig(**youtube_add_config))

add_config = AddConfig()
naval_chat_bot.add(
  "pdf_file",
  "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf",
  add_config)
naval_chat_bot.add("web_page", "https://nav.al/feedback", add_config)
naval_chat_bot.add("web_page", "https://nav.al/agi", add_config)

naval_chat_bot.add_local(
  "qna_pair",
  ("Who is Naval Ravikant?",
   "Naval Ravikant is an Indian-American entrepreneur and investor."),
  add_config)

query_config = QueryConfig()  # Currently no options
print(
  naval_chat_bot.query(
    "What unique capacity does Naval argue humans possess when it comes to understanding explanations or concepts?",
    query_config))

# InitConfig:-
# option	  description	                type	                       default
# ef	    embedding function	  chromadb.utils.embedding_functions	{text-embedding-ada-002}
# db	    vector database      	BaseVectorDB	                      ChromaDB

# Query Config:-
# option	    description	                        type
# template	  custom template for prompt          Template

# default;
# Template("Use the following pieces of context to answer the query at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. contextQuery :query Helpful Answer:")
