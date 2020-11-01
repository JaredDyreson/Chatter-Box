# Bauer: Reverse Polish Notation Calculator

Example of RPN:

```
1 2 * 3 4 * *
```

This is the equivalent in regular notation:

```
(1 * 2) * (3 * 4)
```

Numbers are ingested, converted into a double representation and then pushed onto a stack.
This stack is implemented using a regular C array that is where the farthest most element is the top of the stack.

## Operations

### Math

The following mathematical functions are supported:

- SIN
- COS
- TAN
- ASIN (arcsin)
- ACOS (arccos)
- ATAN (arctan)
- SINH (hyperbolic sine)
- COSH (hyperbolic cosine)
- TANH (hyperbolic tangent)
- LOG (base 10 logarithm)
- LN (natural log)
- POW
- EXP
- ADD ('+')
- SUB ('-')
- MUL ('-')
- DIV ('-')
- MOD ('%')
- FLOOR
- SQRT

These operands are considered keywords, therefore they cannot be used for variable assignment.
`ADD` through `MOD` are called using the character adjacent to the operand code name.
If a number is pushed onto the stack and one of these operands are misspelled, then the program will throw a `GARBAGE` operand code, which will then signal an error message and subsequent clearing of the stack.


### Stack

The following stack operations are supported:

- POP
  - Take the top most element off the stack
- PEEK
  - See the top most element of the stack without modifying the stack pointer
- SWAP
  - Swap the top two most elements with each other
- CLONE
  - Make a copy of the stack

### Variable Assignment and Retrieval

The way we set a variable can be seen in the following example:

```
10 =variable
```

Please note that the value of the variable needs to precede the `=variable` assignment. 
The value is pushed onto the stack as it can be used for other operations.
If nothing else comes after the variable assignment, the stack will be cleared.

We can retrieve variables with the symbol `?` as seen here:

```
?variable
```

Where the value of variable is retrieved from a hash table containing a key (variable name) and a subsequent value (value assigned above)

Both of these can be chained together in one line like so:

```
10 =variable
10 =variable_two
?variable ?variable_two * =variable_three
?varible_three
```

Here we assign both `variable` and `variable_two` to contain 10, then we multiply the result and store that value into `variable_three`.

### Scripting

The above can be consolidated into a script written by the end user.
These scripts are plain text files and no special extensions are needed.
Comments are declared **only** by a `#` preceding the line.
The following is an example of a quadratic formula program:

```
# this is a quadratic formula program
# written by Jared Dyreson CSUF 2021
1 =a
-2 =b
-3 =c
# this expression calculates the inside of the square root
?b 2 POW ?a ?c * 4 * - SQRT =square_root
?b -1 * =b
?b ?square_root + ?a 2 * / =solution_one
?b ?square_root - ?a 2 * / =solution_two
```

Answer is `[-1, 3]`.
More features include a keyword `QUIET` where assignment declarations and peeks to the stack are not printed to the console.
Other formulas can be found in the `formulas` directory in this repository.

## Constants

The only constant currently supported is pi which can be called by `PI` and will be pushed to the stack

# Running the Flask Application

First make sure you have this environment variable set correctly to the main python file that runs your web application:

```bash
export FLASK_APP="application"
```

Put this in your shell's configuration file if you want it to persist:

`~/.bashrc`, `~/.zshrc`, etc.


If you want to run the application solely on `localhost`, you can run it with the following command:

```bash
flask run
```

However, if you want to broadcast the application to all devices connected to the network, you can run the following command:

```bash
flask run --host=0.0.0.0
```
