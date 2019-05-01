#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 *check_cycle - checks if linked list repeats
 *@list: pointer to head of the list
 *
 *Return: number of nodes in the list
 */
int check_cycle(listint_t *list)
{
	listint_t *one;
	listint_t *two;

	one = list;
	two = list;
	while (two && two->next)
	{
		one = one->next;
		two = two->next->next;
		if (one == two)
			return (1);
	}
	return (0);
}
