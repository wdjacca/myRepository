# XQuery Exercise 2
1a. `let $collection := collection('/db/apps/shakespeare/data/')//TEI
return $collection`
b. `let $collection := collection('/db/apps/shakespeare/data/')//TEI
let $speaker := $collection//descendant::speaker => count()
return $speaker` (1 item, 31702 results) 
c. `let $collection := collection('/db/apps/shakespeare/data/')//TEI
let $speaker := $collection//descendant::speaker
let $distinctspkr := distinct-values($speaker)
return $distinctspkr` (966 results)
It worked since I don't see the duplicated speakers now.
d. `let $collection := collection('/db/apps/shakespeare/data/')//TEI
let $speaker := $collection//descendant::speaker
let $distinctspkr := distinct-values($speaker) => count()
return $distinctspkr` (1 item, 966 results)
e.`let $collection := collection('/db/apps/shakespeare/data/')//TEI
for $p in $collection
let $title := $p//titleStmt//title
let $speaker := distinct-values($p//descendant::speaker)=> count()
where $speaker > 50
return $title`

2a. `let $collection := collection('/db/apps/shakespeare/data/')//TEI
for $p in $collection
let $title := $p//titleStmt//title/text()
let $speaker := distinct-values($p//descendant::speaker)=> count()
where $speaker > 50
return $title` 
b. `let $collection := collection('/db/apps/shakespeare/data/')//TEI
for $p in $collection
let $title := $p//titleStmt//title/text()
let $speaker := distinct-values($p//descendant::speaker)=> count()
where $speaker > 50
return  base-uri($p)` 
I see the file path to the specific files that match my criteria. 
c. `let $collection := collection('/db/apps/shakespeare/data/')//TEI
for $p in $collection
let $title := $p//titleStmt//title/text()
let $speaker := distinct-values($p//descendant::speaker)=> count()
where $speaker > 50
return  concat($title, " file path: ", base-uri($p))`