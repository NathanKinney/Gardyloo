import shutil
import os
import re

# shutil.unpack_archive('unzip_me_for_instructions.zip', 'the_extracted_content', 'zip')

# f = open('the_extracted_content/Instructions.txt', 'r')
#
# lines = f.readlines()
#
# for line in lines:
#     print(line)

test_phrase1 = 'https://drive.google.com/open?id=1tWJBFrSQL06qTZgkohs4t_a5Cu84AheLo'
test_phrase2 = 'https://docs.google.com/document/d/Q-DcxM17nJm_El0aGsNnY7FajaogRviwja/edit'
pattern = r'https://[-?/_=.\w]+'
found1 = re.findall(pattern, test_phrase1)
found2 = re.findall(pattern, test_phrase2)
# print(found1)
# print(found2)

def search(file,pattern=r'https://[-?/_=.\w]+'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern,text)
    else:
        return ''

results = []

for folder, sub_folders, files in os.walk('the_extracted_content'):
    for f in files:
        full_path = folder+'/'+f

        findings = search(full_path)

        if findings != '':
            results.append(findings)
print(len(results))

for match in results:
    print(match.group())

for r in results:
    if r != '':
        print(r.group)
