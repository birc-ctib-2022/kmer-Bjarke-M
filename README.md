[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8801801&assignment_repo_type=AssignmentRepo)
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