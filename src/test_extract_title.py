import unittest
from copy_static import extract_title

class TestExtractTitle(unittest.TestCase):
    text ="""
Document Title
==============

***This is a subtitle***

**Author:** *Me*

# Chapter One: Overview

Do you know the way?
"""
    text2 ="""
Document Title
==============

***This is a subtitle***

**Author:** *Me*

Chapter One: Overview

Do you know the way?
"""
    def test_extract_title(self):
        self.assertEqual("Hello", extract_title("# Hello"))

    def test_extract_title_multiline(self):

        self.assertEqual("Chapter One: Overview", extract_title(self.text))

    def test_extract_title_raise_exception(self):
        with self.assertRaises(Exception):
            extract_title("Hello")

    def test_extract_title_raise_exception_multilines(self):
        with self.assertRaises(Exception):
            extract_title(self.text2)

if __name__ == '__main__':
    unittest.main()
