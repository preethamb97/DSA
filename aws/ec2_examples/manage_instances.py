"""
AWS EC2 Management - Python SDK Examples
Create, list, start, stop, and terminate EC2 instances
"""

import boto3
from botocore.exceptions import ClientError
from typing import List, Dict, Optional


class EC2Manager:
    """EC2 Instance Manager"""
    
    def __init__(self, region_name: str = 'us-east-1'):
        self.ec2 = boto3.client('ec2', region_name=region_name)
        self.region = region_name
    
    def list_instances(self, filters: Optional[Dict] = None) -> List[Dict]:
        """
        List all EC2 instances
        """
        try:
            response = self.ec2.describe_instances(Filters=filters or [])
            
            instances = []
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instances.append({
                        'InstanceId': instance['InstanceId'],
                        'InstanceType': instance['InstanceType'],
                        'State': instance['State']['Name'],
                        'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                        'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A'),
                        'LaunchTime': instance['LaunchTime'].isoformat()
                    })
            
            return instances
        except ClientError as e:
            print(f"Error listing instances: {e}")
            return []
    
    def create_instance(
        self,
        image_id: str,
        instance_type: str = 't2.micro',
        key_name: Optional[str] = None,
        security_group_ids: Optional[List[str]] = None,
        user_data: Optional[str] = None
    ) -> Optional[str]:
        """
        Create a new EC2 instance
        """
        try:
            kwargs = {
                'ImageId': image_id,
                'InstanceType': instance_type,
                'MinCount': 1,
                'MaxCount': 1
            }
            
            if key_name:
                kwargs['KeyName'] = key_name
            
            if security_group_ids:
                kwargs['SecurityGroupIds'] = security_group_ids
            
            if user_data:
                kwargs['UserData'] = user_data
            
            response = self.ec2.run_instances(**kwargs)
            instance_id = response['Instances'][0]['InstanceId']
            
            print(f"Creating instance {instance_id}...")
            return instance_id
        except ClientError as e:
            print(f"Error creating instance: {e}")
            return None
    
    def start_instance(self, instance_id: str) -> bool:
        """Start an EC2 instance"""
        try:
            self.ec2.start_instances(InstanceIds=[instance_id])
            print(f"Starting instance {instance_id}...")
            return True
        except ClientError as e:
            print(f"Error starting instance: {e}")
            return False
    
    def stop_instance(self, instance_id: str) -> bool:
        """Stop an EC2 instance"""
        try:
            self.ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Stopping instance {instance_id}...")
            return True
        except ClientError as e:
            print(f"Error stopping instance: {e}")
            return False
    
    def terminate_instance(self, instance_id: str) -> bool:
        """Terminate an EC2 instance"""
        try:
            self.ec2.terminate_instances(InstanceIds=[instance_id])
            print(f"Terminating instance {instance_id}...")
            return True
        except ClientError as e:
            print(f"Error terminating instance: {e}")
            return False
    
    def get_instance_status(self, instance_id: str) -> Optional[str]:
        """Get instance status"""
        try:
            response = self.ec2.describe_instance_status(InstanceIds=[instance_id])
            if response['InstanceStatuses']:
                return response['InstanceStatuses'][0]['InstanceState']['Name']
            return None
        except ClientError as e:
            print(f"Error getting instance status: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize EC2 manager
    ec2_manager = EC2Manager(region_name='us-east-1')
    
    # List all running instances
    print("=== Running Instances ===")
    running_instances = ec2_manager.list_instances(
        filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    for instance in running_instances:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"  Type: {instance['InstanceType']}")
        print(f"  State: {instance['State']}")
        print(f"  Public IP: {instance['PublicIpAddress']}")
        print()
    
    # Note: Uncomment to create instance (requires valid AMI ID and credentials)
    # instance_id = ec2_manager.create_instance(
    #     image_id='ami-0c55b159cbfafe1f0',  # Amazon Linux 2
    #     instance_type='t2.micro',
    #     key_name='my-key-pair'
    # )
    # print(f"Created instance: {instance_id}")

