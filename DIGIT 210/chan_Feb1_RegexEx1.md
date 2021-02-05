# Regex Steps for Converting Movie Data From a tab-separated text file to XML

1 - Find: '&' (315 matches)
    Replace: '&amp;'
2 - Find: '<' (0 matches)
    Replace: 
3 - Find: '>' (0 matches)
    Replace: 
4 - Find: 'title\t.+$' (1 match)
    Replace: '<xml>'
# clk: removing the first row and adding starting root element
5 - Find: '\n(^.+$)' (25094 matches)
    Replace: '<movie>\0</movie>\n'
6 - Find: '(<movie>)(.+?)\t' (25094 matches)
    Replace: '\1<title>\2</title>'
7 - Find:'((19|20)\d{2})' (25346 matches)
# clk: I noticed that if I only did '\d{4}', it would also give me the years that are within the movie titles and I did a quick look and didn't see any of the years before 1900 so I did it this way instead
    Replace: '<date>\1</date>'
7 - Find: '(\d{1,}) min<' (24545 matches)
    Replace: '<time unit="min">\1</time>'
8 - Find:'\t([A-Z|a-z]{2,})' (20240 matches)
    Replace: '<location>\1</location>'
9 - Find: '\t"(.+)"\t' (4824 matches)
    Replace: '<location>\1</location>'
10 - Find: '\n\Z' (1 match)
    Replace: '</xml>'
# clk: Adding closing root element