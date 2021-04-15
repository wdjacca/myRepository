1 `let $shakespeare := collection('/db/apps/shakespeare/data/')
let $title := $shakespeare//titleStmt/title
return $title` (43 items) 

2 `let $shakespeare := collection('/db/apps/shakespeare/data/')
let $title := $shakespeare//titleStmt/title
let $textonly := $title => data()
return $textonly` (43 items) 

3 `collection('/db/apps/shakespeare/data/')//TEI` (43 items)

4,5,6 `collection('/db/apps/shakespeare/data/')//speaker[text()="Falstaff"]/ancestor::TEI//titleStmt/title => data()` (4 items)

7 `collection('/db/apps/shakespeare/data/')//speaker[text()="Falstaff"]/following-sibling::l/text()`
`collection('/db/apps/shakespeare/data/')//speaker[text()="Falstaff"]/following-sibling::l/text() => count()` (1 item, 473 counts)

8 `let $shakespeare := collection('/db/apps/shakespeare/data/')
let $falstaff := $shakespeare//speaker[text()="Falstaff"]
let $text := $falstaff/following-sibling::l/text()
let $count := count($text)
return $count`

9 `let $shakespeare := collection('/db/apps/shakespeare/data/')
let $falstaff := $shakespeare//speaker[text()="Falstaff"]
let $fplays := $shakespeare//TEI[descendant::speaker="Falstaff"]
for $f in $fplays
let $count := $f//sp[speaker="Falstaff"] => count()
let $title := $f//titleStmt/title/text()
return concat($title,":  ",$count)`