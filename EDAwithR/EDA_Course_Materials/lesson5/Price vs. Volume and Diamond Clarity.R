# Create a scatterplot of diamond price vs.
# volume (x * y * z) and color the points by
# the clarity of diamonds. Use scale on the y-axis
# to take the log10 of price. You should also
# omit the top 1% of diamond volumes from the plot.

# Note: Volume is a very rough approximation of
# a diamond's actual volume.

# The plot should look something like this.
# http://i.imgur.com/excUpea.jpg

# Note: In the link, a color palette of type
# 'div' was used to color the scatterplot using
# scale_color_brewer(type = 'div')

names(diamonds)
ggplot(data = diamonds, aes(x = volume, y = price)) +
    geom_point(aes(color = clarity)) +
    scale_x_continuous(limits = c(0, quantile(diamonds$volume, 0.99))) +
    scale_y_log10() +
    scale_color_brewer(type = 'div') +
    xlab("volume") +
    ylab("price")
