input =. fread 'input'

f  =. [: +/\ 0 0 , (,/ ,"0/~ i:1) {~ ' ^ < > v ' i. ]
f2 =. 0 +/\@, _1 1 0j_1 0j1 {~ '<>^v' i. ]  NB. via Fluffum

NB. Part A
echo  # ~. f2 input
NB. Part B
echo  # ~. ,/ f"1 |: _2 ]\ input

exit''
