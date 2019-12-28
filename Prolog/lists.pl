/* 

List Structure: [HEAD | TAIL]
HEAD --> First element
TAIL --> Elements without the HEAD. Can think of it as if we remove the first element from the list, literally.

examples:

  List                 HEAD          TAIL
 [a,b,c]                a           [b,c]
   []                   -             -
[[o,gato],pula]       [o,gato]     [pula]
[o,[gato,pula]]         o        [[gato,pula]]
[o,[gato,pula],alto]    o        

*/

p([1,2,3]).
p([1,5,3]).
p([o,gato,pulou,[sobre,a,caixa]]).
