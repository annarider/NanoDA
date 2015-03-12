getwd()
setwd('~/Dropbox/Udacity/NanoDA/EDAwithR/EDA_Course_Materials/lesson2')

statesInfo <- read.csv('stateData.csv')

subset(statesInfo, state.region == 4)

subset(statesInfo, illiteracy > 1.5)

statesInfo[statesInfo$illiteracy, ]


statesInfo[statesInfo$income > 5000, ]
