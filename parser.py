import argparse

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

