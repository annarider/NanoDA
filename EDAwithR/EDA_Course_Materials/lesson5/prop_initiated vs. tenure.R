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

ggplot(data = pf, aes(x = tenure, y = prop_initiated)) +
    geom_line(stat = 'summary', fun.y = median, aes(color = year_joined.bucket))

### Everything below is scratch pad
names(pf)
str(pf)
summary(pf$prop_initiatedpf_prop_friend <- pf %>%
    group_by(prop_initiated, tenure, year_joined.bucket) %>%
   # select(year_joined.bucket) %>%
    summarise(median_prop_initiated = median(prop_initiated),
              mean_tenure = mean(tenure),
              year_joined.bucket = year_joined.bucket)

summary(pf_prop_friend)

ggplot(data = pf, aes(x = mean(tenure), y = median(prop_initiated))) +
    geom_line(aes(color = year_joined.bucket))


