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

