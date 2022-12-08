"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import re
import sys

def primes(number_of_primes):
    if(number_of_primes == 0 or number_of_primes<0):
        raise ValueError('Work with Positive Numbers only')
    else:
        list = []       # result list

        
        for i in range(1000):
            if (isPrime(i) == True):
                list.append(i)
                if(len(list) == number_of_primes):
                    break
                    
            # list += filter(isPrime, range(M - 100, M)) # append prime element of [M - 100, M] to l
            # M += 100                                # increment upper-bound
        return list
    

def isPrime(n):
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None


        
# print result list limited to N elements
# need to generate a list of prime numbers.
# while list. length does not equal number of primes then continue.