import json

import boto3
from st2reactor.sensor.base import PollingSensor


class AwsRunningInstancesSensor(PollingSensor):
    ec2 = None
    logger = None

    def setup(self):
        credentials = {
            'region_name': self.config.get('aws_region'),
            'aws_access_key_id': self.config.get('aws_access_key_id'),
            'aws_secret_access_key': self.config.get('aws_secret_access_key'),
        }
        self.ec2 = boto3.client('ec2', **credentials)
        self.logger = self.sensor_service.get_logger(self.__class__.__name__)

    def poll(self):
        response = self.ec2.describe_instance_status()
        instance_ids = [
            i['InstanceId']
            for i in response['InstanceStatuses'] if i['InstanceState']['Name'] == 'running'
        ]
        payload = {'InstanceIds': instance_ids} if instance_ids else {}
        self.sensor_service.dispatch('leave_them_down_st2.aws_running_instances', payload=payload)

    def cleanup(self):
        """
        Run the sensor cleanup code (if any).
        """
        pass

    def add_trigger(self, trigger):
        """
        Runs when trigger is created
        """
        pass

    def update_trigger(self, trigger):
        """
        Runs when trigger is updated
        """
        pass

    def remove_trigger(self, trigger):
        """
        Runs when trigger is deleted
        """
        pass
