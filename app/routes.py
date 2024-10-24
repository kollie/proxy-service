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

    Args:
        file (UploadFile): The file to be uploaded.

    Returns:
        dict: A message indicating the success of the upload.

    Raises:
        HTTPException: Exception to handle error while uploading the file.
    
    Bucket Name:
        The S3 bucket name where the file will be uploaded.
    
    Unique Filename:
        The unique file name is generated using uuid to avoid file naming confict in s3.
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

@app.get("/proxy/download/{file_name}")
async def proxy_download_file(file_name: str):
    """
    Proxy endpoint to download a file from S3.

    Args:
        file_name (str): The name of the file to be downloaded.

    Returns:
        StreamingResponse: The file content as a streaming response.

    Raises:
        HTTPException: If the file is not found, AWS credentials are not found or incomplete, or any other exception occurs.
    
    Bucket Name:
        The S3 bucket name from where the file will be downloaded.
    """
    try:
        file_obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_name)
        return StreamingResponse(io.BytesIO(file_obj['Body'].read()), media_type='application/octet-stream')
    except s3_client.exceptions.NoSuchKey:
        raise HTTPException(status_code=404, detail=f"file '{file_name}' not found")
    except NoCredentialsError:
        raise HTTPException(status_code=403, detail="there was an error with your aws credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"an error occured while uploading the file '{str(e)}'")


