import json

import requests
from st2actions.runners.pythonrunner import Action


class SlackPostMessageAction(Action):
    def __init__(self, config):
        super(SlackPostMessageAction, self).__init__(config)
        self.url = config.get('slack_incoming_webhook_url')

    def run(self, text):
        payload = {'text': text}
        response = requests.post(self.url, data={'payload': json.dumps(payload)})
        return True, response
