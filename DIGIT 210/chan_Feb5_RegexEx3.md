#Auto-tagging Blithedale file
First I looked for reserved characters and cleaning up white spaces ...
1 Find: '&' (0 matches)
    Replace: ''
2 Find: '<' (0 matches)
    Replace: ''
3 Find: '>'(0 matches)
    Replace: ''
4 Find: '\n\n+' (930 matches)
    Replace: '\n\n'
5 Find: '^ +([A-z]{1,}\. ) +' (29 matches)
    Replace: '\1'
Then I started on tagging the contents  ...
6 Find: '\n\n' (930 matches)
    Replace: '</p>\0<p>'
8 Find: '[IVX]{1,}\. ([A-z].+)' (60 matches)
    Replace: '<title>\0</title>'
9 Find: '"(.+?)"' (550 matches)
    Replace: '<quote>\1</quote>'
10 Find: '<p>(<title>)' (29 matches)
    Replace: '\1'
11 Find: '</p>(</title>)' (30 matches)
    Replace: '\1'
12 Find: '(</p>)\n+(<title>)' (28 matches)
    Replace: '\1</chapter>\n\n<chapter>\2'
Then I manually cleaned up my code