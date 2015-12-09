input =. fread 'input'

NB. Part A
echo  +/ (([: -. [: +./@, (_2]\'abcdpqxy') -:"1 _"(_ 1) 2 ]\ ]) *. ([: +./ 2 -:/\ ]) *. (3 <: [: +/ e.&'aeiou'));._2 input

exit ''
