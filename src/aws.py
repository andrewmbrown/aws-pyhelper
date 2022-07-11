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

        # Pass config_dict to local storage config
        self.config = config_dict
        # User Dependent Values
        # AWS Access Key ID and Secret Access Key
        self.AWS_ACC_KEY = access_keys['AWS_ACC_KEY']
        self.AWS_SEC_KEY = access_keys['AWS_SEC_KEY']

        # Session to store config states 
        # Allows us to create service clients and resources
        self.session = boto3.Session(
                aws_access_key_id=self.AWS_ACC_KEY,
                aws_secret_access_key=self.AWS_SEC_KEY)

    def init_client_config(self) -> None:
        """
        Initialize our AWS client using config file
        Depending on functionality (from config), init client differently
        """
        # AWS Configuration settings - via YAML file
        # Universal Settings 
        self.AWS_REGION = self.config['AWS_REGION']
        self.functionality = self.config['FUNCTIONALITY']

        if 'IAM' in self.functionality:
            # IAM Settings
            self.IAM_USER_NAME = self.config['IAM_USER_NAME']
            self.IAM_USER_TAGS = self.config['IAM_USER_TAGS']
            self.IAM_USER_TAGS_VALUE = self.config['IAM_USER_TAGS_VALUE']
            self.IAM_USER_TAGS_KEY = self.config['IAM_USER_TAGS_KEY']
            
        if 'EC2' in self.functionality:
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
        
        if 'S3' in self.functionality:
            # S3 Settings
            self.S3_BUCKET_NAME = self.config['S3_BUCKET_NAME']
            self.S3_BUCKET_TAGS = self.config['S3_BUCKET_TAGS']
            self.S3_BUCKET_TAGS_VALUE = self.config['S3_BUCKET_TAGS_VALUE']
            self.S3_BUCKET_TAGS_KEY = self.config['S3_BUCKET_TAGS_KEY']

        if 'CW' in self.functionality:
            # CloudWatch Settings
            self.CW_ALARM_NAME = self.config['CW_ALARM_NAME']
            self.CW_ALARM_DESCRIPTION = self.config['CW_ALARM_DESCRIPTION']
            self.CW_ALARM_METRIC_NAME = self.config['CW_ALARM_METRIC_NAME']
            self.CW_ALARM_NAMESPACE = self.config['CW_ALARM_NAMESPACE']
            self.CW_ALARM_STATISTIC = self.config['CW_ALARM_STATISTIC']
        
        if 'AS' in self.functionality:
            # AutoScaling Settings
            self.WORKER_MINIMUM = self.config['WORKER_MINIMUM']
            self.WORKER_MAXIMUM = self.config['WORKER_MAXIMUM']
    
