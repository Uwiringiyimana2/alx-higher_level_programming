#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to pointer to the head of lists
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;
	listint_t *current, *temp;

	if (*head == NULL)
		return (1);

	current = *head;
	temp = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;

	while (temp != NULL && *head != NULL)
	{
		if (temp->n == (*head)->n)
		{
			temp = temp->next;
			(*head) = (*head)->next;
		}
		else
			return (0);
	}
	return (1);
}
