input =. fread 'input'

NB. Part A
echo  +/ ([: (<./ + 2 * +/) 1 */\. ])"1  ([: ".;._1 'x',]);._2 input
NB. Part B
echo  +/ (*/ + 2 * +/ - >./)"1 ([: ".;._1 'x',]);._2 input

exit''
