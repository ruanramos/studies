#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
	unsigned capacity;
	double *array;
	int top;

} Stack;

Stack* CreateStack(unsigned capacity);
int IsFull(Stack *stack);
int IsEmpty(Stack *stack);
int Push(double element, Stack *stack);
int Pop(Stack *stack);
void PrintStack(Stack *stack);

int Push(double element, Stack *stack) {
	if(IsFull(stack)) {
		// if i want to give error message its this block
		printf("Error: Stack is Full\n");
		return 0;
		// if i want to add capacity to the stack its this block
		/*Stack *tmpStack = CreateStack(stack->capacity * 1.5);
		tmpStack->top = stack->top;
		for (int i = 0; i < stack->top - 1; i++)
		{
			tmpStack->array[i] = stack->array[i];
		}
		stack = tmpStack;
		stack->array[stack->top] = element;
		PrintStack(stack);
		stack->top += 1;
		PrintStack(stack);
		return 1;*/
	}
	stack->array[stack->top] = element;
	stack->top++;
	return 1;
}

int Pop(Stack *stack) {
	if(IsEmpty(stack)) {
		printf("Error: Stack already empty\n");
		return 0;
	}
	stack->top--;
	return 1;
}

int IsFull(Stack *stack) {
	if(stack->top >= stack->capacity) return 1;
	return 0;
}

int IsEmpty(Stack *stack) {
	if(stack->top == 0) return 1;
	return 0;
}

Stack* CreateStack(unsigned capacity) {
	Stack* stack = (Stack*) malloc(sizeof(Stack));
	stack->capacity = capacity;
	stack->top = 0;
	stack->array = (double*) malloc(sizeof(double) * stack->capacity);
	return stack;
}

void PrintStack(Stack *stack) {
	if(IsEmpty(stack)) {
		printf("Stack is empty\n");
		return;
	}
	for (int i = stack->top - 1; i >= 0; i--)
	{
		printf("%lf\n", stack->array[i]);
	}
	printf("----------------------------------------\n");
	return;
}

int main(int argc, char const *argv[])
{
	Stack *stack = CreateStack(3);

	Push(200, stack);
	
	Push(200, stack);
	
	Push(200, stack);
	
	Push(200, stack);
	
	PrintStack(stack);
	return 0;
}
