# -*- coding: utf-8 -*-
import os
import sys
import shutil

import chardet
from unittest import main, TestCase

from toutf8 import trans_file
from toutf8 import main as trans

PATH = os.path.abspath(os.path.dirname(__file__))
class TestSingleFile(TestCase):
    def test_gbk(self):
        in_file = os.path.join(PATH, 'in/gbk.txt')
        out_file = os.path.join(PATH, 'out/gbk.txt')

        shutil.copy(in_file, out_file)

        guess = chardet.detect(open(out_file, 'rb').read())
        self.assertTrue(guess['encoding'] in ('GBK', 'GB2312', 'GB18030'))

        self.assertTrue(trans_file(out_file))

        guess = chardet.detect(open(out_file, 'rb').read())
        self.assertEqual(guess['encoding'], 'utf-8')

    def test_utf8(self):
        in_file = os.path.join(PATH, 'in/utf8.txt')
        out_file = os.path.join(PATH, 'out/utf8.txt')

        shutil.copy(in_file, out_file)

        guess = chardet.detect(open(out_file, 'rb').read())
        self.assertEqual(guess['encoding'], 'utf-8')

        self.assertFalse(trans_file(out_file))

        guess = chardet.detect(open(out_file, 'rb').read())
        self.assertEqual(guess['encoding'], 'utf-8')

class TestFolder(TestCase):
    def test_folder(self):
        in_path = os.path.join(PATH, 'in/folder')
        out_path = os.path.join(PATH, 'out/folder')

        shutil.copytree(in_path, out_path)

        sys.argv = [None, out_path]
        trans()

        f = open(os.path.join(out_path, 'gbk1.txt'), 'rb')
        guess = chardet.detect(f.read())
        self.assertEqual(guess['encoding'], 'utf-8')

        f = open(os.path.join(out_path, 'gbk2.txt'), 'rb')
        guess = chardet.detect(f.read())
        self.assertEqual(guess['encoding'], 'utf-8')

        f = open(os.path.join(out_path, 'subfolder/gbk3.txt'), 'rb')
        guess = chardet.detect(f.read())
        self.assertEqual(guess['encoding'], 'utf-8')


if __name__ == '__main__':
    main()
