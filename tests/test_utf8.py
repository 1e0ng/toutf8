# -*- coding: utf-8 -*-
import os
import shutil

import chardet
from unittest import main, TestCase

from toutf8 import trans_file

PATH = os.path.realpath(os.path.dirname(__file__))
class TestToutf8(TestCase):
    def test_gbk(self):
        in_file = os.path.join(PATH, 'in/gbk.txt')
        out_file = os.path.join(PATH, 'out/gbk.txt')

        shutil.copy(in_file, out_file)

        guess = chardet.detect(open(out_file, 'rb').read())
        self.assertTrue(guess['encoding'] in ('GBK', 'GB2312', 'GB18030'))

        self.assertTrue(trans_file(out_file))

        guess = chardet.detect(open(out_file, 'rb').read())
        self.assertEqual(guess['encoding'], 'utf-8')

    def test_gbk(self):
        in_file = os.path.join(PATH, 'in/utf8.txt')
        out_file = os.path.join(PATH, 'out/utf8.txt')

        shutil.copy(in_file, out_file)

        guess = chardet.detect(open(out_file, 'rb').read())
        self.assertEqual(guess['encoding'], 'utf-8')

        self.assertFalse(trans_file(out_file))

        guess = chardet.detect(open(out_file, 'rb').read())
        self.assertEqual(guess['encoding'], 'utf-8')


if __name__ == '__main__':
    main()
