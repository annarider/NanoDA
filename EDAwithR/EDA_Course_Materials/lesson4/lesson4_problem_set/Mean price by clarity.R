# Use the function dplyr package
# to create a new data frame containing
# info on diamonds by clarity.

# Name the data frame diamondsByClarity

# The data frame should contain the following
# variables in this order.

#       (1) mean_price
#       (2) median_price
#       (3) min_price
#       (4) max_price
#       (5) n

# where n is the number of diamonds in each
# level of clarity.

suppressMessages(library(ggplot2))
suppressMessages(library(dplyr))
data(diamonds)

# ENTER YOUR CODE BELOW THIS LINE
# ======================================================

names(diamonds)
str(diamonds)
diamondsByClarity <- diamonds %>%
    group_by(clarity) %>%
    summarise(mean_price = mean(as.numeric(price)), median_price = median(as.numeric(price)),
              min_price = min(as.numeric(price)), max_price = max(as.numeric(price)), n = n())

