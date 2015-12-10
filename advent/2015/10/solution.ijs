input =. CRLF -.~ fread 'input'

runlengths =. 1 + [: #;.(_1) 0 , 2 =/\ ]
runvalues =. {~ [: <: +/\@:runlengths
lookandsay =. runlengths ,@,. runvalues

NB. Part A
echo # lookandsay^:40  "."0 input
NB. Part B
echo # lookandsay^:50  "."0 input

exit''
