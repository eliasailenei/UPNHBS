# Creating two basic solutions 

### Elias Andrew Ailenei

We get the binary value, and we keep splitting it from one number, and
then adding the next number and so on until we reach the last position
of the original string. We then work backwards to get any left out
numbers. We convert these binary values into actual denary values. All
results are stored in a set meaning that we do not get any duplicates.
We then use an algorithm to generate some prime numbers up to N such as
trial or sieve to do some comparisons. We then only keep the numbers
from the set if they are prime numbers by saying is number seen in the
prime list? If so, keep it otherwise discard it.

### Lloyd Prach

There are hidden binary values in each binary. We use a set of
algorithms to find every possible binary value and then remove that
possible value. The program repeats itself until there are no more
values. Once that is done, I will convert it into denary. If there are
any repetition it will be removed. Then we use another algorithm to
filter out non prime numbers. A variable called "N" will ensure that any
prime number value would be smaller. If there are more than six values,
it will generate the last 3 values(biggest) and the first 3
values(smallest). Otherwise, it will just generate the values.

### Caleb Nimo

The issue requires extracting hidden binary values from a binary string
given by repeatedly dividing and adding numbers up to the last position.
Then, the process is reversed to find any value that has been
overlooked. The binary values are then converted to denary and stored in
a set to remove duplicates. To remove irrelevant results, an algorithm
like trial division or the sieve method generates primes up to N.
Numbers that occur in the prime list alone are retained. When there are
more than six values left, the three smallest and three largest are
selected. Otherwise, all of them are returned. This maintains efficiency
with different input sizes.

### Safin Chowdhury

We begin with a binary number and make it smaller by spitting it by the
digits each time, then it proceeds to add to the next once each time,
until the end of the binary string is reached. Then it will begin to go
backwards catching any numbers that might have missed out. Then it
converts all the binary strings into decimal substrings, the results are
stored in a set to avoid duplicates. Then an algorithm is used like a
sieve method or trial division to generate prime numbers up to N.
finally the sets are checked and if the numbers are in the list prime
numbers the number will stay and if not, it will be discarded.

*\
*

# Testing and comparing solutions

In this coursework, the team have developed two solutions to extract
unique prime numbers hidden within a binary string, each using different
data structures and having different time complexities. The first
solution uses sets and lists, where the set ensures uniqueness by
preventing duplicate numbers from appearing in the final list, and the
lists help compute prefix sums to extract decimal values from the binary
substrings. Prime checking in solution 1 is done using trial division,
which is a simple but inefficient method for larger numbers.

The second solution makes use of lists and the Sieve of Eratosthenes,
where a list-based sieve algorithm efficiently precomputes prime numbers
up to a constant limit (usually 10 million since it provides a good
balance between accuracy and speed). This approach reduces the need for
repeatedly checking primes individually. However, while this method is
way faster than trial division, it comes with a trade-off, it takes up a
lot of memory. Some systems might crash with a Memory Overflow error if
they can't handle the sieve's storage requirements.

Another key thing to note is that when $N$ exceeds the sieve limit, the
second solution defaults back to trial division for numbers beyond the
precomputed range, meaning that while smaller primes are found much
faster, the larger numbers still require trial division just like in
solution 1.


When it comes to time complexity, solution 1 runs at
$O(n²\  + \ n\sqrt{}m)$, where $n$ is the length of the binary string
and $m$ is the largest number extracted. Solution 2 (when only using
Sieve) has a complexity of $O(L²\  + \ M\ log\ log\ M\  + \ C)$, where L
is substring extraction, $M$ is the sieve limit, and $C$ is just some
constant overhead. But if the sieve needs to switch back to trial
division, the complexity shifts to
$O(L²\  + \ 10⁷\ log\ log\ 10⁷\  + \ C\sqrt{}m)$, which shows how it
balances speed and memory usage.

At the end of the day, both solutions have their strengths and
weaknesses---solution 1 is simpler and uses less memory but takes
longer, while solution 2 is way faster but can be heavy on system
resources. The best choice depends on how large $N$ is and how much
memory the system must work with.

# Optimising solutions

In this improved version, we build upon our basic solution 2 from Task 1
but keep the core flow of extracting numbers from the binary string
using a Sieve approach. We make the Sieve itself more efficient by only
segmenting and using it when it's needed, plus we bring in a stronger
factorization method (Pollard's Rho) and a Fermat based primality test.
Together, these additions let the program handle a wide range of numeric
sizes far more quickly often within sub second times. First off, numbers
under 10,000 still go through trial division. As we learned from our
original solutions, trial division is perfectly fine when the values are
that small. However, once we jump past 10,000 and up to 10 million, we
turn to a segmented Sieve of Eratosthenes, which sieves only the low and
high range of candidate numbers. This approach cuts down on memory and
avoids time lost sieving from 1 all the way up to the highest candidate.

For numbers that go beyond 10 million, we do a quick Fermat primality
test first. Fermat's little theorem essentially tells us that if $n$ is
prime, then for any integer $a$ not divisible by
$n,a^{n - 1}\ mod\ n = 1$. We check this with a few random 'a' value if
one fails, we know $n$ is composite right away. While this test can
occasionally be fooled by "Carmichael numbers," those cases are rare,
and it's super fast in practice.

If the number still isn't ruled out by the Fermat test, we move on to
Pollard's Rho, which is a randomized factorization algorithm. Instead of
dividing by every number up to $\sqrt{}n$​, Pollard's Rho uses a
polynomial function (commonly $f(x) = \left( x^{2} + c \right)\ mod\ n$
and some advanced math to detect nontrivial factors more quickly. It's
much faster than naive trial division for larger inputs often cutting
the expected runtime dramatically.

Thanks to this combination (segmented Sieve for medium ranges, Fermat +
Pollard's Rho for large ranges), we avoid the worst-case scenarios of
traditional approaches. In Big O terms, we no longer rely purely on
$O(\sqrt{n})$ for large $n$. Pollard's Rho typically finds factors in
around $O(n^{\frac{1}{4}})\ $or better under average conditions, while
the segmented Sieve runs in roughly $O(k\log{\log{k)}}$ for an interval
size $k$. These are big improvements over naive methods, especially for
large inputs.

We've also preserved the prefix array from our previous solution, so
each binary substring can be converted to a decimal in $O(1)$ time. This
avoids re checking and parsing the same substring repeatedly. Overall,
these updates give us a solution that's both more scalable and
consistently faster than our original Solution 2 while still building on
its foundation rather than scrapping it entirely. The only slight
downside is the tiny probabilistic risk of Fermat's test being tricked,
but that's rare enough compared to the major speed gains we get in
return.

# Comparing performance

This new solution is more modular and efficient than the solutions seen
in Task 1 as its focus is to tackle memory usage and reduce excess
calculations for prime checking. Both solutions use sets to store unique
prime numbers and prefix sum arrays to efficiently convert binary
substrings into useable numbers for Python. The main difference between
these solutions, reguarding their data structure, is that this new
solution optimizes performance by using a Boolean array in its segmented
sieve implementation which helps to reduce memory usage and improve
lookup times. As a result, this makes the new solution more memory
efficient when handling large numbers (or even extreme numbers) unlike
the previous solution 2 which relies on a more basic approach on
implementing Sieve which thus leads to it becoming more inefficient when
given large inputs. Furthermore, reguarding algorithmic differences, the
main difference between these solutions is in their primality testing
strategies (see if it's a prime or not algorithms). This new solution
has three stages that it can go through to get the fastest numbers:
brute force stage, look-up stage and random generation stage. Unlike the
previous solution which used trail division for larger numbers, this new
solution uses trail division to brute force small numbers since its less
expensive for our resources to do that and it always comes up faster, we
usually do this with numbers that are less than or equal to 10,000
$O\left( \sqrt{N} \right)$. If we still have more numbers above the
trail threshold, we move onto using segmented sieve which means we only
sieve from where trail has ended to where we need which greatly reduces
memory overhead, we usually give Sieve a 10 million limit
$O(N\log{\log{N)}}$. In the previous solution, Sieve was used for small
numbers and always started from 1 to $N$ which was inefficient. Lastly,
if the numbers are still greater than the Sieve limit, we will use our
combination of Fermat's primality test $O(K\log{N)}$ with Polland Rho's
algorithm $O\left( N^{0.25} \right)$ to quickly find the remaining.
Lastly the main difference between these approaches, reguarding
implementation, is that is new solution follows a more modular design
which helps to improve maintainability and scalability whereas the
previous solution was straightforward but was lacking modularity thus
not being able to handle large cases like this new solution.

Firstly, we do our binary conversion by extracting all possible
substrings and converting them into numbers. Since we use prefix sums,
we can assume that each substring can be computed at $O(1)$ and the
extraction being at $O\left( n^{2} \right)$ for an input of length $n$.
We then move onto trial division, which is used for small numbers under
or equal to 10,000 giving us the worst-case scenario of
$O\left( \sqrt{m} \right)$ per number. We also have segmented sieve
which starts from 10,001 to 10,000,000 which gives the complexity of
$O(m\log{\log{m)}}$ for numbers up to $10^{7}$. If the numbers are still
greater than 10,000,000, we then move to our duo of Polland Rho and
Fermat's test which gives us a complexity of $O\left( m^{0.25} \right)$.
When the N is extremely large, as in the $10^{12}$ area, most candidates
will be checked with Polland Rho. The final worse case scenario for this
solution is:

$$O(n^{2} + m^{0.25})$$


