import zipfile
import os
import glob

with zipfile.ZipFile('materials_/Hello.docx', 'r') as zip_ref:
    zip_ref.extractall('temp_docx')

for root, dirs, files in os.walk('temp_docx'):
    for file in files:
        if file.endswith('.xml'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'Hello!11111' in content:
                content = content.replace('Hello!11111', 'Hi, vikikrivich')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print('replaced Hello!11111 with Hi, vikikrivich')

with zipfile.ZipFile('final/Hello_modified.docx', 'w') as zip_ref:
    for root, dirs, files in os.walk('temp_docx'):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, 'temp_docx')
            zip_ref.write(filepath, arcname)
    zip_ref.write('materials_/schedule.png', 'schedule.png')
    print('added schedule.png')

import shutil
shutil.rmtree('temp_docx')

