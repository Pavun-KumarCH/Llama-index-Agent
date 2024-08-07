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

    # Initialize session state
    if 'query_engine' not in st.session_state:
        st.session_state.query_engine = None
    if 'model' not in st.session_state:
        st.session_state.model = load_model_once()

    # Sidebar Menu
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
        
        # Button to process files
        if st.button("Submit & Process"):
            if not pdf_docs:
                st.error("Please upload PDF files to proceed.")
            else:
                with st.spinner("Processing..."):
                    document = load_data(pdf_docs)
                    st.session_state.query_engine = download_gemini_embedding(st.session_state.model, document)
                    st.success("Processing Complete!")

    # Text input for user's question
    if st.session_state.query_engine:
        user_question = st.text_input("Ask a Question from the Processed PDF Files")
        
        if user_question:
            response = st.session_state.query_engine.query(user_question)
            st.write(response.response)
    else:
        st.info("Please upload and process PDF files first.")

if __name__ == "__main__":
    main()
