"""
AWS S3 Operations - Python SDK Examples
Upload, download, list, and delete objects in S3
"""

import boto3
from botocore.exceptions import ClientError
from typing import List, Optional, Dict
import os


class S3Manager:
    """S3 Bucket Manager"""
    
    def __init__(self, region_name: str = 'us-east-1'):
        self.s3 = boto3.client('s3', region_name=region_name)
        self.region = region_name
    
    def create_bucket(self, bucket_name: str) -> bool:
        """Create an S3 bucket"""
        try:
            if self.region == 'us-east-1':
                # us-east-1 doesn't require LocationConstraint
                self.s3.create_bucket(Bucket=bucket_name)
            else:
                self.s3.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': self.region}
                )
            print(f"Bucket '{bucket_name}' created successfully")
            return True
        except ClientError as e:
            print(f"Error creating bucket: {e}")
            return False
    
    def list_buckets(self) -> List[str]:
        """List all S3 buckets"""
        try:
            response = self.s3.list_buckets()
            return [bucket['Name'] for bucket in response['Buckets']]
        except ClientError as e:
            print(f"Error listing buckets: {e}")
            return []
    
    def upload_file(
        self,
        bucket_name: str,
        local_file_path: str,
        s3_key: Optional[str] = None
    ) -> bool:
        """Upload a file to S3"""
        try:
            if s3_key is None:
                s3_key = os.path.basename(local_file_path)
            
            self.s3.upload_file(local_file_path, bucket_name, s3_key)
            print(f"File '{local_file_path}' uploaded to s3://{bucket_name}/{s3_key}")
            return True
        except ClientError as e:
            print(f"Error uploading file: {e}")
            return False
    
    def download_file(
        self,
        bucket_name: str,
        s3_key: str,
        local_file_path: str
    ) -> bool:
        """Download a file from S3"""
        try:
            self.s3.download_file(bucket_name, s3_key, local_file_path)
            print(f"File downloaded from s3://{bucket_name}/{s3_key} to {local_file_path}")
            return True
        except ClientError as e:
            print(f"Error downloading file: {e}")
            return False
    
    def list_objects(self, bucket_name: str, prefix: str = '') -> List[Dict]:
        """List objects in a bucket"""
        try:
            response = self.s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
            
            objects = []
            if 'Contents' in response:
                for obj in response['Contents']:
                    objects.append({
                        'Key': obj['Key'],
                        'Size': obj['Size'],
                        'LastModified': obj['LastModified'].isoformat()
                    })
            
            return objects
        except ClientError as e:
            print(f"Error listing objects: {e}")
            return []
    
    def delete_object(self, bucket_name: str, s3_key: str) -> bool:
        """Delete an object from S3"""
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=s3_key)
            print(f"Object '{s3_key}' deleted from bucket '{bucket_name}'")
            return True
        except ClientError as e:
            print(f"Error deleting object: {e}")
            return False
    
    def generate_presigned_url(
        self,
        bucket_name: str,
        s3_key: str,
        expiration: int = 3600
    ) -> Optional[str]:
        """Generate a presigned URL for temporary access"""
        try:
            url = self.s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': s3_key},
                ExpiresIn=expiration
            )
            return url
        except ClientError as e:
            print(f"Error generating presigned URL: {e}")
            return None


# Example usage
if __name__ == "__main__":
    s3_manager = S3Manager(region_name='us-east-1')
    
    # List all buckets
    print("=== S3 Buckets ===")
    buckets = s3_manager.list_buckets()
    for bucket in buckets:
        print(f"  - {bucket}")
    
    # Example: Upload a file (uncomment to use)
    # s3_manager.upload_file(
    #     bucket_name='my-bucket',
    #     local_file_path='./example.txt',
    #     s3_key='uploads/example.txt'
    # )
    
    # Example: List objects in a bucket
    # objects = s3_manager.list_objects('my-bucket', prefix='uploads/')
    # for obj in objects:
    #     print(f"  {obj['Key']} - {obj['Size']} bytes")

