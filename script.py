#from tracemalloc import start
from googletrans import Translator
#from google_trans_new import google_translator
import json
import os
import shutil

translator = Translator()
def save_translation_json(directory, file_name, language):
    print(directory + "/" + file_name)
    file = open(directory + "/" + file_name)
    file_json = json.load(file)
    translation_dict = {}
    for key in file_json:
        if key is None:
            pass
        elif(file_json[key] is None):
            print(key + " None")
            translation_dict[key] = None
        elif(file_json[key] == ""):
            translation_dict[key] = ""
        else:
            print(key, ":", file_json[key])
            if language == "zh":
                translation = translator.translate(text=file_json[key], dest="zh-cn")
            else:
                translation = translator.translate(text=file_json[key], dest=language)
            print(translation.text)
            translation_dict[key] = translation.text
    path_to_dest_file = language + "/" + file_name
    with open(path_to_dest_file , 'w') as json_file:
        json.dump(translation_dict, json_file)
    file.close()

languages = ["zh", "da", "nl", "fi", "fr", "de", "el", "hu", "it", "ja", "ko", "no", "pl", "pt", "ro", "ru", "es", "sv", "tr", "th"]
    
for language in languages:
    # make the directory if it doesn't exist
    if not os.path.exists(language):
        os.mkdir(language)
    for file in os.listdir("./translationresources"):
        # make the directory if it doesn't exist
        if not os.path.exists(language + "/" + str(file)):
            save_translation_json("./translationresources", file, language)
        # print(file[:-5])
    if not os.path.exists(language + ".zip")
        shutil.make_archive(language, 'zip', language)



