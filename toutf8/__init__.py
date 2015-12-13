#!/usr/bin/python
import os
import re
import sys
import shutil

import chardet

des_enc = 'utf-8'

def trans_file(file_name):
    bk_file = file_name + '.bk'
    shutil.copy(file_name, bk_file)

    fin = open(bk_file, 'rb')

    succeed = True
    try:
        data = fin.read()
        guess = chardet.detect(data)
        if guess is None or guess['confidence'] < 0.618:
            raise Exception
        src_enc = guess['encoding']
        if src_enc == des_enc:
            raise Exception

        src_enc = 'GB18030' if src_enc in ('GB2312', 'GBK') else src_enc
        padding = ' ' * max((60 - len(file_name)), 0)
        print('%s:%s%s ==> %s' % (file_name, padding, src_enc, des_enc))

        data = data.decode(encoding=src_enc).encode(des_enc)
        fout = open(file_name, 'wb')
        fout.write(data)
        fout.close()

    except Exception as e:
        succeed = False

    finally:
        fin.close()
        os.remove(bk_file)
        return succeed

def main():
    nums = len(sys.argv)
    if nums not in (2, 3):
        print('Usage: toutf8 path [filename_pattern(in regular expression)]')
        exit()

    path = os.path.abspath(sys.argv[1])
    if os.path.isfile(path):
        trans_file(path)
    else:
        pattern = r'.*' if nums == 2 else sys.argv[2]

    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            if re.search(pattern, filename) and filename != __file__:
                trans_file(os.path.join(dirpath, filename))
