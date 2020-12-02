# Day 1 Problem

## Description 

### Part One

After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

Your puzzle answer was 926464.

### Part Two

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 65656536.

## My Thoughts

### Part One

Firstly I did it the easy way just to get myself thinking, I sequentially went through the list and added each number to every other number that wasn't itself until we had an answer, this was done by reading the whole file into a list.

I knew there would be a better way and thought that it may be in the reading of the list, by reading the file line by line i could do some comparisons as I went along. so i decided to take each number away from 2020 and store the result in a list. Then on each number i could check the list for the current number, if i found it then it meant that the current number had a value before it that added up to 2020! This value would be (2020 - current number), so I could just return the product of these.

The final step was the issue of having to search a whole list every time I checked a number, which wasnt good. Instead I decided to store the value of (2020 - currentNumber) as the key of a dictionary and try access this each time. I had to catch a KeyError for when it missed, but if it didnt miss then I had my result! I could again just return the product.

This final solution was very quick i think, with the file reading being at worst O(n) and the seach being O(1), making this linear in the worst case and much faster in the average case.

### Part Two

I knew my solution for part two was going to come from my final solution for the previous section, All I did here to change this for having three numbers was instead of just setting the dict value to True, i set it to the two numbers that added up to it as a list for the value.

This process had to be done for each number previous to the current number which makes the solution O(n^2).
