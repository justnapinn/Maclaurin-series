
"""
Assume that one is calculating 𝑒^1.2 using the Maclaurin series, thenlet n = number of terms.
(A) Find approximate error and absolute relative approximateof 𝑒^1.2 for each n
(B)Let us assume one wants the absolute relative approximate error to be less than 0.01%, what number n would stop the
approximation?

"""

import math as m
import pandas as pd

def roundError(powerOff,percent):
  sum = 1
  previous = 1
  n = 1
  data = [[1, 1.0, "N/A", "N/A"]]
  while(True):

    fy = (powerOff)**n / m.factorial(n)
    sum += round(fy,4)

    Ea = round((abs(sum - previous)),4)
    previous = sum

    relative_approx = round(((Ea/sum) * 100),4)

    data.append([n+1,sum,Ea,relative_approx])

    if (relative_approx <= percent):
      break;

    n += 1

  return data

columns = [
    "n",  # Number of terms
    "e^1.2",  # Approximation of e^1.2
    "Ea",  # Absolute Error
    "|Ea|%"  # Relative Error (%)
]

# Create a DataFrame from the extracted data with the specified columns
df = pd.DataFrame(roundError(1.2, 0.01), columns=columns)
df.head(10)
