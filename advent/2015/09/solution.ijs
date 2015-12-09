input =. fread 'input'

table     =. 0 2 4 {"1 ;:;._2 input
locations =. ~. , 0 1 {"1 table
dists     =. (+ |:) (".@> 2 {"1 table) (<"1 locations i. 0 1 {"1 table)} (0$~,~#locations)

NB. Part A
echo  <./ ([: +/ dists {~ 2 <@,\ ])"1 ((i.@!) A. i.) #locations
NB. Part B
echo  >./ ([: +/ dists {~ 2 <@,\ ])"1 ((i.@!) A. i.) #locations

exit''
