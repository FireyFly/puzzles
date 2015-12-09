input =. fread 'input'

NB. Part A
echo  +/ 1 _1 0 {~ '()' i. input
NB. Part B
echo  >: _1 i.~ +/\ 1 _1 0 {~ '()' i. input

exit''
