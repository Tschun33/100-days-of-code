
file_template = open("/Users/Stefan/Desktop/100 days of code/mail merging/letter_template/letter_template.txt", "r")
file = file_template.read()
name_file = open("/Users/Stefan/Desktop/100 days of code/mail merging/name_list/name_list.txt")
names = name_file.read().split()

for name in names:
    letter_text = file.replace(f"[name]", f"{name}")
    letter_file = open(f"/Users/Stefan/Desktop/100 days of code/mail merging/letter_to_send/letter_to_{name}.txt", "w")
    letter_file.write(letter_text)
    letter_file.close()

name_file.close()
file_template.close()
