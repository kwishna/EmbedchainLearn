#!pip install -q embedchain
from embedchain import App
from embedchain.config import QueryConfig
import os
import dotenv
# --------------------------------------------
# from embedchain import OpenSourceApp
# naval_chat_bot = OpenSourceApp()
#
# OpenSourceApp (uses opensource models, free)
# from embedchain import OpenSourceApp

# naval_chat_bot = OpenSourceApp()
# OpenSourceApp uses open source embedding and LLM model. It uses all-MiniLM-L6-v2 from Sentence Transformers library as the embedding model and gpt4all as the LLM.

# Here there is no need to setup any api keys. You just need to install embedchain package and these will get automatically installed.

# Once you have imported and instantiated the app, every functionality from here onwards is the same for either type of app.
# --------------------------------------------

# from embedchain import PersonApp
# naval_chat_bot = PersonApp("name_of_person_or_character") #Like "Yoda"

# ---------------------------------------------
os.environ['OPENAI_API_KEY'] = 'sk-xxx'  #environment variables
naval_bot = App()
# App uses OpenAI's model, so these are paid models. You will be charged for embedding model usage and LLM usage.

# App uses OpenAI's embedding model to create embeddings for chunks and ChatGPT API as LLM to get answer given the relevant docs. Make sure that you have an OpenAI account and an API key. If you have dont have an API key, you can create one by visiting this link.

# Once you have the API key, set it in an environment variable called OPENAI_API_KEY

# ----------------------------------------------
# Embed Online Resources
naval_bot.add("youtube_video", "https://www.youtube.com/watch?v=3qHkcs3kG44")
naval_bot.add(
  "pdf_file",
  "https://navalmanack.s3.amazonaws.com/Eric-Jorgenson_The-Almanack-of-Naval-Ravikant_Final.pdf"
)
naval_bot.add("web_page", "https://nav.al/feedback")
naval_bot.add("web_page", "https://nav.al/agi")
naval_bot.add_local(
  'text',
  'Seek wealth, not money or status. Wealth is having assets that earn while you sleep. Money is how we transfer time and wealth. Status is your place in the social hierarchy.'
)
# naval_bot.add('docx', 'a_local_docx_file_path')

# Embed Local Resources
naval_bot.add_local(
  "qna_pair",
  ("Who is Naval Ravikant?",
   "Naval Ravikant is an Indian-American entrepreneur and investor."))

# --------------------------------------------------------
# This interface is like a question answering bot. It takes a question and gets the answer. It does not maintain context about the previous chats.
print(naval_bot.query("What are the ways to become rich?"))
print(naval_bot.query("What do you think about fame and wealth?"))
print(naval_bot.query("What is a better alternative to UBI?"))

# ---------------------------------------------------------
# This interface is chat interface where it remembers previous conversation. Right now it remembers 5 conversation by default.
print(naval_bot.chat("How to be happy in life?"))
# answer: The most important trick to being happy is to realize happiness is a skill you develop and a choice you make. You choose to be happy, and then you work at it. It's just like building muscles or succeeding at your job. It's about recognizing the abundance and gifts around you at all times.

print(naval_bot.chat("who is naval ravikant?"))
# answer: Naval Ravikant is an Indian-American entrepreneur and investor.

print(naval_bot.chat("what did the author say about happiness?"))
# answer: The author, Naval Ravikant, believes that happiness is a choice you make and a skill you develop. He compares the mind to the body, stating that just as the body can be molded and changed, so can the mind. He emphasizes the importance of being present in the moment and not getting caught up in regrets of the past or worries about the future. By being present and grateful for where you are, you can experience true happiness.

print(naval_bot.dry_run('Can you tell me who Naval Ravikant is?'))
'''
Use the following pieces of context to answer the query at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
        Q: Who is Naval Ravikant?
A: Naval Ravikant is an Indian-American entrepreneur and investor.
        Query: Can you tell me who Naval Ravikant is?
        Helpful Answer:
'''

# --------------------------------------------------------------
query_config = QueryConfig(stream=True)
resp = naval_bot.query(
  "What unique capacity does Naval argue humans possess when it comes to understanding explanations or concepts?",
  query_config)

for chunk in resp:
  print(chunk, end="", flush=True)
# answer: Naval argues that humans possess the unique capacity to understand explanations or concepts to the maximum extent possible in this physical reality.

# ---------------------------------------------------------
# Resets the database and deletes all embeddings. Irreversible. Requires reinitialization afterwards.
# app.reset()

# ---------------------------------------------------------
# Counts the number of embeddings (chunks) in the database.
# print(app.count())
