# K-mers

A k-mer is a substring of length k of some string s. For example, the k-mers for k = 3 of

```
agtagtcg
```

are

```
agt
gta
tag
agt
gtc
tcg
```

**Exercise:** Write a function, `kmers`, which returns a list of all k-mers in a given string for a specific k:

**Exercise:** Often, we're only interested in unique k-mers. Write a function, `unique_kmers`, which only returns unique k-mers.

**Exercise:** Now try to write a function that returns a list of all k-mers paired together with the number of occurrences of that k-mer in the string. Consider it a bonus if you return the list sorted according to the number of occurrences.