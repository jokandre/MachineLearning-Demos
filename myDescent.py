def yo(message = 'mamacita'):
    print(message)

# hypothetical line, slope as t1 && y-intercept as t0
def h_theta(t0, t1, x):
    return t0 + t1 * x

# total error, j(theta)
def cost_SSE( points, t0, t1 ):
    # Sum Squared Error funtion
    #J = sum([(t0 + t1* points[i, 0] - points[i, 1])**2 for i in range(0 , len(points))])

    totalError = 0 # same as J above

    # Sum Squared distance between line and all data points
    for i in range(0, len(points)):
        x_i = points[i][0] #get x value from dataset
        y_i = points[i][1] #get y value from dataset
        totalError += ( h_theta(t0, t1, x_i)  - y_i)**2
    return totalError# / 2*float(len(points))


def gradient_descent( points, t0, t1, alpha = 0.01, max_iter=10000, ep = 0.01):
    converged = False
    iter = 0

    total_samples = len(points) # total samples in dataseet
    x= points[ : , 0] # get all x values from dataset
    y= points[ : , 1] # get all y values from dataset


    J = sum([(t0 + t1* x[i] - y[i])**2 for i in range(0 , len(points))])

    # Iterate Loop
    while not converged:
        # for each training sample, compute the gradient (d/d_theta j(theta))
        grad0 = 1.0/total_samples * sum([(t0 + t1* x[i] - y[i]) for i in range(total_samples)])
        grad1 = 1.0/total_samples * sum([(t0 + t1* x[i] - y[i]) * x[i] for i in range(total_samples)])

        # update the theta_temp
        temp0 = t0 - alpha * grad0
        temp1 = t1 - alpha * grad1

        # update theta
        t0 = temp0
        t1 = temp1

        # mean squared error
        e = sum( [ (t0 + t1*x[i] - y[i])**2 for i in range(total_samples)] )

        if abs(J - e) <= ep:
            print ('Converged, iterations: ', iter, '!!!')
            converged = True

        J = e   # update error
        iter += 1  # update iter

        if iter == max_iter:
            print ('Max interactions exceeded!')
            converged = True

    return t0,t1, iter
