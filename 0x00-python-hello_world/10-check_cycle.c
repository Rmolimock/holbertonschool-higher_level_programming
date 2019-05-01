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

	if (list == NULL)
		return (0);
	one = list;
	two = list;
	do {
		if (one->next == NULL || two->next->next == NULL)
			return (0);
		if (two->next == NULL)
			return (0);
		one = one->next;
		if (two->next != NULL)
			two = two->next->next;
	} while (one != two);
	return (1);
}
