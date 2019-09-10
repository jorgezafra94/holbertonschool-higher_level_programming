#include "lists.h"
/**
 * insert_node - insert a node with the number value
 * @head: pointer to the list
 * @number: value of the new position
 * Return: a list with the new node inside
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *aux;

	if (head == NULL)
		return (NULL);
	temp = malloc(sizeof(listint_t));
	if (!temp)
		return (NULL);
	temp->n = number;
	if (*head == NULL)
	{
		temp->next = *head;
		*head = temp;
		return (*head);
	}
	aux = *head;
	if (aux->n > temp->n)
	{
		temp->next = aux;
		aux = temp;
		*head = aux;
		return (aux);
	}
	for (aux = *head; aux && aux->next; aux = aux->next)
	{
		if ((aux->next)->n > temp->n)
		{
			temp->next = aux->next;
			aux->next = temp;
			return (aux->next);
		}
	}
	temp->next = NULL;
	aux->next = temp;
	return (aux->next);
}
