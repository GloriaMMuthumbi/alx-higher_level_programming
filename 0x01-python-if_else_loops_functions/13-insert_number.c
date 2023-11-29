#include "lists.h"
/**
 * insert_node - inserts a new number into singly linked
 * list
 * @head: pointer to pointer of head of list
 * @number: number to inserted
 * Return: returns new node address or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint *runner = *head, *new, *prev = NULL;

	new = malloc(sizeof(listint));
	if (new == NULL)
		return (NULL);

	new->n = number;

	while (runner && runner->n < number)
		prev = runner, runner = runner->next;

	new->next = runner;

	if (prev == NULL)
		*head = new;
	else
		prev->next = new;

	return (new);
}
