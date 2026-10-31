# Ask the Doc App

This project implements the GenAI Assignment 1 document question-answering application. It uses Streamlit for the interface, LangChain text splitting, OpenAI embeddings, Chroma retrieval, and the OpenAI Responses API for grounded answers.

## Features

- Upload UTF-8 `.txt` documents up to 5 MB.
- Split documents into overlapping 1,000-character chunks.
- Embed chunks with `text-embedding-3-small`.
- Retrieve relevant chunks from an in-memory Chroma vector store.
- Generate grounded answers with chunk references.
- Use a visitor-supplied API key or an optional Streamlit secret.
- Handle invalid keys, rate limits, connection failures, and invalid files.

## Requirements

- Python 3.12
- Internet access
- An OpenAI API key with API credits

## Local setup

### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open the local URL shown by Streamlit, usually `http://localhost:8501`.

## API key options

The assignment-compatible default is to enter an API key in the app's password field. The key is used for the current Streamlit session and is not written to the project.

Alternatively, copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and insert a key for local testing. Never commit the real secrets file.

On Streamlit Community Cloud, add this through the app's **Settings → Secrets** interface:

```toml
OPENAI_API_KEY = "your-key-here"
```

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The unit tests do not call the OpenAI API and do not consume credits.

## Deployment

1. Copy this folder to the machine that can access GitHub.
2. Review the files and initialize Git there.
3. Create a GitHub repository and push this folder.
4. In Streamlit Community Cloud, create an app from that repository.
5. Select the branch and set the main file path to `streamlit_app.py`.
6. Select Python 3.12 in Advanced settings.
7. Add `OPENAI_API_KEY` to Streamlit Secrets only if the deployed app should use your key.
8. Deploy and test the public URL.

See `DEPLOYMENT_CHECKLIST.md` for the final verification list.

## Suggested demonstration

Upload `sample_documents/ask_the_doc_demo.txt` and ask:

> What controls are required before an AI pilot can move into production?

The answer should be grounded in the sample document and cite relevant chunk numbers.

