def best_position(points, weights):
  '''
  points: List of tuples, each tuple contains two float elements corresponds to the x and y location of a point.
  weights: List of floats.

  Return: a tuple (x,y) that represents the location of the point that minimizes the weighted distance sum.
  '''

  # find weight median x
  xs = list(zip(list(zip(*points))[0], weights))
  ys = list(zip(list(zip(*points))[1], weights))
  xs.sort(key=lambda x: x[0])
  ys.sort(key=lambda x: x[0])

  w_m_x = 0
  w_m_y = 0
  Sum1 = xs[0][1]
  Sum2 = 0
  
  for i in range(len(xs)-1):
    Sum1 += xs[i+1][1]
    Sum2 += xs[i][1]
    if(Sum1 >= 0.5 and Sum2 < 0.5):
      w_m_x = xs[i+1][0]
      break

  Sum1 = ys[0][1]
  Sum2 = 0
  
  for i in range(len(ys)-1):
    Sum1 += ys[i+1][1]
    Sum2 += ys[i][1]
    if(Sum1 >= 0.5 and Sum2 < 0.5):
      w_m_y = ys[i+1][0]
      break

  return (w_m_x, w_m_y)