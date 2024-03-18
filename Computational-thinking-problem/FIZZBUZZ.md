YOU 
Do you know about the game FIZZBUZZ works ?

GEMINI
Yes, I do! Fizzbuzz is a fun and educational game that helps people learn about divisibility. Here's how it works:

You can play with a group of people or by yourself.
Players take turns saying numbers in order, starting from 1.
There's a twist! Instead of saying certain numbers, you say a different word according to these rules:
If the number is divisible by 3, say "Fizz" instead.
If the number is divisible by 5, say "Buzz" instead.
If the number is divisible by BOTH 3 and 5 (which means it's divisible by 15), say "Fizzbuzz" instead.
For example, the beginning of a Fizzbuzz round might go: 1, 2, Fizz, 4, Buzz, Fizz, 7...
If a player says the wrong word or hesitates for too long, they might be out depending on the variation of the game.
Overall, Fizzbuzz is a simple but engaging way to practice divisibility and keep your mind sharp

YOU
That's right . Now write me a Python program for the same 

GEMINI
Here's a Python program for Fizzbuzz:

```def fizzbuzz(n):
  """
  This function plays Fizzbuzz up to a given number (n).
  """
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

# Example usage: Play Fizzbuzz up to 100
fizzbuzz(100)```


This program defines a function called fizzbuzz that takes an integer n as input. The function then iterates through numbers from 1 to n using a loop. Inside the loop, it checks for divisibility by 3 and 5 using the modulo operator (%).

If the number is divisible by both 3 and 5, it prints "FizzBuzz".
If it's only divisible by 3, it prints "Fizz".
If it's only divisible by 5, it prints "Buzz".
Otherwise, it prints the number itself.
The program also includes an example usage that calls the fizzbuzz function with the number 100. You can change this number to play Fizzbuzz up to a different limit.



