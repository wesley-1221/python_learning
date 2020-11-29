# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Pdf(Document):
    def show(self):

        return 'Show pdf contents!'


class Word(Document):
    def show(self):

        return 'Show word contents!'


pdf_obj = Pdf("联系方式.pdf")
word_obj = Word("联系方式.doc")


objs = [pdf_obj,word_obj]
for o in objs:
    print(o.show())

