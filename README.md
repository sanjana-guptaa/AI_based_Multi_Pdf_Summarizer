# 📄 Multi-PDF Summarizer

A simple web application built using **Streamlit** and  **Python** to summarize the content of multiple PDF files. Upload PDFs, extract text, and get a summarized version of all their content.

## Features

- Upload multiple PDF files at once.
- Extract text from the PDFs.
- Split long text into chunks for better summarization.
- Summarize the extracted text using OpenAI GPT model.
- Download the summarized content as a `.txt` file.

## Prerequisites

To run the app locally, you'll need the following dependencies installed:

- Python 3.7+
- **Streamlit**
- **PyPDF2**
- **OpenAI API key**
- **langchain**

You can install all the required Python packages by running:
```
pip install streamlit PyPDF2 openai langchain
```
Setup
1. Clone the Repository
```
git clone https://github.com/yourusername/multi-pdf-summarizer.git
cd multi-pdf-summarizer
```

2. Set Up OpenAI API Key in Virtual Environment
```
openai.api_key = "your-api-key-here"
```
3. Run the Streamlit App

```
streamlit run app.py
```
After that, open your browser and navigate to http://localhost:8501 to use the app.

Usage
1. Upload Multiple PDFs
Click on the "Upload PDFs" button to upload multiple PDF files.

2. Summarize the PDFs
After uploading, click the "Summarize All" button.

3. View the Summary
The summarized content of the PDFs will be displayed.

4. Download Summary
You can download the summarized text as a .txt file by clicking the "Download Summary" button.


License
This project is licensed under the MIT License. See the LICENSE file for details.
