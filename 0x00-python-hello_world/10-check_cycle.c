#include "lists.h"

/**
 * check_cycle - Singly list function
 * list: Linked list
 * Return: 1 if there is a cycle and 0 otherwise
 *
 * Description: Function that checks if a singly linked list has a cycle in it.
 **/

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if(!list || !list->next)
		return (0);
	fast = list->next->next;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
