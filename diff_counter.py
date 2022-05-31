#!/usr/bin/env python3
"""example usage:
python diff_counter.py seq1.fas seq2.fas
Both sequences much be in fasta
"""
import sys
seqfi1 = open(sys.argv[1])
seqfi2 = open(sys.argv[2])

seq1 = ''
for lin in seqfi1.readlines():
    if lin.startswith('>'):
        pass
    else:
        seq1 = seq1+lin.strip()

seq2 = ''
for lin in seqfi2.readlines():
    if lin.startswith('>'):
        pass
    else:
        seq2 = seq2+lin.strip()


print("Sequence {f1} is {l1} bp".format(f1=sys.argv[1],l1=len(seq1)))
print("Sequence {f2} is {l2} bp".format(f2=sys.argv[2],l2=len(seq2)))

diff = 0
for i, char in enumerate(seq1):
    if char != seq2[i]:
        diff += 1

print("They differ at {d} sites".format(d=diff))