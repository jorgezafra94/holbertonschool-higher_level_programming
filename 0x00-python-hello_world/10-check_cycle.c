#include "lists.h"
/**
 * check_cycle - checks if the linked list has a loop or not
 * @list: linked list to check
 * Return: 0 if there is no loop or 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *a = NULL, *b = NULL;

	if (!list)
		return (0);
	a = list->next;
	if (!a)
		return (0);
	b = list->next->next;
	if (!b)
		return (0);
	for (; b && b->next && a; a = a->next, b = b->next->next)
	{
		if (a == b)
			return (1);
	}
	return (0);
}
