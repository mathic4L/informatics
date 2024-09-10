import yaml
import json

import os

read_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'from.yaml')
with open(read_path, 'r') as yaml_file:
    yaml_content = yaml.safe_load(yaml_file)

write_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'to_dop1.json')
with open(write_path, 'w') as json_file:
    json.dump(yaml_content, json_file, indent=4, ensure_ascii=False)