#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int palindrome;
	listint_t *slow = *head, *fast = *head, *prev_slow = *head;
        listint_t *second_half, *mid_node = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	palindrome = 1;

	/*Find the middle of the list*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	/*If the list has an odd number of elements, skip the middle node*/
	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	/*Reverse the second half of the list*/
	second_half = slow;
	prev_slow->next = NULL;  /*break the list into two halves*/

	reverse_list(&second_half);

	/*Compare the first and second halves*/
	palindrome = compare_lists(*head, second_half);

	/*Restore the original list*/
	reverse_list(&second_half);
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}

	return (palindrome);
}

/**
 * reverse_list - reverses a linked list in place
 * @head: pointer to the head of the linked list
 * Return: pointer to the new head of the reversed list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the head of the first linked list
 * @list2: pointer to the head of the second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return 0;
		list1 = list1->next;
		list2 = list2->next;
	}

	/*If one of the lists is longer than the other*/
	if (list1 != NULL || list2 != NULL)
		return (0);

	return (1);
}
