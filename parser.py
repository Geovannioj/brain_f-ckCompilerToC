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


def parse():


def main():

  
if __name__ == '__main__':
    main()
