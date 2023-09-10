#include <stdio.h>

void func(int,int);
int main()
{
int a=10, b=20;
func(a,b);
printf("%d, %d\n",a,b);
}
void func(int a,int b)
{
int *c = &a;
printf("%d, \n",c);
int *d = &b;
printf("%d, \n",*d);
/*
&a = 3;
&b = 4;
printf("%d, %d\n",&a,&b);
*/
}
