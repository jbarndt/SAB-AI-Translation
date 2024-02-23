import deepl

# input API key here
auth_key = ""

translator = deepl.Translator(auth_key)

# result = translator.translate_text("Hello, world!", target_lang="FR")
# print(result.text)

# print("Source languages:")
# for language in translator.get_source_languages():
#     print(f"{language.name} ({language.code})")  # Example: "German (DE)"

print("Target languages:")
language_list = []
for language in translator.get_target_languages():
    print(f"{language.name} ({language.code})")
    language_list.append(language.code.lower())

print(language_list)

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
    if line.startswith("en: "):
        # print("Line {}: {}".format(count, line.strip()))
        en_ui_element = line.strip().removeprefix("en: ")
        # print(en_ui_element)
        en_ui_elements.append(en_ui_element)

print(ui_element_titles)
print(en_ui_elements)

with open("SAB_interface_deepl.txt", "a", encoding='utf-8') as text_file:
    text_file.write("# Interface Translations\n# Scripture App Builder 11.1.1\n# Created: 16-Feb-2024 11:23:00\n\n[Translations]\n\n")

for i in range(0, len(en_ui_elements)):

    ui_elem_title = ui_element_titles[i]
    ui_elem_en = en_ui_elements[i]
    print(ui_elem_title)
    print("en: " + ui_elem_en)
    with open("SAB_interface_deepl.txt", "a", encoding='utf-8') as text_file:
        text_file.write(ui_elem_title + "\n")
        text_file.write("en: " + ui_elem_en + "\n")

    for lang in language_list:

        target_language = lang  # "PT-BR"

        result = translator.translate_text(ui_elem_en, target_lang=target_language)
        print(target_language.lower() + ": " + result.text)

        with open("SAB_interface_deepl.txt", "a", encoding='utf-8') as text_file:
            text_file.write(target_language.lower() + ": " + result.text + "\n")

    with open("SAB_interface_deepl.txt", "a", encoding='utf-8') as text_file:
        text_file.write("\n")
    print("")
