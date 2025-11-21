l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input('Enter a number: '))

def rotate_l(l, n):
  m = l[n:]
  del l[n:]
  l = m[:] + l[:]
  return l

print(rotate_l(l, n))