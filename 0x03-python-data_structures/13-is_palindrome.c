#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a
 * palindrome
 * @head: pointer to pointer of head of linked list
 * Return: returns 0 if not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *prev_slow = NULL;
	listint_t *temp;
	int is_palindrome = 1;

	if ((*head)->next == NULL || *head == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev_slow;
		prev_slow = temp;
	}
	if (fast != NULL)
		slow = slow->next;
	while (slow != NULL)
	{
		if (slow->n != prev_slow->n)
		{
			is_palindrome = 0;
			break;
		}
		slow = slow->next;
		prev_slow = prev_slow->next;
	}
	while (temp != NULL)
	{
		slow = temp->next;
		temp->next = prev_slow;
		prev_slow = temp;
		temp = slow;
	}
	*head = prev_slow;
	return (is_palindrome);
}
