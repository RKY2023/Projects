/* ======= Short Circuiting =======
// Example 1: Short Circuiting
#include <stdio.h>
int main()
{ int a=1, b=1, k=5;
int c = a++ || b-- || k++;
printf(“%d%d”, c, b);
}
// Output : 1,1

// Example 2: Short Circuiting
#include <stdio.h>
int main()
{ int a=0, b=1, k=5;
int c = a++ || --b || k++;
printf(“%d%d”, c, k);
}
// Output : 1,6
*/

/* ======= Comma =======
// Example 1: Comma
#include <stdio.h>
int main()
{ int a=5;
    a=1,2,3;
printf(“%d%d”, a, a);
}
// Output : 1,1

// Example 2: Comma
#include <stdio.h>
int main()
{ int a=10;
int b = (a++ || a++ || a++);
printf(“%d%d”, a, b);
}
// Output : 13,12
executed from left to right and
the value of rightmost expression is returned by the comma operator.
*/

/*


*/