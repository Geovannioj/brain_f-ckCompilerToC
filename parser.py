import click

# brain_f*ck tokens

tokens = {
  ">":"++ptr;",
  "<":"--ptr;",
  "+":"++*ptr;",
  "-":"--*ptr;",
  ".":"putchar(*ptr);",
  ",":"*ptr =getchar();",
  "[": "while (*ptr) {",
  "]": "}"
}

#click handle
@click.command()
@click.argument('firstUserInput', type = click.File('r'))
@click.option('-o', type = click.File('w'))


#parse function
def parse(firstUserInput, outPutFile):

  firstPart = """ #include<stdio.h>
    
    #define LENGTH 40000

    int main() {
        
        static char brain[LENGTH];
        static char *pointer;
        pointer = brain; """

    lastPart = """ return 0; 
    }"""

    middlePart = ""

    brain_fuck_content = firstUserInput.read()
    
    for content_item in brain_fuck_content
        if item in tokens:
            middlePart += tokens[item]



    completeFile = firstPart + middlePart + lastPart
    
    outPutFile.write(completeFile)
    outPutFile.flush


  
if __name__ == '__main__':
    parse()
