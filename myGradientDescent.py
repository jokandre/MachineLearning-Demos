#helper functions for gradient descent
from array import array
#cost funct = squared error funtion = 1/N SUM(Yi - (MXi+B))^2
def compute_error_for_line_given_points(b, m, points):
	totalError = 0
	#for every point in dataset
	for i in range(0, len(points)):
		x = points[i, 0] #get x value
		y = points[i, 1] #get y value
		#calc distance between point and line
		totalError += (y - (m*x + b))**2
	return totalError / float(len(points))

def step_gradient(b_current, m_current, points, learning_rate):
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))

	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		#direction with respect to b and m
		#computing partial derivatices of error function
		b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
		m_gradient += -(2/N) * x * (y - ((m_current *x) + b_current))
	#update b and m values using partial derivatives
	new_b = b_current - (learning_rate * b_gradient)
	new_m = m_current - (learning_rate * m_gradient)

	return [new_b, new_m]

def gradient_descent_runner( points, starting_b, starting_m, learning_rate, num_iterations):
	#starting b and m
	b = starting_b
	m = starting_m
	#gradient descent
	for i in range(num_iterations):
		#update b and m by
		b, m = step_gradient(b, m, points, learning_rate)

	return [b, m]

def yo():
	print('call me maybe')
