#include <stdio.h>

/*
void fun(int *,int *);
int main()
{
int i =5, j=2;
fun(&i,&j);
printf("%d %d\n",i,j);
return 0;
}
void fun(int *i, int *j)
{
*i = *i**i;
*j = *j**j;
}
*/	//output = 25 4

/*
int main()
{
float a =13.5;
float *b,*c;
b = &a;
c = b;
printf("%u %u %u\n",&a,b,c);
printf("%f %f %f %f\n",*(&a),*&a,*b,*c);

return 0;
}
*/	//output = Error

/* 
void fun(int ,int );
int main()
{
int i =23, j=24;
fun(&i,&j);
printf("%d %d\n",i,j);
return 0;
}
void fun(int a, int b)
{
 a= a+a;
 b= b+b;

}
*/	//Error

void fun(int *);
int main()
{
int i=35,*z;
*z = function(&i);
printf("%d\n",*z);
return 0;
}
void fun(int *m)
{
return *m+2;
}
