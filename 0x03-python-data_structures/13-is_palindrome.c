#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a
 * palindrome
 * @head: pointer to pointer of head of linked list
 * Return: returns 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reversed, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	reversed = reverse_list(&temp);
	mid = reversed;
	temp = *head;
	while (reversed != NULL)
	{
		if (temp->n != reversed->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}
	reverse_list(&mid);
	return (1);
}

/**
 * reverse_list - reverses the list
 * @head: pointer to pointer of head of list
 * Return: returns pointer to head of new list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next_node, *prev_node = NULL;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev_node;
		prev_node = current;
		current = next_node;
	}
	*head = prev_node;
	return (*head);
}
