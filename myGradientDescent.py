#helper functions for gradient descent


#error funtion = 1/N SUM(Yi - (MXi+B))^2
def compute_error_for_line_given_points(m, b, points):
	totalError = 0
	#for every point in dataset
	for i in range(0, len(points)):
		x = points[i][0] #get x value
		y = points[i][1] #get y value
		#calc distance between point and line
		totalError += (y - (m*x + b))**2
	return totalError / float(len(points))
		
