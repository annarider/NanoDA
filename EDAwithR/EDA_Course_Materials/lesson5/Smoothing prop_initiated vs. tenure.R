# Smooth the last plot you created of
# of prop_initiated vs tenure colored by
# year_joined.bucket. You can use larger
# bins for tenure or add a smoother to the plot.


str(pf)


ggplot(data = pf, aes(x = tenure, y = prop_initiated)) +
    geom_line(stat = 'summary', fun.y = median, aes(color = year_joined.bucket))
