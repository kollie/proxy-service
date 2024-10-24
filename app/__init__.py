# initialize packages for use across the proxy service
import uvicorn
import os
import boto3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# create fastapi application
app = FastAPI()

# Initialize the S3 client with AWS credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

# Initialize S3 bucket name
BUCKET_NAME = os.getenv('BUCKET_NAME')

#add middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app import routes
