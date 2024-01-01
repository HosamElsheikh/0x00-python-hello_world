#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if there is a cycle in the list
 *
 * @list: A pointer to the beginning of the list
 *
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fixedList = list;
	listint_t *changedList = list;

	if(list == NULL)
		return(0);
	while(fixedList != NULL && changedList != NULL && changedList != NULL)
	{
		fixedList = fixedList -> next;
		changedList = (changedList -> next) -> next;
		if(changedList == fixedList)
			return(1);
	}
	return(0);
}
