from collections import namedtuple


UserVisit = namedtuple('UserVisit', ['user_id', 'page', 'user_agent', 'ip'])

UserData = namedtuple('UserData', ['user_id', 'action_type', 'action_name', 'action_value'])
