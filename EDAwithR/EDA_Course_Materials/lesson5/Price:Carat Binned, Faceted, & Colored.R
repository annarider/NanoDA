# Create a scatter plot of the price/carat ratio
# of diamonds. The variable x should be
# assigned to cut. The points should be colored
# by diamond color, and the plot should be
# faceted by clarity.

# The plot should look something like this.
# http://i.imgur.com/YzbWkHT.jpg.

# Note: In the link, a color palette of type
# 'div' was used to color the histogram using
# scale_color_brewer(type = 'div')

names(diamonds)

ggplot(data = diamonds, aes(x = cut, y = price/carat)) +
    geom_point(aes(color = color), position = position_jitter(h = 0)) +
    facet_wrap( ~ clarity) +
    scale_color_brewer(type = 'div')
