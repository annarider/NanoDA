install.packages('ggthemes', dependencies = TRUE) 
install.packages('ggplot2', dependencies = TRUE) 
library(ggplot2)
library(ggthemes) 

ggplot(aes(x = dob_day), data = pf) + 
  geom_histogram() + 
  scale_x_discrete(breaks = 1:31)

ggplot(data = pf, aes(x = dob_day)) + 
  geom_histogram() + 
  scale_x_discrete(breaks = 1:31) + 
  facet_wrap(~dob_month)

setwd("~/Dropbox/Udacity/NanoDA/EDAwithR/EDA_Course_Materials/lesson3")
pf <- read.delim('pseudo_facebook.tsv')

names(pf)
qplot(x = friend_count, data = pf) 
# answer in ggplot form
ggplot(aes(x = friend_count), data = pf) + 
  geom_histogram()

qplot(x = friend_count, data = pf, binwidth = 25) + 
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
facet_wrap(~gender)
# alternative answer using facet_grid
qplot(x = friend_count, data = pf) + 
  facet_grid(gender ~ .) 
# alternative answer in ggplot2
ggplot(aes(x = friend_count), data = pf) + 
  geom_histogram() + 
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  facet_wrap(~gender)

# NA values - http://www.statmethods.net/input/missingdata.html
qplot(x = friend_count, data = subset(pf, !is.na(gender)), binwidth = 25) + 
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  facet_wrap(~gender)
# another way to deal with Na values - caution: more dangerous as it will omit
# NA values in other variables, not only gender
qplot(x = friend_count, data = na.omit(pf), binwidth = 25) + 
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  facet_wrap(~gender)
# in ggplot2
ggplot(aes(x = friend_count), data = subset(pf, !is.na(gender))) +
  geom_histogram() + 
  scale_x_continuous(limits = c(0, 1000), breaks = seq(0, 1000, 50)) +
  facet_wrap(~gender)



# Statistics 'by' Gender Solution
by(pf$friend_count, pf$gender, summary)

# The parameter color determines the color outline of objects in a plot. 
# The parameter fill determines the color of the area inside objects in a plot. 
# You might notice how the color black and the hex code color of #099DD9 (a shade of blue)
# are wrapped inside of I(). The I() functions stand for 'as is' and tells qplot 
# to use them as colors. 

# ggplot2 docs on themes: http://docs.ggplot2.org/0.9.2.1/theme.html

ggplot(aes(x = tenure), data = pf) + 
  geom_histogram(binwidth = 30, color = 'black', fill = '#099DD9')


# Tenure
qplot(x = tenure/365, data = pf, binwidth = 1, color = I('black'), fill = I('#099DD9'))
# Improved plot
qplot(x = tenure/365, data = pf, binwidth = .25, color = I('black'), fill = I('#F79420')) +
  scale_x_continuous(breaks = seq (1, 7, 1), lim = c(0,7)) # makes breaks go from 0-7
## ggplot2 equivalent
ggplot(aes(x = tenure/365), data = pf) + 
  geom_histogram(binwidth = .25, color = 'black', fill = '#F79420')

# Adding labels to plots
qplot(x = tenure/365, data = pf, binwidth = .25, color = I('black'), fill = I('#F79420'),
  xlab = "Number of years using Facebook",
  ylab = "Number of users in sample") +  
  scale_x_continuous(breaks = seq (1, 7, 1), lim = c(0,7)) # makes breaks go from 0-7
# Add nice labels to the plot
## ggplot2 version
ggplot(aes(x = tenure / 365), data = pf) + 
  geom_histogram(color = 'black', fill = '#F79420') + 
  scale_x_continuous(breaks = seq(1, 7, 1), limits = c(0, 7)) + 
  xlab('Number of years using Facebook') + 
  ylab('Number of users in sample')


names(pf)
# Exercise to create Histogram of ages from pf dataset
ggplot(aes(x = age), data = pf) +
  geom_histogram(binwidth = 10, color = 'black', fill = 'yellow') +
  scale_x_continuous(breaks = seq(1, 120, 10), limits = c(10,120)) +
  xlab("Age in years") +
  ylab("Number of users in sample")
