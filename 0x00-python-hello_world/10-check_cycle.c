#include "lists.h"
/**
 * check_cycle - checks if the linked list has a loop or not
 * @list: linked list to check
 * Return: 0 if there is no loop or 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	if (!list)
		return (0);
	if ((a = list->next) == NULL)
		return (0);
	if ((b = list->next->next) == NULL)
		return (0);
	for (; a && b; a = a->next, b = b->next->next)
	{
		if (a == b)
			return (1);
	}
	return (0);
}
