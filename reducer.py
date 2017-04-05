#!/usr/bin/env python

from operator import itemgetter
import sys

word1 = None
count = 0
word = None

for line in sys.stdin:
        line = line.strip()
        word,wordcount = line.split('\t',1)
        try:
                wordcount = int(wordcount)
        except ValueError:
                continue
        if word1 == word:
                count += wordcount
        else:
                if word1:
                        print '%s\t%s' % (word1, count)
                count = wordcount
                word1= word
if word1 == word:
        print '%s\t%s' % (word1, count)
