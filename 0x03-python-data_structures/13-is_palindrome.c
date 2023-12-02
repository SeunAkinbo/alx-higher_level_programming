#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL, *temp;

    // Find the middle node using the slow-fast pointer technique
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the first half of the list
    while (slow) {
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // Compare the reversed first half with the second half
    slow = prev;
    while (prev) {
        if (prev->n != slow->n) {
            return 0;
        }
        prev = prev->next;
        slow = slow->next;
    }

    // Restore the original list
    slow = prev;
    prev = NULL;
    while (slow) {
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    *head = prev;

    return 1;
}

