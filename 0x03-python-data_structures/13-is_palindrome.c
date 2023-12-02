#include "lists.h"
#include <stdbool.h>

/**
 * reverse_list - Reverses a linked list
 * @head: Linked list
 * Return: returs reversed linked list
 **/

listint_t *reverse_list(listint_t *head)
{
	listint_t *current = head;
	listint_t *before;
	listint_t *after;

	if (current == NULL)
		return (NULL);

	while (current != NULL)
	{
		after = current->next;
		current->next = before;
		before = current;
		current = after;
	}
	return (before);
}


/**
 * is_palindrome - Checks a linked list for palindrome
 * @head: Linked list head
 * Return: 1 for success 0 otherwise
 **/

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = *head, *middle = NULL;

	if (*head == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		middle = slow;
		slow = slow->next;
	}
	slow = reverse_list(slow);
	fast = *head;
	while (slow != NULL)
	{
		if (fast->n != slow->n)
		{
			return (0);
		}
		fast = fast->next;
		slow = slow->next;
	}
	slow = reverse_list(slow);
	if (middle != NULL)
	{
		prev_slow->next = middle;
		middle->next = slow;
	}
	else
		prev_slow->next = slow;

	return (1);
}
