#include "lists.h"
/**
 * check_cycle - checks cycles in singly linked lists
 * @list: pointer to the head of the list
 * Return: integer, 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *check1 = list, *check2 = list;

	while (check1 && check2 && check2->next)
	{
		check1 = check1->next;
		check2 = check2->next->next;
		if (check1 == check2)
			return (1);
	}
	return (0);
}
