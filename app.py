import streamlit as st
import PyPDF2
import openai
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

openai.api_key = ""


# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text.strip()

# Function to split text into chunks
def split_text(text, chunk_size=1000, overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    return text_splitter.split_text(text)

# Function to summarize text using OpenAI API

def summarize_text(text):
    try:
        client = openai.OpenAI()  # Create OpenAI client
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize the following text:\n{text}"}
            ],
            max_tokens=200,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"


# Streamlit UI
st.title("📄 Multi-PDF Summarizer")
st.write("Upload multiple PDF files, and get a summarized version of all their content.")

# Upload multiple PDFs
uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    extracted_texts = {}

    # Extract text from each PDF
    for pdf_file in uploaded_files:
        st.subheader(f"📑 Extracting Text from: {pdf_file.name}")
        extracted_texts[pdf_file.name] = extract_text_from_pdf(pdf_file)

    # Button to summarize all PDFs together
    if st.button("Summarize All"):
        st.subheader("Summarizing PDFs...")
        final_summaries = []

        for filename, text in extracted_texts.items():
            chunks = split_text(text)
            summary_results = []

            for chunk in chunks:
                summary = summarize_text(chunk)
                summary_results.append(summary)

            full_summary = "\n\n".join(summary_results)
            final_summaries.append(f"### {filename} Summary:\n{full_summary}")

        # Combine all summaries
        complete_summary = "\n\n".join(final_summaries)

        # Display final summary
        st.subheader("📌 Final Summary for All PDFs")
        st.text_area("All Summarized PDFs", complete_summary, height=500)

        # Download summarized text
        st.download_button("Download Summary", complete_summary, file_name="pdf_summary.txt")
