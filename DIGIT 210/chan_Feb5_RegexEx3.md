#Auto-tagging Blithedale file
First I looked for reserved characters ...
1 Find: '&' (0 matches)
    Replace: ''
2 Find: '<' (0 matches)
    Replace: ''
3 Find: '>'(0 matches)
    Replace: ''
Then I cleaned up the whitespaces ...
4 Find: '\n\n+' (931 matches)
    Replace: 'n'
5 Find: '^ +([A-z])'(29 matches)
    Replace: '\1'