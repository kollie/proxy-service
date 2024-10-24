#  Proxy Service for S3 with FastAPI

This project provides a proxy service for uploading and downloading files to and from AWS S3. The service is built using FastAPI and Boto3, and it is deployed on AWS Elastic Beanstalk with a CI/CD pipeline integrated with GitHub.

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
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

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
    uvicorn main:app --reload


