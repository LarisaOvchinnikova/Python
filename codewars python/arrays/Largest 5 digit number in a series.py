#https://www.codewars.com/kata/51c8991dee245d7ddf00000e
def solution(digits):
    n = str(digits)
    arr = [int(n[i:i+5]) for i in range(len(n)-4)]
    return max(arr)