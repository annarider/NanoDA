# Smooth the last plot you created of
# of prop_initiated vs tenure colored by
# year_joined.bucket. You can use larger
# bins for tenure or add a smoother to the plot.


str(pf)
ggplot(data = pf, aes(x = tenure, y = prop_initiated)) +
    geom_line(aes(color = year_joined.bucket), stat = "summary", fun.y = median)

ggplot(data = pf, aes(x = tenure, y = prop_initiated)) +
    geom_line(stat = 'summary', fun.y = median, aes(color = year_joined.bucket)) +
    geom_smooth()

is.data.frame(pf)
update.packages(ggplot2)
update.packages(plyr)

R.Version()
