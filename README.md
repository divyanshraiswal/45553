# ScrapeGraph Application

## Overview
The **ScrapeGraph Application** is a Streamlit-based tool designed to scrape data from specified URLs using a combination of a large language model (LLM) and sentence transformers for embeddings. This application allows users to input a URL and a prompt, which are then processed to extract relevant data efficiently.

## Features
This application provides several key features. Users can input a specific URL to target for data extraction, and they have the option to specify a prompt to guide the scraping process. It utilizes the `SentenceTransformer` for generating embeddings from the scraped content and integrates `HuggingFaceEndpoint` to leverage the Llama-3.2-1B model for language processing tasks. Additionally, the results of the scraping process are saved as a JSON file, making it easy to access and utilize the data later.

## Requirements
Before running the application, ensure you have Python installed along with the necessary libraries: Streamlit, `sentence-transformers`, `scrapegraphai`, and `langchain_huggingface`. You can install these libraries using pip. Furthermore, the application attempts to install Playwright automatically. If the installation fails, you will need to ensure you have Playwright installed by running `playwright install`.

## Environment Variables
To use the application, set your Hugging Face API token as an environment variable. This is crucial for authenticating with the Hugging Face services. You can do this in your terminal by using the command `export HUGGINGFACEHUB_API_TOKEN='your_token_here'`.

## Usage
To run the application, launch it using the command `streamlit run app.py`, making sure to replace `app.py` with the actual filename of your script if it is different. Once the application is running, you will see input fields where you can provide the URL you wish to scrape and enter a custom prompt to guide the scraping process. After filling in these details, click on the **"Scrape Courses"** button to initiate the scraping task.

Once the scraping is complete, the results will be displayed on the screen in JSON format, allowing you to view the data easily. Additionally, the scraped data will be saved in a file named `courses.json`, making it convenient for later use.

## Error Handling
If any issues occur during the scraping process, the application will display an error message, indicating the nature of the problem. This feature helps users quickly identify and resolve any issues that may arise.

## Example
For instance, to scrape course data from a specified URL, you can enter the URL (e.g., `https://example.com/courses`) and provide a relevant prompt (e.g., "List the available courses"). After clicking **"Scrape Courses"**, the application will process the request and present the results for your review.
