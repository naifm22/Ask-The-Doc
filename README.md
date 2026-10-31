# Ask the Doc

Ask the Doc is a document question-answering application built with Streamlit, LangChain, Chroma, and the OpenAI API. Users can upload a text document and ask questions that are answered using information retrieved from that document.

## Live Application

- **Application:** https://ask-the-doc-alrashdi.streamlit.app/
- **Source code:** https://github.com/naifm22/Ask-The-Doc

## Features

- Upload UTF-8 `.txt` documents up to 5 MB.
- Split documents into overlapping text chunks.
- Generate embeddings with OpenAI.
- Store and search embeddings using Chroma.
- Retrieve document passages relevant to a question.
- Generate grounded answers with chunk references.
- Display retrieved source passages.
- Handle invalid API keys, rate limits, connection failures, and invalid files.

## How It Works

1. The user uploads a text document.
2. The user enters their own OpenAI API key.
3. The application divides the document into overlapping chunks.
4. OpenAI generates an embedding for each chunk.
5. Chroma stores the embeddings in a vector index.
6. The user submits a question.
7. The application retrieves the most relevant document chunks.
8. OpenAI generates an answer grounded in the retrieved context.

## Technology Stack

- Python 3.12
- Streamlit
- OpenAI API
- LangChain
- Chroma
- `text-embedding-3-small` embeddings

## Project Structure

```text
Ask-The-Doc/
├── .streamlit/
│   └── config.toml
├── sample_documents/
│   └── ask_the_doc_demo.txt
├── .gitignore
├── .python-version
├── app_core.py
├── README.md
├── requirements.txt
└── streamlit_app.py
```

## Local Setup

Clone the repository:

```bash
git clone https://github.com/naifm22/Ask-The-Doc.git
cd Ask-The-Doc
```

Create and activate a virtual environment.

### Linux or macOS

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies and start the application:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the local address displayed by Streamlit, normally `http://localhost:8501`.

## API Key

Each user must enter their own OpenAI API key in the application's password field. The key is used to create document embeddings and generate answers during the current Streamlit session. It is not written to the repository or stored by the application.

## Usage

1. Open the application.
2. Enter your OpenAI API key in the sidebar.
3. Upload a UTF-8 `.txt` document.
4. Select the answer model and number of chunks to retrieve.
5. Select **Process document**.
6. Enter a question about the document.
7. Select **Ask**.
8. Review the answer and retrieved source chunks.

A sample document is available at `sample_documents/ask_the_doc_demo.txt`.

An example question is:

> What controls are required before an AI pilot can move into production?

## Deployment

The application can be deployed using Streamlit Community Cloud:

1. Connect Streamlit Community Cloud to the GitHub repository.
2. Select the `main` branch.
3. Set the application entry point to `streamlit_app.py`.
4. Configure Python 3.12 when the option is available.
5. Deploy the application.

No application-owned OpenAI API key is required because each visitor supplies their own key.

## Privacy and Security

- API keys are entered through a password field and are not displayed.
- API keys are not written to the repository or stored by the application.
- Uploaded documents are treated as untrusted reference material.
- The model is instructed to ignore commands contained within uploaded documents.
- Answers are restricted to information supported by retrieved document chunks.
- Uploaded text and vector indexes remain within the current Streamlit session.

## Limitations

- Only UTF-8 `.txt` files are supported.
- Documents are limited to 5 MB.
- An internet connection is required.
- Each user needs an OpenAI API key with available credits.
- Processing documents and answering questions consume the user's OpenAI API credits.
- Answer quality depends on the uploaded document and retrieved context.

## License

This project is intended for educational use.
