#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Entry point
 *
 *
 * Return: 0, always success
 */
int main(void)
{
	pid_t pid;
	int count;

	count = 0;

	while (count < 5)
	{
		count++;
		pid = fork();
		if (pid > 0)
			sleep(1);
		else if (pid == 0)
		{
			printf("Zombie process created, PID: %u\n", getpid());
			exit(0);
		}
		else
			exit(0);
	}

	infinite_while();

	return (0);
}

/**
 * infinite_while - infinite function
 *
 * Return: 0, but will it
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}
