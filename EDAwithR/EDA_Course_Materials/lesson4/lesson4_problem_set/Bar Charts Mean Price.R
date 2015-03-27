# We’ve created summary data frames with the mean price
# by clarity and color. You can run the code in R to
# verify what data is in the variables diamonds_mp_by_clarity
# and diamonds_mp_by_color.

# Your task is to write additional code to create two bar plots
# on one output image using the grid.arrange() function from the package
# gridExtra.

diamonds_by_clarity <- group_by(diamonds, clarity)
diamonds_mp_by_clarity <- summarise(diamonds_by_clarity, mean_price = mean(price))

diamonds_by_color <- group_by(diamonds, color)
diamonds_mp_by_color <- summarise(diamonds_by_color, mean_price = mean(price))

diamonds_mp_by_color
diamonds_mp_by_clarity

p1 <- ggplot(data = diamonds_mp_by_color, aes(x = color, y = mean_price)) +
    geom_bar(stat="identity")

p2 <- ggplot(data = diamonds_mp_by_clarity, aes(x = clarity, y = mean_price)) +
    geom_bar(stat="identity")

grid.arrange(p1, p2, ncol = 1)

# With mean price by color, the mean price graduating increases as the color goes from D to J (color decreases in quality, i.e. D is the best color).
#
# With mean price by clarify, there is less consistency as the clarity changes from I1 to IF, the price rises up & peaks at SI2, and dips to the lowest bar at VVS1. Price doesn't consistently decrease as the clarity decreases.


