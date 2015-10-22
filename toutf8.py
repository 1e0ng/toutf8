#!/usr/bin/python
import os
import re
import sys
import shutil

import chardet

des_enc = 'utf-8'

def transcode(file_name, path):
    display_name = file_name[len(path):]
    # Backup
    bk_file = file_name + '.bk'
    shutil.copy(file_name, bk_file)

    # Trans
    fin = open(bk_file)

    succeed = True
    try:
        data = fin.read()
        guess = chardet.detect(data)
        if guess is None or guess['confidence'] < 0.618:
            raise Exception
        src_enc = guess['encoding']
        if src_enc != des_enc:
            src_enc = 'GB18030' if src_enc in ('GB2312', 'GBK') else src_enc
            padding = ' ' * max((60 - len(display_name)), 0)
            print '%s:%s%s ==> %s' % (display_name, padding, src_enc, des_enc)
            data = unicode(data, encoding=src_enc).encode(des_enc)
            fout = open(file_name, 'w')
            fout.write(data)
            fout.close()
    except:
        succeed = False
        print '%s: error --- unknown encoding ---' % display_name

    fin.close()
    os.remove(bk_file)
    return succeed

if __name__ == '__main__':
    nums = len(sys.argv)
    if nums not in (2, 3):
        print 'Usage: toutf8.py path [file_pattern]'
        exit()

    path = os.path.abspath(os.path.dirname(sys.argv[1]))
    pattern = r'.*' if nums == 2 else sys.argv[2]

    print 'Translating files in %s with names in pattern %s to %s ...' % (
            path, pattern, des_enc)
    print '-' * 80

    errors = []
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            if re.search(pattern, filename) and filename != __file__:
                if not transcode(os.path.join(dirpath, filename), path):
                    errors.append(filename)


    print '-' * 80
    if errors:
        print "These files got error:"
        for err in errors:
            print err
        print '-' * 80
    else:
        print "All files have been translated successfully."
