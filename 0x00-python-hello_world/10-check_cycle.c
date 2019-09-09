#include "lists.h"
/**
 * check_cycle - checks if the linked list has a loop or not
 * @list: linked list to check
 * Return: 0 if there is no loop or 1 if yes
 */
int check_cycle(listint_t *list)
{
	listint_t *a;

	if (!list)
		return (0);
	a = list->next;
	if (!a)
		return (0);
	list = list->next->next;
	if (!list)
		return (0);
	for (; a && list; a = a->next, list = list->next->next)
	{
		if (a == list)
			return (1);
	}
	return (0);
}
