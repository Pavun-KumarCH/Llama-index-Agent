import streamlit as st
from Components.data_ingestion import load_data
from Components.embedding import download_gemini_embedding
from Components.model_api import load_model

@st.cache_resource
def load_model_once():
    return load_model()

def main():
    st.set_page_config(page_title="University Course Documents")
    st.image("assets/LlamaIndex.jpg", use_column_width=True)
    st.header("Chat with Intelligent Agent using Gemini💁")

    # Sidebar Menu
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if not pdf_docs:
                st.error("Please upload PDF files to proceed.")
            else:
                with st.spinner("Processing..."):
                    # Load the data and model
                    document = load_data(pdf_docs)
                    model = load_model_once()  # Load model only once
                    query_engine = download_gemini_embedding(model, document)
                    st.success("Processing Complete!")

    # Text input for user's question
    user_question = st.text_input("Ask a Question from the Processed PDF Files")

    if user_question:
        if 'query_engine' not in locals():
            st.warning("Please upload and process the PDF files first.")
        else:
            response = query_engine.query(user_question)
            st.write(response.response)

if __name__ == "__main__":
    main()
