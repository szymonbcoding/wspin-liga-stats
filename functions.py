import time

import numpy as np

FRAMES_PER_SECOND = 24

def get_samples_trapezoidal_growth(start_sample: int, stop_sample: int) -> list[float]:
    overall_growth: int = stop_sample - start_sample

    spgg: float = 2 * overall_growth / (7/4 * FRAMES_PER_SECOND) # second phase gradual growth
    
    fpl = np.fromiter((round(start_sample + sum(range(x))/6 * spgg, 2) for x in range(1,7)), float) # first phase list
    spl = np.fromiter((round(fpl[-1] + x * spgg, 2) for x in range(1,19)), float) # second phase list
    
    return np.concatenate((fpl, spl), axis=0) 

def get_samples_rectangular_growth(start_sample: int, stop_sample: int):
    overall_growth: int = stop_sample - start_sample
    gradual_growth: float = overall_growth / FRAMES_PER_SECOND

    growth_list = np.fromiter((round(start_sample + x * gradual_growth, 2) for x in range(FRAMES_PER_SECOND)), float)
    return growth_list

if __name__ == '__main__':

    a = get_samples_trapezoidal_growth(0,24)
    print(a)
