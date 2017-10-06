import boto3
from botocore.exceptions import ClientError
from st2actions.runners.pythonrunner import Action


class AwsAction(Action):
    def __init__(self, config):
        super(AwsAction, self).__init__(config)
        self.credentials = {
            'region_name': config.get('aws_region'),
            'aws_access_key_id': config.get('aws_access_key_id'),
            'aws_secret_access_key': config.get('aws_secret_access_key'),
        }

    def run(self, service_name, action, **params):
        cli = boto3.client(service_name, **self.credentials)
        try:
            if params:
                return True, getattr(cli, action)(**params)
            else:
                return True, getattr(cli, action)()
        except ClientError as e:
            return False, e
