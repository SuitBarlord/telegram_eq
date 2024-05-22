import json


def read_json(path):
    with open(path, encoding='utf-8', newline='') as f:
        file_content = f.read()
        templates = json.loads(file_content)

    for section, commands in templates.items():
        print(section)
        print('\n'.join(commands))
    
    return templates


# read_json()