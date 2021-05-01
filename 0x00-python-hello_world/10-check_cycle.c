#include <stdio.h>
#include "lists.h"
/**
 *check_cycle -detects if a singly linked list has a cycle in it
 *@lists: the list to check
 *
 *Return: ) if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tail;

	if (list == NULL)
		return(0);

	head = list;
	tail = list;

	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
			return (1);
	}
	return (0);
}
