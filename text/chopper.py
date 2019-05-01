#!/usr/bin/python
#! encoding: utf8

# Нарезаем текст "Онегина" на кусочки

import re, codecs
from roman import toRoman
from time import sleep

chapt_num = 6
pat_stanza  = re.compile('\n\n( )*[IVXL]*.*\n\n')
ch1 = codecs.open('chapt_%d'%chapt_num, 'r', 'utf-8').read()
stanzas  = pat_stanza.split(ch1)

print len(stanzas)
"""
for i,s in enumerate(stanzas):
    print "\n==========\nStanza %d\n==========" %(i)
    print len(s)
    print s
"""
stanzas = [s for s in stanzas[1:] if len(s)>1 and s != ' ']

for i,s in enumerate(stanzas):
    print "\n==========\nStanza %d\n==========" %(i)
    """
    tweet = s.split('\n')
    fd = open("../tweets/%d-%02d.txt"%(chapt_num, i), 'w')
    for j in range(6, -1, -1):
        fd.write(tweet[2 * j] + '\n' + tweet[2 * j + 1] + "\\\\\n")
    fd.write("Глава %d, %s"%(chapt_num,toRoman(i + 1)))
    """
    tweet = s.split('\n')
    tweets = []
    tweets += ['\n'.join(tweet[11:14]) + "\\\\\n"]
    tweets += ['\n'.join(tweet[8:11])  + "\\\\\n"]
    tweets += ['\n'.join(tweet[4:8])   + "\\\\\n"]
    tweets += ['\n'.join(tweet[0:4])   + "\\\\\n"]
    for t in tweets:
        if len(t) > 140:
            print "Problem in stanza %d: len = %d"%(i, len(t))
            print t
            sleep(3)
    fd = codecs.open("../tweets/%d-%02d.txt"%(chapt_num, i), 'w', 'utf-8')
    for t in tweets:
        fd.write(t)
    fd.write(u"Глава %d, %s"%(chapt_num, toRoman(i + 1)))
    fd.close

