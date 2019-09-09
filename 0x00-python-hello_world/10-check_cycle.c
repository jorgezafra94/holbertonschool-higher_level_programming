#include "lists.h"
/**
 * check_cycle - checks if the linked list has a loop or not
 * @list: linked list to check
 * Return: 0 if there is no loop or 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	a = list->next;
	b = list->next->next;
	while(b->next->next && a->next)
	{
		if (a == b)
			return (1);
		a = a->next;
		b = b->next->next;
	}
	return (0);
}
