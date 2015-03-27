# Create a scatterplot of price vs. volume (x * y * z).
# This is a very rough approximation for a diamond's volume.

# Create a new variable for volume in the diamonds data frame.
# This will be useful in a later exercise.

diamonds$volume <- diamonds$x * diamonds$y * diamonds$z


ggplot(data = diamonds, aes(x = volume, y = price)) +
    geom_point()

# Observations

# positive relationship between volume and price
# 20 observations have 0 volumes

# You can find out how many diamonds have 0 volume by using
library(plyr)
count(diamonds$volume == 0).
# The count() function comes with the plyr package.
# Note: You need to run this command in R to unload
# the plyr package.
detach("package:plyr", unload=TRUE)
# The plyr package will conflict with the dplyr package
# in later exercises.

cor.test(diamonds$price, diamonds$volume)
diamonds_volume <- subset(diamonds, volume > 0 & volume <= 800)
cor.test(diamonds_volume$price, diamonds_volume$volume)

# Subset the data to exclude diamonds with a volume
# greater than or equal to 800. Also, exclude diamonds
# with a volume of 0. Adjust the transparency of the
# points and add a linear model to the plot. (See the
# Instructor Notes or look up the documentation of
# geom_smooth() for more details about smoothers.)

# We encourage you to think about this next question and
# to post your thoughts in the discussion section.

# Do you think this would be a useful model to estimate
# the price of diamonds? Why or why not?
