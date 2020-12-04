# Day 2 Problem

## Description 

### Part One

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

Your puzzle answer was 456.

### Part Two

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

## My Thoughts

### Part One

Today's puzzle was a litle bit more spicy, thre input is a little more complex, and each line will have to be manipulated and split, thankfully python is great for this so we were in good shape.

I decided to create a class to handle manipulating each line due to the awkwardness of the data, i had this contain:

- Minimum
- Maximum
- Character to use
- Password

This allowed for an initial naive solution to read in all the items as objects of this class, and then run a simple method to check whether it fit the criteria sequentially. I then optimised this up slightly by reusing a single variable for each object and not creating a list, just incrementing a count at run time if it was valid, rather than storing each one.

It is likely possible to speed up the method of checking if the password fits the policy however i was tired and havent updated this yet, I may revisit later, but for now I decided O(n) int he worst case fit well enough for my day.

### Part Two

This was actually quite simple to implement and sped everything up greatly, it removed the O(n) traversal and allowed just two searched by index checks, working an XOR on these.

Easy peasy, see ya in Day 3 future me. No one else is ever gonna read this.
