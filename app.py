import asyncio
import nest_asyncio
import json
import streamlit as st
from sentence_transformers import SentenceTransformer
from scrapegraphai.graphs import SmartScraperMultiGraph
from langchain_huggingface import HuggingFaceEndpoint
import subprocess
import os
from dotenv import load_dotenv  # Import load_dotenv from dotenv

# Load environment variables
load_dotenv()
token=os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv('HUGGINGFACEHUB_API_TOKEN')

# Install Playwright if not already installed
try:
    subprocess.run(["playwright", "install"], check=True)
except Exception as e:
    st.warning("Playwright installation failed. Make sure Playwright is installed.")

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Load the sentence transformer model
embedding_model_instance = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Streamlit Application
st.title("ScrapeGraph Application")
st.write("Enter a URL to scrape and your prompt for the scraping task.")

# Custom URL Input
custom_url = st.text_input("Enter the URL for scraping:")

# Prompt Input
user_prompt = st.text_input("Enter your prompt for scraping:")

# LLM Configuration
llm_model_instance = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B",  # Using Llama-3.2-1B
    max_length=128,
    temperature=1,
    token=token  
)

# Scraping Configuration
graph_config = {
    "llm": {
        "model": llm_model_instance,  # Use HuggingFaceEndpoint for LLM
        "temperature": 1
    },
    "embeddings": {
        "model_instance": embedding_model_instance  # Use SentenceTransformer for embeddings
    },
    'verbose': True,
    "headless": True  # Set to True to run in headless mode
}

# Run the scraper when the button is clicked
if st.button("Scrape Courses"):
    if not custom_url or not user_prompt:
        st.error("Please provide both a URL and a prompt.")
    else:
        try:
            # Create the SmartScraperMultiGraph instance with the custom URL
            smart_scraper_graph = SmartScraperMultiGraph(
                prompt=user_prompt,  # Use the user-defined prompt
                source=[custom_url],  # Scrape only the provided URL
                config=graph_config
            )

            # Run the scraper
            result = smart_scraper_graph.run()

            # Save the JSON data to a file
            with open("courses.json", "w") as outfile:
                json.dump(result, outfile, indent=4)

            # Display the results in Streamlit
            st.success("Scraping completed successfully!")
            st.json(result)  # Display the result as a JSON object

        except Exception as e:
            st.error(f"An error occurred: {e}")
