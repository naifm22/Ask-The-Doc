# Ask the Doc

Ask the Doc is a document question-answering application built with Streamlit, LangChain, Chroma, and the OpenAI API. Users can upload a text document and ask questions that are answered using information retrieved from that document.

## Live Application

- **Application:** https://ask-the-doc-alrashdi.streamlit.app/
- **Source code:** https://github.com/naifm22/Ask-The-Doc

## Features

- Upload UTF-8 `.txt` documents.
- Validate documents up to 5 MB.
- Split documents into overlapping text chunks.
- Generate embeddings with OpenAI.
- Store and search embeddings using Chroma.
- Retrieve document passages relevant to a question.
- Generate answers grounded in the uploaded document.
- Display chunk references and retrieved source passages.
- Handle invalid API keys, rate limits, connection failures, and invalid files.

## How It Works

1. The user uploads a text document.
2. The application validates and divides the document into overlapping chunks.
3. OpenAI generates an embedding for each chunk.
4. Chroma stores the embeddings in a vector index.
5. The user submits a question.
6. The application retrieves the most relevant document chunks.
7. OpenAI generates an answer using the retrieved context.
8. The answer includes references to the relevant chunk numbers.

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
├── streamlit_app.py
├── app_core.py
├── requirements.txt
├── README.md
└── sample_documents/
    └── ask_the_doc_demo.txt
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

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Start the application:

```bash
streamlit run streamlit_app.py
```

Open the local address displayed by Streamlit, normally:

```text
http://localhost:8501
```

## API Key Configuration

The application supports a key entered directly through the Streamlit sidebar or a key configured with Streamlit Secrets.

For local development, create:

```text
.streamlit/secrets.toml
```

Add the following setting:

```toml
OPENAI_API_KEY = "your-key-here"
```

For Streamlit Community Cloud, add the same setting through the application’s **Settings → Secrets** page.

Never commit a real API key or `.streamlit/secrets.toml` to GitHub.

## Usage

1. Open the application.
2. Upload a UTF-8 `.txt` document.
3. Select the answer model and number of chunks to retrieve.
4. Select **Process document**.
5. Enter a question about the document.
6. Select **Ask**.
7. Review the answer and its retrieved source chunks.

A sample document is available at:

```text
sample_documents/ask_the_doc_demo.txt
```

An example question for the sample document is:

> What controls are required before an AI pilot can move into production?

## Deployment

The application can be deployed using Streamlit Community Cloud.

1. Connect Streamlit Community Cloud to the GitHub repository.
2. Select the `main` branch.
3. Set the application entry point to `streamlit_app.py`.
4. Configure Python 3.12 when the option is available.
5. Add `OPENAI_API_KEY` through Streamlit Secrets if required.
6. Deploy the application.

When an owner-provided API key is configured, requests made by public visitors consume credits from that OpenAI project. Appropriate project spending limits should be configured.

## Privacy and Security

- API keys entered through the sidebar are not written to the repository.
- Uploaded documents are treated as untrusted reference material.
- The model is instructed to ignore commands contained within uploaded documents.
- Answers are restricted to information supported by retrieved document chunks.
- Uploaded text and vector indexes remain within the current Streamlit session.

## Limitations

- Only UTF-8 `.txt` files are supported.
- Documents are limited to 5 MB.
- An internet connection is required.
- Processing documents and answering questions consume OpenAI API credits.
- Answer quality depends on the uploaded document and retrieved context.

## License

This project is intended for educational use.
