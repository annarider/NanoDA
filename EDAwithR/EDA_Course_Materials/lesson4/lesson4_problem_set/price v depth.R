# Create a simple scatter plot of price vs depth.

# This assignment is not graded and
# will be marked as correct when you submit.

# ENTER YOUR CODE BELOW THIS LINE
#==================================================

ggplot(data = diamonds, aes(x = depth, y = price)) +
    geom_point()

# Change the code to make the transparency of the
# points to be 1/100 of what they are now and mark
# the x-axis every 2 units. See the instructor notes
# for two hints.

ggplot(data = diamonds, aes(x = depth, y = price)) +
    geom_point(alpha = 1/100) +
    scale_x_continuous(breaks = seq(2,80,2))

# Correlation
cor.test(diamonds$depth, diamonds$price)
# -> -0.0106474
