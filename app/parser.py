import tempfile

def save_temp_file(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file_bytes)
        return tmp.name
