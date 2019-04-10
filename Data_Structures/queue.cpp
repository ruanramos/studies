#include <stdio.h>
#include <stdlib.h>

typedef struct Queue
{
	unsigned capacity;
	double *array;
	int start;
	int end;
	int size;
} Queue;

Queue* CreateQueue(unsigned capacity);
int Enqueue(Queue *Queue, double element);
int Dequeue(Queue *Queue);
int IsEmpty(Queue *queue);
int IsFull(Queue *queue);

Queue* CreateQueue(unsigned capacity) {
	Queue *queue = (Queue*) malloc(sizeof(Queue));
	queue->capacity = capacity;
	queue->start = -1;
	queue->end = -1;
	queue->size = 0;
	queue->array = (double*) malloc(sizeof(double) * queue->capacity);
	return queue;
}

int Enqueue(Queue *queue, double element) {
	if(!IsFull(queue)) {
		if(IsEmpty(queue)) {
			queue->start = 0;
			queue->end = 1;
			queue->array[queue->start] = element;
		} 
		else {
			queue->array[queue->end] = element;
			queue->end = (queue->end + 1) % (queue->capacity + 1);
		}
		queue->size++;
		
		return 1;
	}
	printf("Error: Queue is full\n");
	return 0;
}

int Dequeue(Queue *queue) {
	if(IsEmpty(queue)) {
		printf("Error: queue already empty\n");
		return 0;
	}
	else if(queue->start == queue->end - 1) {
		queue->start = -1;
		queue->end = -1;
	}
	queue->start = (queue->start + 1) % (queue->capacity);
	queue->size--;
	return 1;
}

int IsEmpty(Queue *queue) {
	if(queue->start == -1 && queue->end == -1) {
		queue->size = 0;
		return 1;
	}
	return 0;
}

int IsFull(Queue *queue) {
	if(queue->size == queue->capacity) {
		return 1;
	}
	return 0;
}

void PrintQueue(Queue *queue) {
	if(IsEmpty(queue)) {
		printf("Queue is empty\n");
		return;
	}
	for (int i = queue->start; i <= queue->end - 1; i++)
	{
		printf("%.2lf ", queue->array[i]);
	}
	printf("\n");
	return;
}

int main(int argc, char const *argv[])
{
	Queue *queue = CreateQueue(3);
	
	PrintQueue(queue);
	printf("end = %d, start = %d\n", queue->end, queue->start);
	Enqueue(queue, 1);
	printf("end = %d, start = %d\n", queue->end, queue->start);
	Enqueue(queue, 1);
	printf("end = %d, start = %d\n", queue->end, queue->start);
	Enqueue(queue, 1);
	printf("end = %d, start = %d\n", queue->end, queue->start);
	Dequeue(queue);
	printf("end = %d, start = %d\n", queue->end, queue->start);
	Dequeue(queue);
	printf("end = %d, start = %d\n", queue->end, queue->start);
	Enqueue(queue, 1);
	printf("end = %d, start = %d\n", queue->end, queue->start);
	PrintQueue(queue);

	return 0;
}