# RAG in a box
This is a simple repo to make and try out a simple RAG app. Will likely not work or be abandoned soon
I also roughly document my thoughts in here, so it might be confusing at times (as am I).


## Initial idea
I want to implement a simple RAG app using Ollama, some documents (no idea from where and which) and a vector database for fast retrieval (likely ChromaDB).  
There are already a ton of similar and better repos implementing the same, so don't use this if you want some actual good app as this is just a playground.

## Steps to do (ideally with UI)

1. Run Ollama locally (probably using Mistral or llama2)
2. Get query
3. Embed query
4. Get context relevant text chunks from vector store
5. Enhance query
6. ...
7. Profit

### 1. Run Ollama locally
I won't go into detail, is it might vary greatly based on hard- and software. Just get into a state where you can run the following commands.
```sh
ollama serve
ollama run llama2
```
This will start the ollama server and load the llama2 7B model.

### 2. Get the query
To get the query from the user, we will make a simple UI using Streamlit. In this step it should simple provide an interface for some user.
