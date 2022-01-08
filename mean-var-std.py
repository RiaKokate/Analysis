import numpy as np

def mean_var_std(list):
  if len(list) != 9:
    print("List must contain nine numbers.")
    return
  array = np.array(list).reshape((3, 3))
  print("Mean")
  print(np.mean(array, axis = 0))
  print(np.mean(array, axis = 1))
  print(np.mean(array))
  print("\nVariance")
  print(np.var(array, axis = 0))
  print(np.var(array, axis = 1))
  print(np.var(array))
  print("\nStandard Deviation")
  print(np.std(array, axis = 0))
  print(np.std(array, axis = 1))
  print(np.std(array))

mean_var_std([0,1,2,3,4,5,6,7,8])
