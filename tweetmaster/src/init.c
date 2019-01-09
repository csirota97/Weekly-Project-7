#include "init.h"

int main(int argc, char** argv)
{
	char* user = (char*) malloc(sizeof('a')*32);
	char* pass = (char*) malloc(sizeof('a')*32);

	printf("Username:\t");
	gets(user);
	printf("Password:\t");
	gets(pass);
	

	printf("clear && python3 src/tweet_master.py %s %s\n", user,pass);

	char fun[100] = {};
	
	functionPrint(user, pass, fun);

	system(fun);

	free(user);
	free(pass);

	return 0;
}


char* functionPrint(char* user, char* pass, char* function)
{
	char* func = "clear && python3 src/tweet_master.py ";
	strcat(function,func);
	strcat(function,user);
	strcat(function, " ");
printf("%s\n",function);
	strcat(function,pass);
        printf("%s\n", function);
	return function;
}
