/*program to understand the use of fputc() function*/
#include <stdio.h>
#include <stdlib.h>

int main(){
	FILE *fptr;
	int ch;

	if ((fptr=fopen("test","w"))==NULL){
		printf("file doesn't exist");
		exit(1);
	}
	printf("Enter text: ");


	/* Press Ctr+z in DOS and Ctr+d in unix to stop reading character*/
	while((ch=getchar())!=EOF)
		fputc(ch,fptr);
	fclose(fptr);
	return 0;
}
