import StreamlitApp as st
from Components.data_ingestion import load_data
from Components.embedding import download_gemini_embedding
from Components.model_api import load_model

def main():
    st.set_page_config(page_title = "University Course Documents")
    st.image("assets/LlamaIndex.jpg", use_column_width=True)
    st.header("Chat with Intelligent Agent using Gemini💁")

    pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
    user_question = st.text_input("Ask a Question from the PDF Files")

    if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                document = load_data(pdf_docs)
                model = load_model()
                query_engine = download_gemini_embedding(model, document)
                st.success("Done")
                response = query_engine.query(user_question)
                st.write(response.response)

if __name__ == "__main__":
     main()

