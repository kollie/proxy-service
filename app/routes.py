import os
import io
import uuid
from fastapi import File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from botocore.exceptions import NoCredentialsError

from app import app, BUCKET_NAME, s3_client

@app.post("/proxy/upload/", tags=["Upload File"])
async def proxy_upload_file(file: UploadFile = File(...)):
    """
    Proxy endpoint to upload a file to S3.

    Description:
        file (str): the file to be uploaded.
        unique_filename (str): then name of the file, unique to avoid name conflict in s3.
        BUCKET_NAME: the s3 destination of the file.
        HTTPException: raises errors in the case the file was not uploaded
    """
    try:
        file_extension = os.path.splitext(file.filename)[1]
        unique_filename = f"proxy-{uuid.uuid4()}{file_extension}"
        s3_client.upload_fileobj(file.file, BUCKET_NAME, unique_filename)
        return {"message": f"File '{unique_filename}' uploaded successfully"}
    except NoCredentialsError:
        raise HTTPException(status_code=403, detail="there was an error with your aws credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"an error occured while uploading the file '{str(e)}'")

@app.get("/proxy/download/{file_name}", tags=["Download File"])
async def proxy_download_file(file_name: str):
    """
    Proxy endpoint to download a file from S3.

    Description:
        file_name (str): the file to be downloaded.
        BUCKET_NAME: the file s3 destination of the file.
        HTTPException: raises errors in the case the file is not found
    """
    try:
        file_obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
        return StreamingResponse(io.BytesIO(file_obj['Body'].read()), media_type='application/octet-stream')
    except s3_client.exceptions.NoSuchKey:
        raise HTTPException(status_code=404, detail=f"file '{file_name}' not found")
    except NoCredentialsError:
        raise HTTPException(status_code=403, detail="there was an error with your aws credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"an error occured while downloading the file '{str(e)}'")


