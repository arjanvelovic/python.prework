# Question 1:
def hello_name(user_name):
    print(f'hello_{user_name}!')

# Question 2:
def first_odd():
    for i in range(100):
        if i % 2 == 1:
            print(i)

# Question 3
def max_num_in_list(a_list):
    max = int()
    for i in range(len(a_list)):
        if a_list[i] > max:
            max = a_list[i]
    return max

# Question 4:
def is_leap_year(a_year):
    if a_year % 400 == 0:
        return a_year
    elif a_year % 100 == 0:
        return None
    elif a_year % 4 == 0:
        return a_year
    else:
        return None

# Question 5:
def is_consecutive(a_list):
    first = a_list[0]
    for i in range(len(a_list)):
        if first == a_list[i]:
            first += 1
        else:
            return False
    return True