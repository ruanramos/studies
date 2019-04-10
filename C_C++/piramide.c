#include <iostream>
#include <math.h>
using namespace std;
 //Compiler version g++ 6.3.0

 int main() {
 	int linhas, contador=1, espacos;
 	scanf("%d", &linhas);
 	espacos = linhas -1;
 	int i =0, j=0, k=0;
 	while(i < linhas){
 		while (k < espacos) {
 			putchar(' ');
 			k++;
 		}
 		
 		while(j < contador) {
 			putchar('*');
 			j++;
 		}
 		i++;
 		putchar('\n');
 		contador+=2;
 		j=0;
 		espacos--;
 		k=0;
 	}
 	return 0;
 }