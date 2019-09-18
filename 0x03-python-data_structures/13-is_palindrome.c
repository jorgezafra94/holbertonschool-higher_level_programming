#include "lists.h"
/**
 * is_palindrome - says if a singly linked list is a palindrome
 * @head: double pointer that point to the linked list
 * Return: 1 if it is a palindorme or 0 if not
 */
int is_palindrome(listint_t **head)
{
	int count = 0, pos = 0, var = 0, i;
	listint_t *prim = NULL, *seg = NULL;

	if (*head == NULL)
		return (0);
	prim = *head;
	seg = *head;
	for (; prim; count++, prim = prim->next)
		;
	if ((count % 2) == 0)
		var = count / 2;
	else
		var = (count / 2) + 1;
	for (; var > 0; var--)
		seg = seg->next;
	for (i = 0; i < (count / 2); i++)
	{
		pos = i;
		prim = *head;
		while (pos < (count / 2) - 1)
		{
			prim = prim->next;
			pos++;
		}
		if ((prim->n) == (seg->n))
			seg = seg->next;
		else
			return (0);
	}
	return (1);
}
