"""
AWS Lambda Function Examples
Serverless functions for various use cases
"""

import json
import boto3
from typing import Dict, Any


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Basic Lambda function handler
    """
    try:
        # Extract data from event
        name = event.get('name', 'World')
        message = f"Hello, {name}!"
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': message,
                'event': event
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }


def s3_upload_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda function triggered by S3 upload
    """
    s3 = boto3.client('s3')
    
    try:
        # Process S3 event
        for record in event.get('Records', []):
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            
            # Get object
            response = s3.get_object(Bucket=bucket, Key=key)
            content = response['Body'].read().decode('utf-8')
            
            # Process content (example: count words)
            word_count = len(content.split())
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'bucket': bucket,
                    'key': key,
                    'word_count': word_count
                })
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


def api_gateway_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda function for API Gateway integration
    """
    try:
        # Extract HTTP method and path
        http_method = event.get('httpMethod', 'GET')
        path = event.get('path', '/')
        query_params = event.get('queryStringParameters') or {}
        body = event.get('body', '{}')
        
        # Parse JSON body if present
        if body:
            try:
                body_data = json.loads(body)
            except:
                body_data = {}
        else:
            body_data = {}
        
        # Process request
        if http_method == 'GET':
            response_data = {
                'message': 'GET request processed',
                'path': path,
                'query_params': query_params
            }
        elif http_method == 'POST':
            response_data = {
                'message': 'POST request processed',
                'path': path,
                'body': body_data
            }
        else:
            response_data = {
                'message': f'{http_method} request received',
                'path': path
            }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(response_data)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


def dynamodb_stream_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda function triggered by DynamoDB stream
    """
    try:
        processed_records = []
        
        for record in event.get('Records', []):
            event_name = record['eventName']
            dynamodb = record.get('dynamodb', {})
            
            if event_name == 'INSERT':
                new_image = dynamodb.get('NewImage', {})
                processed_records.append({
                    'action': 'inserted',
                    'data': new_image
                })
            elif event_name == 'MODIFY':
                old_image = dynamodb.get('OldImage', {})
                new_image = dynamodb.get('NewImage', {})
                processed_records.append({
                    'action': 'modified',
                    'old_data': old_image,
                    'new_data': new_image
                })
            elif event_name == 'REMOVE':
                old_image = dynamodb.get('OldImage', {})
                processed_records.append({
                    'action': 'removed',
                    'data': old_image
                })
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'processed_records': len(processed_records),
                'records': processed_records
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


# Example: Image processing Lambda
def image_processor_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Lambda function to process images uploaded to S3
    """
    s3 = boto3.client('s3')
    
    try:
        for record in event.get('Records', []):
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            
            # Check if it's an image
            if not key.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                continue
            
            # Get image metadata
            response = s3.head_object(Bucket=bucket, Key=key)
            size = response['ContentLength']
            content_type = response['ContentType']
            
            # Process image (example: create thumbnail)
            # In production, use PIL/Pillow or similar library
            
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'bucket': bucket,
                    'key': key,
                    'size': size,
                    'content_type': content_type,
                    'processed': True
                })
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

