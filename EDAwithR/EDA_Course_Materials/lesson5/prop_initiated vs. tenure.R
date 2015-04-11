# Create a line graph of the median proportion of
# friendships initiated ('prop_initiated') vs.
# tenure and color the line segment by
# year_joined.bucket.

# Recall, we created year_joined.bucket in Lesson 5
# by first creating year_joined from the variable tenure.
# Then, we used the cut function on year_joined to create
# four bins or cohorts of users.

# (2004, 2009]
# (2009, 2011]
# (2011, 2012]
# (2012, 2014]

# The plot should look something like this.
# http://i.imgur.com/vNjPtDh.jpg
# OR this
# http://i.imgur.com/IBN1ufQ.jpg

getwd()
setwd("/Users/horsepower/Dropbox/Udacity/NanoDA/EDAwithR/EDA_Course_Materials/lesson3/")

pf <- read.delim("pseudo_facebook.tsv")

pf$year_joined <- trunc(abs(pf$tenure/365 - 2014))
pf$year_joined.bucket <- cut(pf$year_joined, breaks = c(2004,2009,2011,2012,2014))
pf$prop_initiated <- pf$friendships_initiated/pf$friend_count

names(pf)

ggplot(data = pf, aes(x = tenure, y = prop_initiated)) +
    geom_line(aes(color = year_joined.bucket), stat = "summary", fun.y = mean)

ggplot(data = pf, aes(x = tenure, y = prop_initiated)) +
    stat_summary(geom = 'line', fun.y = median, aes(color = year_joined.bucket))
