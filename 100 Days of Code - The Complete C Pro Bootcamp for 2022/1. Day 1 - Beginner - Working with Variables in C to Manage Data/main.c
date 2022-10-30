#include <stdio.h>

int main()
{
	char city_name[100],pet_name[100];

	/**
	 * entering the name of the city
	 */
	printf("Enter the name of the city you were born in:\n");
	scanf("%s",city_name);

	/**
	 * Printing the city_name
	 */

	printf("The city you were born is: %s\n",city_name);

	/**
	 * the name of the your pet code
	 */

	printf("What is the name of your pet? \n");
	scanf("%s",pet_name);
	/**
	 * Printing the pet name
	 */
	printf("your pet name is: %s \n", pet_name);

	/**
	 * printing both the city and pet name
	 * concatinatin both variables
	 */
	printf("your band name can be: %s %s",city_name, pet_name);

	return 0;
}
