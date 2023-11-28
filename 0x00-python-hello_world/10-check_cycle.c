#include "lists.h"
/**
 * check_cycle - it checks whether the singly linked
 * list has a cycle in it
 * @list: pointer to the singly linked list to be checked
 * Return: returns 0 if no cycle and 1 id there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node_1;
	listint_t *node_2;

	if (list == NULL)
		return (0);

	node_1 = list;
	node_2 = list;

	while (node_2 != NULL && node_2->next != NULL)
	{
		node_1 = node_1->next;
		node_2 = node_2->next->next;

		if (node_1 == node_2)
			return (1);
	}
	return (0);
}
