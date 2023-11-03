# Markdown parser.py
The purpose of this project is to practice my string parsing skills and applying thr concepts I learned in programming language paradigms like BNFs and parsing.

When parsed out, I will represent markdown as a parse tree and covnert that parse
tree into html elements for example:
- block -> `<div></div>`
- paragraph -> `<p></p>`
- heading -> `<h1></h1>`
and so on

This will be useful for my blog feature.

## Methodology
I have noticed that markdown more or less follows this ebnf
```
block        ::= heading | paragraph | list | blockquote | codeblock | hr

heading      ::= { '#' } text '\n'

paragraph    ::= inline* '\n'

list         ::= ul | ol

ul           ::= li+

ol           ::= li+

li           ::= ('* ' | '1. ') inline '\n'

blockquote   ::= '> ' block*

codeblock    ::= '```' code '```'

hr           ::= '---' '\n'

inline       ::= em | strong | code | text

em           ::= '*' text '*' | '_' text '_'

strong       ::= '**' text '**' | '__' text '__'

code         ::= '`' text '`'

text         ::= { any text }
```

Now the idea is to create a parser that parses these rules.