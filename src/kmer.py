"""Computing kmers of a string."""


from logging import exception


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']
    """
    if k < 1 or k>len(x):
        raise Exception('stupid k')
    result = [x[i:i+k] for i,_ in enumerate(x) if len(x[i:i+k])==k]
    return result
    ...



def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.
    >>> unique_kmers('agtagtcgagttag', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg', 'cga', 'gag', 'gtt', 'tta']
    """
    intermediate = [i for i in kmer(x,k)]
    result=[]
    for i in intermediate:
        if i not in result:
            result.append(i)
    return result
    # return list(set(kmers(x,k)))
    # return list(dict.fromkeys(kmers(x,k))) #should do it ordered 
    ...
print(unique_kmers('agtagtcgagttag', 3))

def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.
    >>> count_kmers('agtagtcgagttag', 3)
    {'agt': 3, 'tag': 2, 'gta': 1, 'gtc': 1, 'tcg': 1, 'cga': 1, 'gag': 1, 'gtt': 1, 'tta': 1}
    """
    liste_of_ts=[ [i,0] for i in unique_kmers(x,k)]
    liste = kmer(x,k)
    for i,_ in enumerate(liste_of_ts): # the same as for i in liste_of_ts
        for j in liste:
            if j == liste_of_ts[i][0]: # all of the count here is ugly, but ofc it could be done in a dict
                liste_of_ts[i][1] += 1 # which would be eaiser, but then sorting becomes wierd, i think
    # now i want to sort, because extra points and (mainly) i want to do it
    # and insertion sort sholud do the trick
    # note to self: dictionaries are tricky to sort like this
    for i in range(1,len(liste_of_ts)):
        j = i
        while j > 0 and liste_of_ts[j-1][1] < liste_of_ts[j][1]:
            liste_of_ts[j-1], liste_of_ts[j] = liste_of_ts[j], liste_of_ts[j-1]
            j -= 1
    dic={ i:c for i,c in liste_of_ts}
    return dic
    ...
### worst case for count_kmers: if i dont change anything, which would make I faster
    # 1*o(n) to make the first list
    # o(n**2) for kmer list
    # o(n**2) for the list_of_ts
    # and the sort runs n**2 in worst case
    # Total n+3*n**2 which is reducing to n**2 
### best case for count_kmers:
    # 1*o(n) to make the first list
    # o(n**2) for kmer list
    # o(n**2) for the list_of_ts
    # sorting is better as the inner loop condition is only tested once == O(n)
    # but it doesnt change the total outcome 
    # n+2+2*n**2 which is reducing to n**2
