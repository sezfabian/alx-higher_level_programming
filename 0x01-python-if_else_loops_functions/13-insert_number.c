#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @number: int number to be inserted in list
 * @head: pointer to pointer to first node linked list
 * Return: new list with inserted no, NULL if fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *newn;

	temp = *head;
	newn = malloc(sizeof(listint_t));
	if (newn == NULL)
		return (NULL);

	newn->n = number;
	newn->next = NULL;

	if (temp == NULL || number < (temp->n))
	{
		newn->next = temp;
		*head = newn;
		return newn;
	}
	while (temp)
	{
		if (temp->next == NULL)
		{
			temp->next = newn;
			break;
		}
		if (number < (temp->next->n))
		{
			newn->next = temp->next;
			temp->next = newn;
			break;
		}
		else
			temp = temp->next;
	}
	return (temp);
}

