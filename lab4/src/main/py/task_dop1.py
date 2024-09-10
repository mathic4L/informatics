from my
import yaml
import json



# Чтение YAML файла
with open('input.yaml', 'r') as yaml_file:
    yaml_content = yaml.safe_load(yaml_file)

# Запись в JSON файл
with open('output.json', 'w') as json_file:
    json.dump(yaml_content, json_file, indent=4)