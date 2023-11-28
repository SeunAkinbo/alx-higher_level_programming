#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * insert_node - Inserts number in a specified position in a sorted list
 * @head: Sorted linked list
 * @number: Integer of number to be insert the list
 * Return: The new node on success and NULL otherwise
 *
 * Descriptiion: The function inserts a node in a specified number position
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = NULL;
	listint_t *temp = NULL;
	listint_t *current = *head;

	if (!head)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;

	if (!*head || (*head)->n > number)
	{
		newNode->next = *head;
		return (*head = newNode);
	}
	else
	{
		while (current && current->n < number)
		{
			temp = current;
			current = current->next;
		}

		temp->next = newNode;
		newNode->next = current;
	}
	return (newNode);
}
