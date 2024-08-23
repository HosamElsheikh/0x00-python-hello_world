#include "lists.h"

/**
 * check_cycle - This checks if there is a cycle in the linked list
 * @list: The list we are checking
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
            return (1);
    }

    return (0);
}
