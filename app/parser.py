from google.cloud import documentai_v1 as documentai

def parse_invoice(document_bytes, mime_type, client, processor_id, project_id, location="us"):
    name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"

    raw_document = documentai.RawDocument(content=document_bytes, mime_type=mime_type)

    request = documentai.ProcessRequest(name=name, raw_document=raw_document)

    result = client.process_document(request=request)

    return result.document
