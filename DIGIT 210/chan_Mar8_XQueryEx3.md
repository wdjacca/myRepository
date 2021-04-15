# XQuery Ex3
1 `let $disneySongs := collection('/db/disneySongs/')//xml
         for $d in $disneySongs
         let $songTitle := $d//title/text()
         return $songTitle`

2 `let $disneySongs := collection('/db/disneySongs/')//xml
         for $d in $disneySongs
         let $line := $d//ln => count()
         return $line`

3 `    let $disneySongs := collection('/db/disneySongs/')//xml
         for $d in $disneySongs
         let $song := $d//song
         let $length := $song => string-length()
         return $length`

4 `let $disneySongs := collection('/db/disneySongs/')//xml
         for $d in $disneySongs
         let $song := $d//song
         let $length := $song => string-length()
         order by $length descending
         return $length`

5 `let $disneySongs := collection('/db/disneySongs/')//xml
         for $d in $disneySongs
         let $song := $d//song
         let $length := $song => string-length()
         let $line := $song//ln =>count()
         let $title := $d//title
         order by $length descending
         return concat($title, " has ", $line, " lines with string length of ", $length)`

6, 7 `let $disneySongs := collection('/db/disneySongs/')//xml
    let $songlength :=
    for $d in $disneySongs
        let $song := $d//song
        let $length := $song => string-length()
        let $line := $song//ln =>count()
        let $title := $d//title
        return $length
   let $maxLength := $songlength => max()
    for $d in $disneySongs
        let $song := $d//song
        let $length := $song => string-length()
        let $title := $d//title
        where $length = $maxLength
        return concat("Max: ", $title, " ; ", $maxLength, ".")

`let $disneySongs := collection('/db/disneySongs/')//xml
let $songlength :=
    for $d in $disneySongs
        let $song := $d//song
        let $length := $song => string-length()
        let $line := $song//ln =>count()
        let $title := $d//title
        return $length
let $minLength := $songlength => min()
    for $d in $disneySongs
        let $song := $d//song
        let $length := $song => string-length()
        let $title := $d//title
        where $length = $minLength
        return concat("Min: ", $title, " ; ", $minLength, ".")`
