from jq import jq
from st2actions.runners.pythonrunner import Action


class JqFilterAction(Action):
    def run(self, input_object, input_array, input_string, filter):
        if input_object or input_array:
            return True, jq(filter).transform(input_object or input_array)
        elif input_string:
            return True, jq(filter).transform(text=input_string)
        else:
            return False, None
