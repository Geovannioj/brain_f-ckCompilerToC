 #include<stdio.h>

	#define LENGTH 40000

	int main() {

		static char brain[LENGTH];

		static char *pointer;

		pointer = brain;
 	++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;while (*pointer) {++pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++pointer;++*pointer;++*pointer;++*pointer;++pointer;++*pointer;--pointer;--pointer;--pointer;--pointer;--*pointer;}++pointer;++*pointer;++*pointer;putchar(*pointer);++pointer;++*pointer;putchar(*pointer);++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;putchar(*pointer);putchar(*pointer);++*pointer;++*pointer;++*pointer;putchar(*pointer);++pointer;++*pointer;++*pointer;putchar(*pointer);--pointer;--pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;++*pointer;putchar(*pointer);++pointer;putchar(*pointer);++*pointer;++*pointer;++*pointer;putchar(*pointer);--*pointer;--*pointer;--*pointer;--*pointer;--*pointer;--*pointer;putchar(*pointer);--*pointer;--*pointer;--*pointer;--*pointer;--*pointer;--*pointer;--*pointer;--*pointer;putchar(*pointer);++pointer;++*pointer;putchar(*pointer);++pointer;putchar(*pointer); return 0;
 }