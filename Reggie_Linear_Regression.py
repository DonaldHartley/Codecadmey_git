def get_y(m, b, x):
    return (m*x+b)

def calculate_error(m,b, point):
    x_coor, y_coor = point
    return abs((m*x_coor+b)-y_coor)

def calculate_all_error(m,b,points):
    total_error = 0
    for point in points:
        total_error += calculate_error(m,b,point)
    return total_error

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
possible_ms = [i*.1 for i in range(-100,101)]
possible_bs = [i*.1 for i in range(-200,201)]
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

print (best_m, best_b, smallest_error)
