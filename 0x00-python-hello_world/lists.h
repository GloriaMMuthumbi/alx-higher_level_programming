#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_t - singly linked list structure
 * @n: an integer in the list
 * @next: pointer of the next node in the list
 */
typedef struct listint_t {
	int n;
	struct listint_t* next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
