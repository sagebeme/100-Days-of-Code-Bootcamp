#include <stdio.h>

int main()
{
	char city_name[200];
	printf("What is the name of the city you grew up in? \n");
	scanf("%s", &city_name);
	printf("City name is: %s",city_name);

	char pet_name[200];
	printf("what is the name of your pet? \n");
	scanf("%s",&pet_name);
	printf("pet name is: %s", pet_name);

	printf("the name of your band could be: %s %s", city_name,pet_name);
}
