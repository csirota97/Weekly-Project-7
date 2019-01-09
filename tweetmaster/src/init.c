#include "init.h"

int main(int argc, char** argv)
{
//	char user[32];
	char pass[32];
	char c;	

	printf("Username:\t");
//	fgets(user,32,stdin);
	printf("Password:\t");
	fgets(pass,32,stdin);
	
	int i = 0;

char*	user = "test\ntest\ntest\n";

	for (i = 0; user[i] != '\0';i++)
	{
		if (user[i] == '\n')
		{
			int j = i;
			for (j = i+1; user[j] != '\0'; j++)
			{
				user[j-1]=user[j];
			}
			user[j-1] = user[j];
			i--;
		}
	}
	print("%s", user);
//	printf("clear && python3 src/tweet_master.py %s %s", user,pass);

//	system(functionPrint(user, pass));

	return 0;
}


char* functionPrint(char* user, char* pass)
{
	char* function = "clear && python3 src/tweet_master.py";
	strcat(function,user);
	strcat(function, " ");
	strcat(function,pass);

	return function;
}
