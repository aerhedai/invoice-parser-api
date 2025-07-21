# 🧾 Invoice & Receipt Parser API

A lightweight, production-ready Python API to parse structured data from invoices and receipts using Google Cloud's Document AI Invoice Parser. Built with FastAPI and designed for flexibility and extensibility.

## 🚀 Features

- Parses invoices and receipts from **PDFs or images**
- Extracts key fields (totals, vendor, dates, line items, tax, etc.)
- Uses Google Cloud's **specialised Invoice Parser**
- Accepts user-provided **Google service accounts** for security
- Cleanly structured with modular components (`main.py`, `parser.py`, `uploader.py`, `config.py`)
- Easily extendable for other Document AI processors

---

## 🛠️ Technologies Used

- 🧠 [Google Cloud Document AI](https://cloud.google.com/document-ai)
- ⚙️ FastAPI
- 🔐 Google Service Account Authentication
- 📦 Python 3.9+

---

## 📂 Project Structure

```
invoice-parser-api/
├── app/
│   ├── main.py         # FastAPI app entry point
│   ├── config.py       # Handles credentials and client setup
│   ├── parser.py       # Logic for processing Document AI output
│   └── uploader.py     # Handles PDF/image uploads from users
├── requirements.txt
├── README.md
└── CHANGELOG.md
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-ORG/invoice-parser-api.git
cd invoice-parser-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Enable Google Cloud APIs

Enable the following APIs in your [GCP Console](https://console.cloud.google.com/):

- Document AI API
- Cloud Storage API (optional if uploading files to GCS)

### 5. Prepare a service account

1. Create a Service Account in GCP
2. Grant `Document AI User` and (optionally) `Storage Object Viewer`
3. Download the JSON credentials file

> 🔐 Your service account JSON is **not hardcoded** – users provide it as part of the API call.

---

## ▶️ Running the API

From the root of the project:

```bash
uvicorn app.main:app --reload
```

The API will be available at:  
`http://localhost:8000/docs` (for Swagger UI)

---

## 📥 Example Request

**POST** `/parse-invoice`

Form-data:
- `file`: Your PDF or image
- `service_account_json`: File field for your Google Cloud service account
- `processor_id`: The processor ID of your invoice parser
- `project_id`: Your GCP project ID
- `location`: Region where processor is deployed (e.g. `us`)

---

## 📦 Versioning

We use [Semantic Versioning](https://semver.org/):  
**MAJOR.MINOR.PATCH**

See `CHANGELOG.md` for version history.

---

## 🛡️ License

MIT © [Aerhed AI]

---
