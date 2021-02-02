1 Find: '&' ( 0 matches)
  Replace: ' '
2 Find: '<' ( 0 matches)
  Replace: ' '
3 Find: '>' ( 0 matches)
  Replace: ' '
4 Find: '^\n^\n' (24 matches)
  Replace: ' '
5 Find: '  ([IXVCL]{1,})\n' (154 matches)
  Replace: '<sonnet number="\1">'
6 Find:'^ +([A-Z|a-z].+$)'
  Replace: '<line>\1</line>'
7 Find: '(</line>)\n\n(<sonnet )' (150 matches)
  Replace: '\1\n</sonnet>\n\2'
