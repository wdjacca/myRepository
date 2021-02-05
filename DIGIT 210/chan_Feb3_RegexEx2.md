1 Find: '&' ( 0 matches)
  Replace: ' '
2 Find: '<' ( 0 matches)
  Replace: ' '
3 Find: '>' ( 0 matches)
  Replace: ' '
4 Find: '^\n^\n' (24 matches)
  Replace: ''
5 Find: '  ([IXVCL]{1,})\n' (154 matches)
  Replace: '<sonnet number="\1">'
6 Find:'^.+$' (2155 matches)
  Replace: '<line>\0</line>'
7 Find: '(>) +(\S)' (2155 matches)
  Replace: '\1\2'
8 Find: '(</line>)(\n+)(<sonnet )' (153 matches)
  Replace: '\1\n</sonnet>\n\3'
9 Find: '</line>\Z' (1 match)
  Replace: '\0</sonnet>'
