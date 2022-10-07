# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from kmer import (
    kmer,
    count_kmers,
    unique_kmers
)

def test_kmer():
    #assert kmer('atg',4)=='stupid k'
    assert kmer('agtagtcg',3)==['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']


def test_unique_kmers():
    assert unique_kmers('agtagtcgagttag', 3) == ['agt', 'gta', 'tag', 'gtc', 'tcg', 'cga', 'gag', 'gtt', 'tta']



def test_count_kmers():
    assert count_kmers('agtagtcgagttag', 3) == {'agt': 3, 'tag': 2, 'gta': 1, 'gtc': 1, 'tcg': 1, 'cga': 1, 'gag': 1, 'gtt': 1, 'tta': 1}



