# -*- coding: utf-8 -*- 
import numpy as np

class Align(object):
    def __init__(self, absolute_max_string_len=32, label_func=None):
        self.label_func = label_func
        self.absolute_max_string_len = absolute_max_string_len

    def from_file(self, path):
        with open(path, 'r') as f:
            lines = f.readlines()
            print "lines :" + str(lines)
        align = [(int(y[0])/1000, int(y[1])/1000, y[2]) for y in [x.decode('utf-8').strip().split(" ") for x in lines]]
        self.build(align)
        return self

    def from_array(self, align):
        self.build(align)
        return self

    def build(self, align):
        self.align = self.strip(align, ['sp','sil'])
        print self.align
        self.sentence = self.get_sentence(align)
        print self.sentence
        self.label = self.get_label(self.sentence) #text_to_labels
        print self.label
        self.padded_label = self.get_padded_label(self.label)
        print self.padded_label

    def strip(self, align, items):
        return [sub for sub in align if sub[2] not in items]

    def get_sentence(self, align):
        return " ".join([y[-1] for y in align if y[-1] not in ['sp', 'sil']])

    def get_label(self, sentence):
        return self.label_func(sentence)

    def get_padded_label(self, label):        
        padding = np.ones((self.absolute_max_string_len-len(label))) * -1
        labels = np.concatenate((np.array(label), padding), axis=0)
        new_labels = []
        for l in labels:
            new_labels.append(int(l))
        return new_labels
        # return labels

    @property
    def word_length(self):
        return len(self.sentence.split(" "))

    @property
    def sentence_length(self):
        return len(self.sentence)

    @property
    def label_length(self):
        return len(self.label)
