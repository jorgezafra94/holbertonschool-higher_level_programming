#include "lists.h"
/**
 * is_palindrome - says if a singly linked list is a palindrome
 * @head: double pointer that point to the linked list
 * Return: 1 if it is a palindorme or 0 if not
 */
int is_palindrome(listint_t **head)
{
	int count = 0, pos[9999], j;
	listint_t *prim = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	prim = *head;
	for (; prim; count++, prim = prim->next)
		pos[count] = prim->n;
	for (j = 0; j < count; j++, count--)
	{
		if (pos[j] != pos[count - 1])
			return (0);
	}
	return (1);
}
