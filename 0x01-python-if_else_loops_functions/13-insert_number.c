#include <stdlib.h>
#include "lists.h"

/**
 *
 *
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	current = *head;
	if (!current)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	else if (current->n > new->n)
	{
		*head = new;
		new->next = current;
		return (new);
	}
	while (current->next && new->n > current->next->n)
		current = current->next;
	if (current->next)
	{
		new->next = current->next;
		current->next = new;
	}
	else
	{
		current->next = new;
		new->next = NULL;
	}
	return (new);
}
