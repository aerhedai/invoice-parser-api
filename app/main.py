from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from .config import get_credentials_from_info, get_documentai_client
from .parser import parse_invoice
import json

app = FastAPI()

@app.post("/parse-invoice/")
async def parse_invoice_api(
    service_account_file: UploadFile = File(...),
    invoice_file: UploadFile = File(...),
    processor_id: str = Form(...),
    project_id: str = Form(...),
    location: str = Form("us")
):
    try:
        # Load service account info
        sa_bytes = await service_account_file.read()
        sa_info = json.loads(sa_bytes)
        credentials = get_credentials_from_info(sa_info)
        docai_client = get_documentai_client(credentials)

        # Read invoice file
        invoice_bytes = await invoice_file.read()
        mime_type = invoice_file.content_type

        # Parse using Document AI
        document = parse_invoice(invoice_bytes, mime_type, docai_client, processor_id, project_id, location)

        # Return simplified result
        return {
            "entities": [
                {
                    "type": ent.type_,
                    "mention_text": ent.mention_text,
                    "confidence": ent.confidence
                }
                for ent in document.entities
            ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
