# Documentation of steps for Regex test

1   A) When "dot matches all" is not checked, only the last lines of the whole speech is found. The number of matches are still the same, but not the whole speech is captured. This is due to the fact that unchecking "dot matches all" means that the dot doesn't match hard enters that signal a new line. By checking " dot matches all", we ensure that the whole speech, regardless if it is spannig across several lines, can be captured, which is our goal. Hence, dot matches all should be checked.
    B) \1 is referring to the speeches, including the speaker and the dialogue itself. \2 is referring to the two new line indicators that helps us separate the speeches for easier viewing. We use these expressions, capturing groups, to be able to easier replicate the content of what we are not trying to alter without having the need to type everything out, therefore minimizing time and chance of human error. 
    C) Find: '^(.+?)(\n\n)' (326 matches)
    Replace: <sp>\1</sp>\2

2 Find: '\(.+\)'(119 matches)
    Replace: '<stage>\1</stage>'
    For this step, I didn't check "dot matches all" since I want to be able to capture each individual occurance of the stage directions and turning on "dot matches all" will result in a greedy match of only 1 match, from the first '(' till the last ')', as the dot will also include new line indicators.

3 Find: '[A-Z]+:' (299 matches)
    Replace: '<speaker>\0</speaker>'

4 Find: '^.+' (1 match)
    Replace: '<Maltese>\0</Maltese>'
    I checked "dot matches all" and used this expression to add a root element. I did not have to do anything additional to make the xml well-formed. 

5 Find: '<sp>(<stage>.+</stage>)</sp>' (26 matches)
    Replace: '\1'
