#include "lists.h"

/**
 * check_cycle - This checks if there is a cycle in the linked list
 * @list: The list we are checking
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list)
		return (0);
	temp = list;
	while (temp->next)
	{
		if (!temp->next)
			return (0);

		if (temp->next == list)
		{
			return (1);
		}
		temp = temp->next;
	}
	return (0);
}
