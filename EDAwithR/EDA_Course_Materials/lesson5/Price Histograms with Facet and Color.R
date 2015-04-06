# Create a histogram of diamond prices.
# Facet the histogram by diamond color
# and use cut to color the histogram bars.

# The plot should look something like this.
# http://i.imgur.com/b5xyrOu.jpg

# Note: In the link, a color palette of type
# 'qual' was used to color the histogram using
# scale_fill_brewer(type = 'qual')

ggplot(data = diamonds, aes(x = price, fill = cut)) +
    geom_histogram() +
    facet_wrap( ~ color) +
    scale_fill_brewer(type = 'qual')
