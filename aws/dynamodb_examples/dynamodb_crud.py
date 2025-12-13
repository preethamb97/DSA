"""
AWS DynamoDB CRUD Operations - Python SDK Examples
Create, read, update, and delete operations
"""

import boto3
from botocore.exceptions import ClientError
from typing import Dict, List, Optional, Any
from decimal import Decimal


class DynamoDBManager:
    """DynamoDB Table Manager"""
    
    def __init__(self, region_name: str = 'us-east-1'):
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)
        self.client = boto3.client('dynamodb', region_name=region_name)
        self.region = region_name
    
    def create_table(
        self,
        table_name: str,
        partition_key: str,
        sort_key: Optional[str] = None
    ) -> bool:
        """Create a DynamoDB table"""
        try:
            key_schema = [
                {'AttributeName': partition_key, 'KeyType': 'HASH'}
            ]
            attribute_definitions = [
                {'AttributeName': partition_key, 'AttributeType': 'S'}
            ]
            
            if sort_key:
                key_schema.append({'AttributeName': sort_key, 'KeyType': 'RANGE'})
                attribute_definitions.append({'AttributeName': sort_key, 'AttributeType': 'S'})
            
            table = self.dynamodb.create_table(
                TableName=table_name,
                KeySchema=key_schema,
                AttributeDefinitions=attribute_definitions,
                BillingMode='PAY_PER_REQUEST'  # On-demand pricing
            )
            
            table.wait_until_exists()
            print(f"Table '{table_name}' created successfully")
            return True
        except ClientError as e:
            print(f"Error creating table: {e}")
            return False
    
    def put_item(self, table_name: str, item: Dict[str, Any]) -> bool:
        """Insert or update an item"""
        try:
            table = self.dynamodb.Table(table_name)
            table.put_item(Item=item)
            print(f"Item inserted into '{table_name}'")
            return True
        except ClientError as e:
            print(f"Error putting item: {e}")
            return False
    
    def get_item(
        self,
        table_name: str,
        key: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """Get an item by key"""
        try:
            table = self.dynamodb.Table(table_name)
            response = table.get_item(Key=key)
            return response.get('Item')
        except ClientError as e:
            print(f"Error getting item: {e}")
            return None
    
    def update_item(
        self,
        table_name: str,
        key: Dict[str, Any],
        update_expression: str,
        expression_attribute_values: Dict[str, Any]
    ) -> bool:
        """Update an item"""
        try:
            table = self.dynamodb.Table(table_name)
            table.update_item(
                Key=key,
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
            print(f"Item updated in '{table_name}'")
            return True
        except ClientError as e:
            print(f"Error updating item: {e}")
            return False
    
    def delete_item(self, table_name: str, key: Dict[str, Any]) -> bool:
        """Delete an item"""
        try:
            table = self.dynamodb.Table(table_name)
            table.delete_item(Key=key)
            print(f"Item deleted from '{table_name}'")
            return True
        except ClientError as e:
            print(f"Error deleting item: {e}")
            return False
    
    def query(
        self,
        table_name: str,
        key_condition_expression: str,
        expression_attribute_values: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Query items by partition key"""
        try:
            table = self.dynamodb.Table(table_name)
            response = table.query(
                KeyConditionExpression=key_condition_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
            return response.get('Items', [])
        except ClientError as e:
            print(f"Error querying: {e}")
            return []
    
    def scan(self, table_name: str) -> List[Dict[str, Any]]:
        """Scan all items in table (use sparingly)"""
        try:
            table = self.dynamodb.Table(table_name)
            response = table.scan()
            return response.get('Items', [])
        except ClientError as e:
            print(f"Error scanning: {e}")
            return []


# Example usage
if __name__ == "__main__":
    db_manager = DynamoDBManager(region_name='us-east-1')
    
    # Example: Create a table
    # db_manager.create_table(
    #     table_name='Users',
    #     partition_key='user_id',
    #     sort_key='email'
    # )
    
    # Example: Insert an item
    # db_manager.put_item('Users', {
    #     'user_id': '123',
    #     'email': 'user@example.com',
    #     'name': 'John Doe',
    #     'age': 30
    # })
    
    # Example: Get an item
    # item = db_manager.get_item('Users', {'user_id': '123', 'email': 'user@example.com'})
    # print(item)

