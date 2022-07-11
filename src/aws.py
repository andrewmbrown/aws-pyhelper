import boto3
import json
import yaml
from keys import access_keys
# initialize the boto3 stuff here universally

class AWSClient:
    def __init__(self, config_file) -> None:
        config_dict = {}
        # the following code opens the yaml config file as a stream, and loads it into the config_dict
        # if it fails on the exception catch it just prints errors and returns immediately. 
        with open(config_file, "r") as stream:
            try:
                config_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print("Configuration load failed!")
                print(exc)
                return

        self.config = config_dict  # Pass config_dict to local storage config
        # User Dependent Values
        # AWS Access Key ID and Secret Access Key
        self.AWS_ACC_KEY = access_keys['AWS_ACC_KEY']
        self.AWS_SEC_KEY = access_keys['AWS_SEC_KEY']

    def init_client_config(self, functionality) -> None:
        """
        Initialize our AWS client using config file
        Depending on functionality (from config), init client differently
        """
        # AWS Configuration settings - via YAML file
        # Universal Settings 
        self.AWS_REGION = self.config['AWS_REGION']

        if 'IAM' in functionality:
            # IAM Settings
            self.IAM_USER_NAME = self.config['IAM_USER_NAME']
            self.IAM_USER_TAGS = self.config['IAM_USER_TAGS']
            self.IAM_USER_TAGS_VALUE = self.config['IAM_USER_TAGS_VALUE']
            self.IAM_USER_TAGS_KEY = self.config['IAM_USER_TAGS_KEY']
            
        if 'EC2' in functionality:
            # EC2 Settings
            self.EC2_INSTANCE_TYPE = self.config['EC2_INSTANCE_TYPE']
            self.EC2_AMI_ID = self.config['EC2_AMI_ID']
            self.EC2_KEY_NAME = self.config['EC2_KEY_NAME']
            self.EC2_SECURITY_GROUP = self.config['EC2_SECURITY_GROUP']
            self.EC2_SUBNET_ID = self.config['EC2_SUBNET_ID']
            self.EC2_IP_ADDRESS = self.config['EC2_IP_ADDRESS']
            self.EC2_INSTANCE_NAME = self.config['EC2_INSTANCE_NAME']
            self.EC2_INSTANCE_TAGS = self.config['EC2_INSTANCE_TAGS']
            self.EC2_INSTANCE_TAGS_VALUE = self.config['EC2_INSTANCE_TAGS_VALUE']
            self.EC2_INSTANCE_TAGS_KEY = self.config['EC2_INSTANCE_TAGS_KEY']
        
        if 'S3' in functionality:
            # S3 Settings
            self.S3_BUCKET_NAME = self.config['S3_BUCKET_NAME']
            self.S3_BUCKET_TAGS = self.config['S3_BUCKET_TAGS']
            self.S3_BUCKET_TAGS_VALUE = self.config['S3_BUCKET_TAGS_VALUE']
            self.S3_BUCKET_TAGS_KEY = self.config['S3_BUCKET_TAGS_KEY']

        if 'CW' in functionality:
            # CloudWatch Settings
            self.CW_ALARM_NAME = self.config['CW_ALARM_NAME']
            self.CW_ALARM_DESCRIPTION = self.config['CW_ALARM_DESCRIPTION']
            self.CW_ALARM_METRIC_NAME = self.config['CW_ALARM_METRIC_NAME']
            self.CW_ALARM_NAMESPACE = self.config['CW_ALARM_NAMESPACE']
            self.CW_ALARM_STATISTIC = self.config['CW_ALARM_STATISTIC']
        
        if 'AS' in functionality:
            # AutoScaling Settings
            self.WORKER_MINIMUM = self.config['WORKER_MINIMUM']
            self.WORKER_MAXIMUM = self.config['WORKER_MAXIMUM']
    
