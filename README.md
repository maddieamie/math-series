# LAB - Class 02
## Project: Fibonacci & Lucas Numbers
## Author: Maddie Lewis

## Links and Resources

[First 200 Lucas Numbers](https://r-knott.surrey.ac.uk/Fibonacci/lucas200.html)
[First 200 Fibonacci Numbers](https://miniwebtool.com/list-of-fibonacci-numbers/?number=200)
[Math Is Fun Fibonacci Explanation](https://www.mathsisfun.com/numbers/fibonacci-sequence.html)

## Setup

.venv in gitignore 
Install Pytest & Python3

### How to initialize/run application 

Run pytest in terminal (or python3 -m pytest)
All tests should pass.


### Tests

_How do you run tests?_
After python3 & pytest are installed in your venv, you can run the tests by using the terminal commands for pytest (pytest or python3 -m pytest) 

_Any tests of note?_
The tests run basic checks to make sure the sequences are being calculated properly. The starting and first terms for each sequence should be returned without calculating. 

_Describe any tests that you did not complete, skipped, etc_

I skipped a big number test for the first fibonacci function, because it is using recursion. When I tried to run it before, it just crashed Pytest, so I think it is too inefficient for larger numbers. I did keep the big number test for the lucas function and the fibonacci2 functions, because they run with iteration and seemed able to handle the computational load.

I also did not run any tests that I was expecting to fail with the code running correctly, simply because this was such a small logical problem that it seemed unnecessary. 