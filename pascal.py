"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #17 - Pascal's Triangle (pascal.py)


Author: Paul Thai

Difficulty Level: 6/10

Background: Blaise Pascal is a famous French Mathematician and Philosopher who 
created Pascal's Triangle. Pascal's Triangle is a triangular array composed of 
binomial coefficients that arises in probability theory, combinatorics, and algebra. (Wikipedia)

Prompt: Given the number of rows, return a 2D list of Pascal's Triangle

Test Cases:
Input: rows = 1 ; Output = [[1]]
Input: rows = 2 ; Output = [[1], [1, 1]]
Input: rows = 3 ; Output = [[1], [1, 1], [1, 2, 1]]

"""

from re import L


class Solution:
    def pascalTri(self, rows):
        # type row: int
        # return type: list[list[int]]
        triangle = [[]]
        for p in range(1, rows+1):
            for i in range(0, p):
                print(p)
                print(i)
                if (i == 0):
                    triangle.append([1])
                elif (i == p-1):
                    triangle[p].append(1)
                else:
                    triangle[p].append(triangle[p-1][i-1] + triangle[p-1][i])
                
        triangle.remove([])
        return triangle



def main():
    num = int(input())

    tc1 = Solution()
    ans = tc1.pascalTri(num)
    print(ans)

if __name__ == "__main__":
    main()
