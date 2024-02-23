# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from google.cloud import translate_v2
import datetime

# put json file in between quotes
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r""

translate_client = translate_v2.Client()

deepl_languages = ["en","bg","cs","da","de","el","en-gb","en-us","es","et","fi","fr","hu","id","it","ja","ko","lt","lv"
    ,"nb","nl","pl","pt","pt-br","pt-pt","ro","ru","sk","sl","sv","tr","uk","zh"]


def detect_language(text: str) -> dict:
    """Detects the text's language."""

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print(f"Text: {text}")
    print("Confidence: {}".format(result["confidence"]))
    print("Language: {}".format(result["language"]))

    return result

# text = "رائع"
# text2 = "ملحمي"

# target = "en"

# output = translate_client.translate([text, text2], target_language=target)

# print(output)

# text3 = "poncho"

# result = translate_client.detect_language(text3)
# print(result)

language_list = translate_client.get_languages()
language_list_no_deepl = []

for language in language_list:
    for key, value in language.items():
        if key == 'language' and value not in deepl_languages:
            # print(key + ", " + value)
            language_list_no_deepl.append(str(value))

print(language_list_no_deepl)

ui_element_titles = []
en_ui_elements = []

# Using readlines()
interface_file = open('SAB_test.txt', 'r', encoding='utf-8')
Lines = interface_file.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    if line.__contains__("$ "):
        ui_element_titles.append(line.strip())
    if line.__contains__("en: ") and not line.__contains__("ben: "):
        if not line.__contains__("en: %,d"):
            # print("Line {}: {}".format(count, line.strip()))
            en_ui_element = line.strip().removeprefix("en: ")
            # print(en_ui_element)
            en_ui_elements.append(en_ui_element)

print(ui_element_titles)
print(en_ui_elements)

tm = datetime.datetime.now()
with open("SAB_interface_gt.txt", "a", encoding='utf-8') as text_file:
    text_file.write("# Interface Translations\n# Scripture App Builder 11.1.1\n# Created: " +
                    tm.strftime("%x").replace("/","-") + " " + tm.strftime("%X") +"\n\n[Translations]\n\n")

for i in range(0, len(en_ui_elements)):

    ui_elem_title = ui_element_titles[i]
    ui_elem_en = en_ui_elements[i]
    print(ui_elem_title)
    print("en: " + ui_elem_en)
    with open("SAB_interface_gt.txt", "a", encoding='utf-8') as text_file:
        text_file.write(ui_elem_title + "\n")
        text_file.write("en: " + ui_elem_en + "\n")

    for lang in language_list_no_deepl:

        target_language = lang

        # result = translator.translate_text(ui_elem_en, target_lang=target_language)
        result = translate_client.translate(ui_elem_en, target_language=target_language)
        translatedText = result['translatedText']
        print(target_language + ": " + translatedText)

        with open("SAB_interface_gt.txt", "a", encoding='utf-8') as text_file:
            text_file.write(target_language + ": " + translatedText + "\n")

    with open("SAB_interface_gt.txt", "a", encoding='utf-8') as text_file:
        text_file.write("\n")
    print("")

