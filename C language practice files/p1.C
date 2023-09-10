    #include <stdio.h>
void message();
    int main()
    {
message();
return 0;
}
void message()
{
printf("msg\n");
main();


/*	double x = 123828752.66;
        int y = x;
        printf("%d\n", y);
        printf("%f\n", y);
		//123828752
		//0.000000
*/

/*        reverse(1);
    }
    void reverse(int i)
    {
        if (i > 5)
            exit(0);
        printf("%d\n", i);
        return reverse(i++);	// Stack overflow
    }
*/


/*	int x = 3, z= 24+1, y = 2; //correct 24+1 =25 ;no error in this line.

        // int z = x /= y %= 2;
        printf("%d\n", z); //Floating point Exception
*/

/*	int d, a = 1, b = 2;
        d =  a++ +++b;
        printf("%d %d %d", d, a, b); //Syntax error
*/

/*     signed char chr;
       chr = 128;
       printf("%d\n", chr); // -128
*/

/*        unsigned char a = 5, b = 9; // a = 5(00000101), b = 9(00001001) 
    printf("a = %d, b = %d\n", a, b); 
    printf("a&b = %d\n", a&b); // The result is 00000001 
    printf("a|b = %d\n", a|b);  // The result is 00001101 
    printf("a^b = %d\n", a^b); // The result is 00001100 
    printf("~a = %d\n", a = ~a);   // The result is 11111010 
    printf("b<<1 = %d\n", b<<1);  // The result is 00010010  
    printf("b>>1 = %d\n", b>>1);  // The result is 00000100  
*/

/*
	int a = 1, b = 1, d = 1;
	printf("%d, %d, %d", ++a + ++a+a++, a++ + ++b, ++d + d++ + a++); // 15,4,6
*/
    }


