def is_odd(n) :
    if n%2 ==1 : return True
    else : return False

def is_even(n) :
    if n%2 == 0: return True
    else : return False

def is_prime(n) :
    for i in range(1, n) :
        if n% i ==0 : return False;

def is_perfect(n) :
    sum=0
    for i in range(1, n) :
        if n % i ==0 :
            sum = sum+i
    if sum == n : return True
    else : return False

def show(num) :
    if is_perfect(num) : print('완전수');
    else : print("완전수 아님")

    if is_even(num):print("짝수")
    else : print("홀수")