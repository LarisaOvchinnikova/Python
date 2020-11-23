# https://www.codewars.com/kata/5868812b15f0057e05000001
def tail_swap(strings):
    head1, tail1 = strings[0].split(':')
    head2, tail2 = strings[1].split(':')
    return [head1 + ':' + tail2, head2 + ':' + tail1]