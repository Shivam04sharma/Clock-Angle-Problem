def findAngle(h, m):

	# handle 24-hour notation
	h = h % 12

	# find the position of the hour's hand
	h = (h * 360) // 12 + (m * 360) // (12 * 60)

	# find the position of the minute's hand
	m = (m * 360) // (60)

	# calculate the angle difference
	angle = abs(h - m)

	# consider the shorter angle and return it
	if angle > 180:
		angle = 360 - angle

	return angle
# Clock Angle Problem
if __name__ == '__main__':

	h =5

	m =30

print('Angle=',findAngle(h, m),"degree")


# The idea is to consider the rate of change of the angle in degrees per minute. The hour hand of a 12–hour
# analog clock turns 360° in 12 hours, and the minute hand rotates through 360° in 60 minutes. So, we can
# calculate the angle in degrees of the hour hand minute hand separately and return their difference using
# the following formula:

# Degree(hh) = H×(360/12) + (M×360)/(12×60)
# Degree(mm) = M×(360/60)

# Here, H is the hour, and M is the minutes past the hour. The angle should be in degrees and measured clockwise
# from the 12 o’clock position of the clock. If the angle is greater than 180°, take its difference with 360.