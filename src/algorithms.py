import numpy as np

SAMPLES_PER_DAY = 24

#  fpgg  |            spgg
#         ______________________________
#       _|
#     _|
#   _|
# _|

# e.g get_samples_step_function(0,100) -> 
# [ 0.    0.69  2.08  4.17  6.94 10.42 (fpgg)
# 15.13 19.85 24.56 29.28 33.99 38.71 43.42 48.14 52.85 57.57 62.28 67.   71.71 76.43 81.14 85.86 90.57 95.29] (spgg)
def get_samples_step_function(start_sample: int, stop_sample: int) -> list[float]:
    overall_growth: int = stop_sample - start_sample

    fpgg: float = overall_growth / 24 # first phase gradual growth
    fpl = np.fromiter((round(start_sample + sum(range(x))/6 * fpgg, 2) for x in range(1,7)), float) # first phase list

    spgg: float = (overall_growth - fpl[-1]) / 19 # second phase gradual growth
    spl = np.fromiter((round(fpl[-1] + x * spgg, 2) for x in range(1,19)), float) # second phase list
    
    return np.concatenate((fpl, spl), axis=0) 

# ______________________________________
# |
# |
# |
# |

# generate_transitional_growth(0,100) ->
#[ 0.    4.17  8.33 12.5  16.67 20.83 25.   29.17 33.33 37.5  41.67 45.83
# 50.   54.17 58.33 62.5  66.67 70.83 75.   79.17 83.33 87.5  91.67 95.83] 
def generate_transitional_growth(start_sample: int, stop_sample: int):
    overall_growth: int = stop_sample - start_sample
    gradual_growth: float = overall_growth / SAMPLES_PER_DAY

    growth_list = [round(start_sample + x * gradual_growth, 2) for x in range(SAMPLES_PER_DAY)]
    return growth_list
