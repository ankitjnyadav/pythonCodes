def rotate(l):
  x = [[l[j][i] for j in reversed(range(len(l)))]for i in range(len(l))]
  return x
