#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to linked list
 * Return: int 1 if present, 0 if absent, null if fail
 */

int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (0);
	while (list->next)
	{
		temp = list;
		while (temp)
		{
			if (temp->next == list)
			{
				return (1);
			}
			temp = temp->next;
		}
		list = list->next;
	}
	free(temp);
	return (0);
}

