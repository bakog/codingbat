# coding=utf-8
"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

make_pi() → [3, 1, 4]
"""
def make_pi():
  return [3,1,4]

def make_pi_2(pi):
    pi=str(pi)
    pi_list= []
    for i in range(len(pi)):
        if i!=1:
            pi_list.append(int(pi[i]))
    return pi_list

print(make_pi_2(3.14))