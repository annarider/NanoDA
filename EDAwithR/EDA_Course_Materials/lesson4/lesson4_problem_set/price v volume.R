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
