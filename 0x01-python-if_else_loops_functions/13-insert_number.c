#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - function in C that inserts a number into
 * a sorted singly linked list
 *
 * @head: head node
 * @number: node number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;

	new_node = malloc(sizeof(listint_t));/*create a box to store a num*/
	if (new_node == NULL)
	{
		return (NULL); /*Allocation failed*/
	}
	new_node->n = number;/*put the num we want to add to the list*/
	new_node->next = NULL;/*connect to a new line*/
	if (*head == NULL || number < (*head)->n)/*chk where to keep d box*/
	{
		/*Insert at the beginning*/
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;/*find the right spot to keep it*/
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		/*either connect in the middle or at the end*/
		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);/*return new num*/
}
