# -*- coding: utf-8 -*-
"""
Translate amino acid sequences into possible DNA sequences.
"""

import argparse

parser = argparse.ArgumentParser(description="Translate the amino acid sequence to DNA sequences.")
parser.add_argument("seq", help="Amino acid sequence to be translated.")

args = parser.parse_args()

DNAseq = []

codontable = {
        'I': ['ATA', 'ATC', 'ATT'],
        'M': ['ATG'],
        'T': ['ACA', 'ACC', 'ACG', 'ACT'],
        'N': ['AAC', 'AAT'],
        'K': ['AAA', 'AAG'],
        'S': ['AGC', 'AGT', 'TCA', 'TCC', 'TCG', 'TCT'],
        'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGT'],
        'L': ['CTA', 'CTC', 'CTG', 'CTT', 'TTA', 'TTG'],
        'P': ['CCA', 'CCC', 'CCG', 'CCT'],
        'H': ['CAC', 'CAT'],
        'Q': ['CAA', 'CAG'],
        'V': ['GTA', 'GTC', 'GTG', 'GTT'],
        'A': ['GCA', 'GCC', 'GCG', 'GCT'],
        'D': ['GAC', 'GAT'],
        'E': ['GAA', 'GAG'],
        'G': ['GGA', 'GGC', 'GGG', 'GGT'],
        'F': ['TTC', 'TTT'],
        'Y': ['TAC', 'TAT'],
        'C': ['TGC', 'TGT'],
        'W': ['TGG']
        }


def translate(seq):
    seqlist = []
    if len(seq) == 1:
        for i in range(len(codontable[seq[0]])):
            aminoseq = codontable[seq[0]][i]
            seqlist.append(aminoseq)
        return seqlist
    else:
        seqlist = (translate(seq[:-1]))
        n = len(seqlist)
        for i in range(n):
            for j in range(len(codontable[seq[-1]])):
                aminoseq = seqlist[i] + codontable[seq[-1]][j]
                seqlist.append(aminoseq)
        seqlist = seqlist[n:]
        return seqlist


aminoseq = args.seq
aminoseq = aminoseq.upper()

DNAseq = translate(aminoseq)

for i in range(len(DNAseq)):
    print(DNAseq[i])
