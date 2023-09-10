#include<stdio.h>
void check(int);
int prime(int);
int main()
{
printf("Enter the no: \n");
int no;
scanf("%d\n",&no);
check(no);
return 0;
}
void check(int a)
{
if(a > 0)
{
	int x = prime(a);
}
else
{
printf("Enter +ve no\n");
main();
}
}
int prime(int a)
{
printf("%d is  prime no",a);
return 1;
}
