import click

# brain_f*ck tokens

tokens = {
	">":"++pointer;",
  	"<":"--pointer;",
  	"+":"++*pointer;",
  	"-":"--*pointer;",
  	".":"putchar(*pointer);",
  	",":"*pointer =getchar();",
  	"[": "while (*pointer) {",
  	"]": "}"
}

#click handle
@click.command()
@click.argument('input', type = click.File('r'))
@click.option('-o', nargs = 1, type = click.File('w'))


#parse function
def parse(input, o):

	firstPart = """ #include<stdio.h>\n
	#define LENGTH 40000\n
	int main() {\n
	\tstatic char brain[LENGTH];\n
	\tstatic char *pointer;\n
	\tpointer = brain;\n """
  
	lastPart = """ \nreturn 0;\n }"""
	middlePart = "\t"
  
	brain_fuck_content = input.read()

	for content in brain_fuck_content:
		if content in tokens:
			middlePart += tokens[content]
	

	complete = firstPart+middlePart+lastPart
	o.write(complete)

        
if __name__ == '__main__':
    parse()
