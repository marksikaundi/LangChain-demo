import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter



def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks
    
    
    

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with many PDF", page_icon=":books")
    
    st.header("Chat with many PDFs :books")
    st.text_input("Ask a question about your document:")
    
    
    with st.sidebar:
        st.subheader("Your document")
        pdf_docs = st.file_uploader(
            "Upload your PDF and click 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
            #get pdf
                raw_text = get_pdf_text(pdf_docs)
            
            #get text chuncks
            text_chunks = get_text_chunks(raw_text)
            st.write(text_chunks)
            
            #create vector store
    
if __name__ == '__main__':
    main()