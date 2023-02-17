import json

json_string = '{"first_name": "John", "last_name": "Doe"}'

parsed_json = json.loads(json_string)

print(parsed_json)