#include<stdio.h>
void printArray(int *a, int n)
{
    for ( int i = 0; i < n; i++)
    {
        printf("%d", a[i]);
    }
    printf("\n");
    
}

int partition(int a[], int low, int high)
{
    int pivot = a[low];
    int i = low + 1;
    int j = high;
    int temp;

    do{
        while(a[i]<=pivot)
        {
            i++;
        }
        while(a[j]>pivot)
        {
            j--;
        }
        if(i<j)
        {
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    }while(i<j);

    temp = a[low];
    a[low] = a[j];
    a[j] = temp;
    return j;
}
void quicksort(int a[], int low, int high)
{
    int pi;
    if (low < high)
        pi = partition(a, low, high);
        quicksort(a, low, pi-1);
        quicksort(a, pi-1, high);

}
int main()
{
    int a[] = {3,5,2,13,12};
    int n = 9;
    printArray(a, n);
    quicksort(a,0,n-1);
    printArray(a,n);
    return 0;
}