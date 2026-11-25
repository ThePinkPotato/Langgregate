import os
import json
import re

def langCreate(langs, language):
    # langs is the aggregate lang file, as a dict
    # language is the language code you want to generate a file for, ie "en_us" or "de_de"
    
    lang_json = {}
    for key, value in langs.items():
        
        namespace = re.search(r"\.(.+)\.", key).group(1)

        if namespace in lang_json.keys():
            lang_json[namespace][key] = value
        else:
            lang_json[namespace] = {key:value}

    for key in lang_json.keys():
        os.makedirs(os.path.join(os.path.abspath(os.getcwd()), "lang", key), exist_ok=True)
        with open(os.path.join(os.path.abspath(os.getcwd()), "lang", key, (language + ".json")), "w") as lang_file:
            lang_file.write(json.dumps(lang_json[key], indent = 4))