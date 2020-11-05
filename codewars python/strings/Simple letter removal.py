https://www.codewars.com/kata/5b728f801db5cec7320000c7
def solve(st,k):
    al = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while k > 0 and len(st)>0:
        c = min(st.count(al[i]), k)
        st = st.replace(al[i],'', c)
        k -= c
        i += 1
    return st