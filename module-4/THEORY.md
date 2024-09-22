# Why do we need functions?

- You've come across functions many times so far, but the view on their merits that we have given you has been rather one-sided. You've only invoked functions by using them as tools to make life easier, and to simplify time-consuming and tedious tasks.

- When you want some data to be printed on the console, you use print(). When you want to read the value of a variable, you use input(), coupled with either int() or float().

- You've also made use of some methods, which are in fact functions, but declared in a very specific way.

- Now you'll learn how to write and use your own functions. We'll write several functions together, from the very simple to the rather complex, which will require your focus and attention.

- It often happens that a particular piece of code is repeated many times in your program. It's repeated either literally, or with only a few minor modifications, consisting of the use of other variables in the same algorithm. It also happens that a programmer cannot resist simplifying their work, and begins to clone such pieces of code using the clipboard and copy-paste operations.

- It could end up as greatly frustrating when suddenly it turns out that there was an error in the cloned code. The programmer will have a lot of drudgery to find all the places that need corrections. There's also a high risk of the corrections causing errors.

- We can now define the first condition which can help you decide when to start writing your own functions: if a particular fragment of the code begins to appear in more than one place, consider the possibility of isolating it in the form of a function invoked from the points where the original code was placed before.

- It may happen that the algorithm you're going to implement is so complex that your code begins to grow in an uncontrolled manner, and suddenly you notice that you're not able to navigate through it so easily anymore.

- You can try to cope with the issue by commenting the code extensively, but soon you find that this dramatically worsens your situation ‒ too many comments make the code larger and harder to read. Some say that a well-written function should be viewed entirely in one glance.

## Where do the functions come from?
1 - The first source of functions is the Python interpreter itself. It comes with a large number of functions that are ready to use. You've already used some of them, like print(), input(), and int().

2 - The second source of functions is the Python Standard Library. It's a collection of modules that provide cross-platform implementations of common facilities such as file I/O, networking, and many others. You can use them in your programs without any additional installation.

3 - The third source of functions is the modules you can write yourself. You can create your own functions and use them in your programs. This is the most important source of functions, as it allows you to create your own tools and to simplify your work.

_Commonly used functions in Python_
| Functions | Description |
| --- | --- |
| print() | Prints the given object to the standard output device (screen) or to the text stream file. |
| input() | Reads a line from the standard input device (keyboard) and returns it as a string. |
| int() | Converts the given object to an integer. |
| float() | Converts the given object to a floating-point number. |
| str() | Converts the given object to a string. |
| len() | Returns the number of items in an object. |
| type() | Returns the type of the given object. |
| range() | Generates a sequence of numbers. |
| abs() | Returns the absolute value of a number. |
| sum() | Returns the sum of all items in an iterable. |
| max() | Returns the largest item in an iterable. |
| min() | Returns the smallest item in an iterable. |
| round() | Rounds a number to a given precision. |
| pow() | Raises a number to a given power. |
| sorted() | Returns a sorted list of the specified iterable object. |
| reversed() | Returns a reversed iterator. |
| zip() | Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. |
| enumerate() | Returns an enumerate object. It contains the index and value of all the items in the object it's applied to. |
| filter() | Constructs an iterator from elements of an iterable for which a function returns true. |
| map() | Applies a given function to all the items in an input list. |
| reduce() | Applies a rolling computation to sequential pairs of values in a list. |
