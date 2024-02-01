import time

import chromadb
import ollama
import streamlit

chroma_client = chromadb.Client()

streamlit.title("Rag Demo")

modelname = streamlit.selectbox(
    "Select the model of your choice",
    ["mistral", "llama2"],
)
assert modelname is not None

# Generate a simple response
streamlit.title("Generate a simple response")
query = streamlit.text_input(
    "Please Enter your query",
    value="Who is John Gobodong",
    placeholder="Enter your query here",
)
response = ollama.generate(model=modelname, prompt=query)
streamlit.markdown(f"{response}")

# Get embeddings
collection = chroma_client.create_collection(name="rag-data", get_or_create=True)
streamlit.title("Get Embeddings and add to database")
additional_information = streamlit.text_area(
    "Some nice content to enrich query. Each line will be treated as a separate document.",
    value="'fear&' is a podcast hosted by HasanAbi, Will Neff, AustinShow and QTCinderella.\n"
    "John Gobodong is an AI Engineer at lector.ai",
)
for i, more_info in enumerate(additional_information.split("\n")):
    embeds = ollama.embeddings(model=modelname, prompt=more_info)
    collection.add(
        documents=[more_info],
        embeddings=[embeds["embedding"]],  # type: ignore
        ids=[f"id{i}"],
    )

# Query the database and rerun the model prompt
query_embeds = ollama.embeddings(model=modelname, prompt=query)
db_result = collection.query(query_embeddings=query_embeds["embedding"], n_results=1)  # type: ignore
streamlit.text_area("Database Results", value=str(db_result))

streamlit.title("Generate a response with additional information")
new_prompt = (
    f'{query}\nHere is some additional information:\n{db_result["documents"][0][0]}\n'  # type: ignore
)
new_response = ollama.generate(model=modelname, prompt=new_prompt)
streamlit.markdown(f"{new_response}")
