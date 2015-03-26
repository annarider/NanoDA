# Create a scatterplot of price vs carat
# and omit the top 1% of price and carat
# values.


ggplot(data = diamonds, aes(x = carat, y = price)) +
    geom_point() +
    scale_x_continuous(quantile(diamonds$carat, 0.9)) +
    scale_y_continuous(quantile(diamonds$price, 0.9)) +
    xlab("carat") +
    ylab("price")


    xlim(0, quantile(diamonds$carat, 0.9)) +
    ylim(0, quantile(diamonds$price, 0.9))
