#Auto-tagging Mulan

1 Find: '&' (0 matches)
    Replace: ''
2 Find: '<' (0 matches)
    Repalce: ''
3 Find: '>' (0 matches)
    Replace: ''
4 Find: '\n\n' (725 matches)
    Replace: '</sp>\0<sp>'
5 Find: '\[(.+?)\]' (770 matches)
    Replace: '<stage>\1</stage>'
6 Find: '(<sp>)(.+):' (539 matches)
    Replace: '\1<speaker>\2</speaker>'
# I saw that the songs were giving me some trouble so I used regex to fix it
7 Find: '(<sp>)<speaker>(<stage>Song)</speaker>' (5 matches)
    Replace: '\1\2'
