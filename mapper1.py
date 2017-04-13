#!/usr/bin/env python

import sys
for line in sys.stdin:
        line = line.strip()
        wordcount=0
        words = line.split(',')
        if words[1] != "DATE":
                for word in reversed(words):
                        wordcount+=1
                        if wordcount<6 and word != "" and word[0]!="\"" and word[-1]!="\"":
                                print '%s\t%s' % (word,1)
