#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct Node{
	int data;
	Node *next;
} Node;

typedef struct List {
	int size;
	Node *head;
} List;

List* CreateList(int data);
void AddNode(Node *head, int data);
int RemoveNode(int data, Node *list);
void PrintList(Node *list);

List* CreateList(int data) {
	List *list = (List*) malloc(sizeof(List));
	Node *node = (Node*) malloc(sizeof(Node));
	node->data = data;
	node->next = NULL;
	list->size = 1;
	list->head = node;
	// next = NULL
	return list;
}

void AddNode(List *list, int data) {
	Node *node = (Node*) malloc(sizeof(Node));
	node->data = data;
	while(list->head->next != NULL) {
		list->head = list->head->next;
	}
	list->head->next = node;
	list->size++;
}

int RemoveNode(int data, Node *list) {
	/*Node *tmp = (Node*) malloc(sizeof(Node));
	tmp = list;
	if(list->data == data) {
		list = list->next;
		return 1;
	}
	if(list->next == NULL) {
		printf("Error: couldnt find element inside the list\n");
		return 0;
	}
	while(tmp->next->data != data) {
		if(tmp->next->next == NULL) {
			printf("Error: couldnt find element inside the list\n");
			return 0;
		}
		// tmp so i dont change the list pointer
		tmp = tmp->next;
	}
	tmp->next = tmp->next->next;
	return 1;*/
	return 0;
}

void PrintList(List *list) {
	for (int i = 0; i < list->size; i++)
	{
		printf("Endereço: %p\nData: %d\nNext: %p\n", list->head, list->head->data, list->head->next);
		list->head = list->head->next;
	}
}

int main(int argc, char const *argv[])
{
	List *list = CreateList(3);
	
	AddNode(list, 5);

	AddNode(list, 3);
	AddNode(list, 7);
	AddNode(list, 10);
	printf("%d", list->size);
	AddNode(list, 1);
	AddNode(list, 2);
	printf("%d", list->size);
	PrintList(list);
	return 0;
}