"""
Totient maximum
Problem 69: https://projecteuler.net/problem=69

Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of numbers less than n which are relatively prime to n.
For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	                1	    2
3	1,2	                2	    1.5
4	1,3	                2	    2
5	1,2,3,4	            4	    1.25
6	1,5		            2	    3
7	1,2,3,4,5,6	        6	    1.1666...
8	1,3,5,7		        4	    2
9	1,2,4,5,7,8	        6	    1.5
10	1,3,7,9	            4	    2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""


def solution(n: int = 10 ** 6) -> int:
    """
    Returns solution to problem.
    Algorithm:
    Find n/φ(n)for all n ≤ 1,000,000 and return the n that attains maximum
    """

    # Precompute phi using product formula (wikilink below)
    # https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula

    phi = list(range(0, n + 1))
    for number in range(2, n + 1):
        if phi[number] == number:
            phi[number] -= 1
            for multiple in range(number * 2, n + 1, number):
                phi[multiple] = (phi[multiple] // number) * (number - 1)

    answer = 6
    for number in range(10, n + 1):
        if phi[answer] / answer < phi[number] / number:
            answer = number

    return answer


if __name__ == "__main__":
    print(solution())
