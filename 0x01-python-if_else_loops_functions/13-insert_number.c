#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to a pointer of head address
 * @number: integer to insert
 *
 * Return: address of new node or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;

	if (*head == NULL || number < current->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}


	while (current->next != NULL)
	{
		if (current->n == number ||
				(current->n < new->n && current->next->n > new->n))
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}

	current->next = new;

	return (new);
}
