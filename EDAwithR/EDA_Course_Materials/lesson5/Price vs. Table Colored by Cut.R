# Create a scatterplot of diamond price vs.
# table and color the points by the cut of
# the diamond.

# The plot should look something like this.
# http://i.imgur.com/rQF9jQr.jpg

# Note: In the link, a color palette of type
# 'qual' was used to color the scatterplot using
# scale_color_brewer(type = 'qual')

names(diamonds)
str(diamonds)

ggplot(data = diamonds, aes(x = table, y = price)) +
    geom_point(aes(color = cut)) +
    scale_color_brewer(type = 'qual')

