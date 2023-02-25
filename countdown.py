import time

def countdown(lst):
    while lst[0] >= 0:
        while lst[1] >= 0:
            while lst[2] > 0:
                lst[2] -= 1
                time.sleep(1)
                print(f"{lst[0]}:{lst[1]}:{lst[2]}")
            lst[1] -= 1
            lst[2] = 60
        lst[0] -= 1
        lst[1] = 59

t = input("Insert time to count down (h:m:s) ")
try:
    t_lst = t.split(":")
    t_lst[0], t_lst[1], t_lst[2] = int(t_lst[0]), int(t_lst[1]), int(t_lst[2])
    countdown(t_lst)
except:
    print("Enter only numbers in the following form (h:m:s) ")
