#include <stdlib.h>
#include "lists.h"

/**
 *is_palindrome - check if values in linked list make palindrome
 *@head: pointer to head of list
 *
 *Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int count = 0, l_tmp = 0, r_tmp = 0, save = 0;
	listint_t *left, *mid, *fast;

	left = mid = fast = *head;
	while (fast && fast->next)
	{
		mid = mid->next;
		fast = fast->next->next;
		count++;
	}
	if (fast)
		mid = mid->next;
	l_tmp = count;
	while (l_tmp)
	{
		count = l_tmp -1;
		while (count)
		{
			left = left->next;
			count--;
		}
		while (r_tmp)
		{
			mid = mid->next;
			r_tmp--;
		}
		if (left->n != mid->n)
			return (0);
		r_tmp = save + 1;
		l_tmp--;
		left = *head;
	}
	return (1);

}
