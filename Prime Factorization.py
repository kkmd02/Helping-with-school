def is_prime(num):
    '''returns True if the number is prime'''
    if num == 2:
        return True
    i = 2
    while i < num:
        if num / i == int(num/i): #if num has a divisor
            return False
        i += 1
    return True

def prime_factorization(num):
    '''returns the prime factorization of a number as a list'''
    i = 2 #since everything is divisible by 1
    pfactor_list = []
    while i <= num:
        if num / i == int(num/i): #if has no remainders
            pfactor_list.append(i)
            num = num / i
            i = 2
            continue
        i += 1
    return pfactor_list

def least_common_multiple(num1, num2):
    '''return the least common multiple of nim1 and num2'''
    if num1 == num2:
        lcm = num1 #if the same number lcm = num1
    pfactor1_list = prime_factorization(num1) #get prime factorization list
    pfactor2_list = prime_factorization (num2)

    for element in pfactor1_list:
        if element in pfactor2_list:
            pfactor1_list.remove(element) #need to remove common factor pairs but still need them in one list

    masterlist = pfactor1_list + pfactor2_list
    ind_master = 0
    lcm = 1
    while ind_master < len(masterlist):
        lcm *= masterlist[ind_master]
        ind_master += 1
    return lcm

lowest_common_multiple(20, 45) #180

def greatest_common_factor(num1, num2):
    '''return greatest common factor of num1 and num2'''
    if num1 == num2:
        gcf = num1
    pfactor1_list = prime_factorization(num1)
    pfactor2_list = prime_factorization (num2)

    if len(pfactor1_list) > len(pfactor2_list):
        shorter_list = pfactor2_list
        longer_list = pfactor1_list
    else:
        shorter_list = pfactor1_list
        longer_list = pfactor2_list

    master_list = []

    for int in shorter_list:
        if int in longer_list:
            master_list.append(int)
    gcf = 1
    ind_master = 0
    while ind_master < len(master_list):
        gcf *= master_list[ind_master]
        ind_master += 1
    return gcf

greatest_common_factor(200, 10)

L = [2, 3, 4, 5]


