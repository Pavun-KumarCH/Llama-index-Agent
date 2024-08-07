# AI-Enhanced Content Generation for University Courses

This project leverages LlamaIndex and Gemini Model Pro 1.5 to generate precise, original, and plagiarism-free summaries of university course materials. By processing PDFs of students' syllabi and other relevant documents, the system produces concise and accurate summaries that enhance the learning experience.

## Project Overview

The AI-Enhanced Content Generation system utilizes LlamaIndex and Gemini Model Pro 1.5 to analyze course content and produce high-quality summaries. This project aims to assist both students and educators by providing well-organized, easy-to-understand summaries of academic materials.

## Key Components

- **LlamaIndex**: The AI model used for creating vector embeddings and handling similarity searches. LlamaIndex is instrumental in breaking down the content into manageable chunks and generating relevant embeddings.
- **Gemini Model Pro 1.5**: The core AI model used for summarizing the extracted content. Gemini Model Pro 1.5 excels at understanding and generating text from the provided documents.
- **LangChain**: Although used separately, LangChain facilitates the interaction between AI models and the content generation processes, ensuring smooth integration and efficient handling of summarization tasks.

## How It Works

1. **Data Input**:
   - Upload PDF files containing students' syllabi and other course-related documents.
   - The system supports multiple document types and formats to ensure versatility.

2. **Content Processing**:
   - **LlamaIndex** analyzes the input PDFs to extract relevant content and create vector embeddings.
   - **Gemini Model Pro 1.5** processes the content to generate concise summaries.
   - **LangChain** orchestrates the interaction between these models, ensuring accurate and contextually relevant summaries.

3. **Content Generation**:
   - The AI models generate summaries that are concise, original, and free from plagiarism.
   - Summaries are tailored to reflect the key concepts and details from the provided syllabi and documents.

4. **Output**:
   - The generated summaries are presented in an easily accessible format.
   - Users can review and utilize these summaries for educational purposes, enhancing both teaching and learning experiences.

## Workflow

![Workflow Diagram](https://github.com/Pavun-KumarCH/Llama-index-Agent/blob/main/assets/LangChainandLlamaIndex.png)

![Workflow Diagram](https://github.com/Pavun-KumarCH/Llama-index-Agent/blob/main/assets/basic_rag.png)

## Getting Started

To set up and run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pavun-KumarCH/Llama-index-Agent/blob/main/README.md.git
3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
4. **Run the Application:**
   ```
   streamlit app.py
5. **Upload Your PDFs:**
   - Access the application through your browser or terminal interface.
   -  Upload the course PDFs to generate summaries.

## Upload Your PDFs

Access the application through your browser or terminal interface. Upload the course PDFs to generate summaries.

## Documentation

### Phase 1 - Interactive PDF Processing
> Corresponding notebook: [Data_Ingestion.ipynb](https://github.com/Pavun-KumarCH/Llama-index-Agent/blob/main/Components/data_ingestion.py)

Implemented tasks:
- **Upload PDFs**: Create an interface for users to upload multiple PDF documents.
- **Extract Text**: Read and extract text content from the uploaded PDFs.
- **Display Results**: Show extracted text and user queries in a user-friendly format.

### Phase 2 - Text Chunking and Vector Store Creation
> Corresponding notebook: [Embedding.ipynb](https://github.com/Pavun-KumarCH/Llama-index-Agent/blob/main/Components/embedding.py)

Implemented tasks:
- **Split Text**: Break down the extracted text into manageable chunks.
- **Create Embeddings**: Convert text chunks into vector embeddings using LlamaIndex.
- **Build Vector Store**: Store these embeddings in a vector store for efficient similarity searches.

### Phase 3 - Conversational QA System
> Corresponding notebook: [Model_API.ipynb](https://github.com/Pavun-KumarCH/Llama-index-Agent/blob/main/Components/model_api.py)

Implemented tasks:
- **Setup QA Chain**: Configure a question-answering chain with Gemini Model Pro 1.5.
- **Process Queries**: Use the QA system to answer user questions based on the processed text.
- **Display Responses**: Show generated responses and relevant text snippets in a user-friendly format.

### Project Overview Live Preview
![Project Showcase](https://github.com/Pavun-KumarCH/Llama-index-Agent/blob/main/assets/showcase.gif)

## Future Enhancements
- **Expand Document Support**: Integrate additional file formats and types for broader applicability.
- **Improve Summary Quality**: Enhance summarization algorithms for more precise content generation.
- **User Interface**: Develop a more intuitive user interface for easier interaction.

## Contributing
Feel free to contribute to this project by submitting issues, suggesting improvements, or making pull requests. For detailed contributing guidelines.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
