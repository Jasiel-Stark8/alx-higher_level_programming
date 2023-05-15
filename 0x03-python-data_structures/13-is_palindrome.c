#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev, *tmp;
    int is_palin = 1;

    if (!head || !(*head) || !(*head)->next)
        return (1);

    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    prev->next = NULL;
    prev = NULL;

    while (slow)
    {
        tmp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = tmp;
    }

    fast = *head;
    slow = prev;

    while (slow && fast)
    {
        if (slow->n != fast->n)
        {
            is_palin = 0;
            break;
        }
        slow = slow->next;
        fast = fast->next;
    }

    slow = prev;
    prev = NULL;

    while (slow)
    {
        tmp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = tmp;
    }

    (*head)->next = prev;

    return (is_palin);
}
