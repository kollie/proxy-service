#  Proxy Service for S3 with FastAPI

This project provides a proxy service for uploading and downloading files to and from AWS S3. The service is built using FastAPI and Boto3.

## Features

- Upload files to S3
- Download files from S3

## Getting Started

### Prerequisites to run the application on your local machine

- Python 3.7+

### AWS Account
- AWS account with S3 and IAM permissions
- AWS CLI configured with your credentials

### Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:kollie/proxy-service.git
   cd proxy-service

2. **Create Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

4. **Set Environment Variables**
    ```bash
    export AWS_ACCESS_KEY_ID='your-access-key-id'
    export AWS_SECRET_ACCESS_KEY='your-secret-access-key'
    export AWS_REGION='your-region'
    export API_KEY='your-api-key'
    export BUCKET_NAME='your-bucket-name'

5. **Runing The Service Locally**
    ```bash
    uvicorn app:app --reload

### Testing
You can test the service locally with the swagger UI or using cur

http://127.0.0.1:8000/docs

![Upload File](https://github.com/kollie/proxy-service/blob/main/image/Screenshot%202024-10-24%20at%2015.02.20.png?raw=true)

![Download File](https://github.com/kollie/proxy-service/blob/main/image/Screenshot%202024-10-24%20at%2015.03.58.png?raw=true)

### Upload
    ```base
    curl -X 'POST' \
        'http://127.0.0.1:8000/proxy/upload/' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F 'file=@path/to/your/file'

### Download
```bash
curl -X 'GET' \
    'http://127.0.0.1:8000/proxy/download/your-file-name' \
    -H 'accept: application/octet-stream'

Direct download using a web browser
http://127.0.0.1:8000/proxy/download/your-file-name


