import os
import hashlib

digest_f = open('ACSC-ISM/README.md', 'w')
digest_f.write('# ISM Revision Digests\n')
digest_f.write('| Revision | MD5       |\n')
digest_f.write('|----------|-----------|\n')

directory = os.fsencode('./ACSC-ISM/')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith('.xml'):
        file_md5 = hashlib.md5(open('./ACSC-ISM/' + filename,'rb').read()).hexdigest()
        print(filename + ' | ' + file_md5)
        digest_f.write('| ' + filename + '  | ' + file_md5 + ' |\n')

digest_f.close()