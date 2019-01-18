def get_y(m, b, x):
    return (m*x+b)

def calculate_error(m,b, point):
    y_point = point[0]
    x_point = point[1]
    y_err = get_y(m,b,x_point)
    return (abs(y_err-y_point))

def calculate_all_error(m,b,points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m,b,point)
    return total_error

def lin_reg(datapoints):
    possible_ms = [i/10 for i in range(-100,101)]
    possible_bs = [i/10 for i in range(-200,201)]
    smallest_error = float("inf")
    best_m = 0
    best_b = 0
    
    for m in possible_ms:
        for b in possible_bs:
            test_err = calculate_all_error(m, b, datapoints)
            if test_err < smallest_error:
                best_m = m
                best_b = b
                smallest_error = test_err
    
    print (str(best_m) +", " + str(best_b) + ", " + str(smallest_error)
