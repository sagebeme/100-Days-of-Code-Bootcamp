#include <stdio.h>

int main(){
	int i, j;
	for (i =1; i<=5; i++){
		printf("%d\n",i);
		for (j=1; j<=3; j++){
			printf("this is i >>%d \nthis is j >> %d\n",i,j);
		}
	}
}
