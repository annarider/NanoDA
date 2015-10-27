# Summary 

My data visualization compares which states and districts in the U.S. have the greatest amount of growth in terms of private companies. The stacked bar chart shows the percentage growth from 2013 to 2014 and segments the data by industries. The data comes from Inc. (http://www.inc.com/). This visualization is directed to people interested in founding a company and who want to know which industries in which states are growing the fastest. 

# Design
- Based on the dataset from Inc. 5000, I decided that a chart that showed the fastest growing companies in the U.S. would be most interesting. I chose a bar chart because it would be easy to compare growth across states taking advantage of the height of the bars as a visual encoding.
- After creating a mock up of the chart on paper and getting initial feedback, I discovered that the chart was too simple - people wanted more information and interaction. 
- Therefore I added industry segmentation to the data. Since the data is categorical, I chose distinct colors for different industries. Different hues show a clear distinction in the industry data, which is better than confusing viewers with a convergent or divergent color palette. Ordinarily, I would have kept all the bars the same color the course instructor emphasized that different colored bars in a bar chart do not encode any additional information and can even distract the reader. However, because I am encoding additional information about industry, the different colors are appropriate for the reader to be able to see the industry breakdown.
- A stacked bar chart was the most intuitive way to display the data. One person did not like the bar chart because it is hard to compare the height of bars for specific industries. I disagreed with this person's feedback because, while not perfect, the bar chart gave me a good way to compare across states using the height of the bar. Reading Stephen Few's article, "Data Visualization: Rules for Encoding Values in Graph", his advice for why bar charts are powerful resonated with me and seemed to be a good chart to chose for the story I want to communicate to readers: "Bars are visually the most weighty and dominant of the three objects that we commonly use to encode data in graphs". 
- Another person gave me feedback that the reader should be able to filter on a specific industry. This feedback conveniently seems to solve the issue raised by the person who did not like stacked bar charts. Therefore, I made it possible to click on the legend boxes to filter the chart. This change adds a lot of interaction and animation to the chart; like the analogy of the mouth of the "martini" glass, readers can now dive into the data and explore trends interesting to them.
- I cleaned up the aesthetics of the chart (title, axes labels, etc.) based on feedback that the text was unclear and messy. I moved the legend to the right to make room for the title. The legend on the right also made it easier for the eye to interpret the different industries because they were listed vertically. 
- I especially spent a lot of time configuring the tooltip because I received recurring feedback that the tooltip was confusing, didn't display data in a useful manner, or lacked data. I went through several iterations until I found the right balance of information to include. 
- Based on feedback by Person4, I changed the left margin in the svg so that the y-axis label would not be cut off.  
- Based on advice from Person4 and Person5 for how to fix the bug that caused an errant bar to appear during animation, I cleaned up the dataset by aggregating values.

### Switching Project datasets
I've decided I need to change datasets because the original company data is far too challenging for an explanatory data visualization.


# Feedback 

### On paper chart

### Iteration 1
#### Person1: 
Looks like you have to put index.html in a folder, then make a subfolder called ./data/ and put companies.csv in there. Then running the Python command from the main folder worked.

#### Person2: 
graph needs a title, pretty axis labels, and legend on the right, make room for the title
state names are cut off
the data is confusing and hard to cmopare. i would maybe do percentages or aggregate by state
it's just hard to compare industries to each other when the heights vary
I like the hovering label, altho i'd clean the text

#### Person3:
My suggestions for you: 
1. Can you resize the chart so it fits on my screen? I really don't like having to scroll up and down to look at the bars
2. The axis labels are cut off. Can you make them more descriptive
3. It's nice to have a legend but it's far away. Can you make it easier to interpret the legend when looking at the bars?


### Iteration 2
#### Person1:
It's interesting and informative. Feedback:
-the state names get cut off
-the tool tip isn't very human readable. Doesn't need to include the state.
-I would make the legend larger, put it in the upper right corner, and list the industries in the same order that you show their bars.

#### Person2: 
not a fan of stacked bar charts. if you really need to get all this information across at once, i guess stacked bar chart is the best way. i'm not sure, but what if you had a dot (or line) for each industry and state.  then you could compare the height of the industry within state and across states

#### Person3: 
Some improvement. I see you took some of my feedback to improve the chart like #1. #2 still is a problem - axis labels cut off. Good you followed #3. Here are more suggestions: 
4. Can you add a title?
5. Can you clean up the tooltip?

### Iteration 3
#### Person1: 
Your chart is greatly improved! Feedback: 
- It's cool to see how much more growth in percentage California has than other states. I like that I can see compare California with the height of the bar.
- Some of the industry categories are squished. I would make the tooltip show the industries and values so you can understand the differences.

#### Person3: 
The chart is better than before. 
6. It is hard to read the bars because they are stacked and I want to know what the precise numbers are. Can you give me more info about the growth dollars and percent? 
7. Why did you get rid of all the additional data in the tooltip? Now it's even more confusing. Can you add the info back like growth percent, etc.?

### Iteration 4
#### Person1: 
- In the tooltip, just "industry" is enough, not "industry category".
- Make growth in one line, not two. Put the percentage growth in parens. 

#### Person3: 
I like that the legend is on the right now. It's easier on my eyes to interpret what the colors mean.

### Iteration 5:
#### Person1: 
If you want to get fancy, you could make it so when you click in the legend, the chart redraws and reorders based on only that industry. It's good. I like the chart.

#### Person4: 
(Discussion forum feedback: https://discussions.udacity.com/t/project-feedback-bug-with-redrawing-chart/34740/2?u=annali)
I don't understand the y axis values - I suspect your data is already in millions but you should check.

I see this artifact in my browser against the the margin. Perhaps it is the y axis label. Margins??

### Iteration 6:
#### Person5:
(Discussion forum feedback: https://discussions.udacity.com/t/project-feedback-bug-with-redrawing-chart/34740/5?u=annali)
Dimple isn't designed to deal with this case where the axis change as well. I think the easiest thing to do is modify the source data. I noticed that the data is unaggregated but everything in the chart is aggregated. I would trying creating a dataset with a row for each State Industry combo including 0 values for industries that don't exist in a particular state. The update code you have now should handle that data gracefully.


### Feedback on Project submission (Iteration 7):
#### Person6 (grader):
 (Feedback on my project submission: https://review.udacity.com/#!/reviews/59563). 

### Reflection after project submission
My first submission for this data viz project didn't meet specs. The main problem was my visualization was exploratory, not explanatory. I spent a lot of time exploring my dataset to try to find relationships, trends, and patterns in the data. I even had a 1:1 coaching session with Carl on 2015-10-20 02:53 PDT. Unfortunately, his advice still wasn't very helpful. So I tried to answer the question: "If I want to live in California, what would be the best metro areas and industries in which to found a company?" Subsequently, I created a bubble chart to display my findings. 

### Iteration 8 (index8.html):
#### Person1: 
The chart is really broken. Initially, I can see the new bubbles but if I click on the legend, it draws another x-axis and the bubbles disappear. When I click the Reset All button, it causes bars to be drawn. 

#### Person3: 
The bubble chart idea is an interesting new direction. I think your new question does focus your project more now. But the chart you showed me doesn't display any relationships or patterns.   


### Iteration 9:
#### Person1:
The bubble chart is still not an explanatory data visualization. You have replaced state with city/metro in the x-axis but the data visualization still takes the form of your original visualization, i.e. it's still exploratory. Can you add information in paragraph form at the bottom of the chart to explain why you are showing these trends?

#### Person3: 
- Mmm...you are able to show me now that Los Angeles is the highest growth in percentage, but SF is higher in dollar growth. That's cool! 
- The chart is still a bit exploratory because I don't know where to go from here with this...
- What's the story behind this visualization? 
- What's the relationships/trends you're showing? 
- This dataset might be too difficult to perform this kind of analysis. Have you considered switching to a different dataset?

### Iteration 10:
#### Person1: 
Based on what you told me, this dataset has more potential for explanatory visualization. The chart is half finished. I can't tell what the different bar colors mean. You shouldn't use the percentage in y-axis; those are artificial. Add a tooltip that shows the statistics average

#### Person3:
Switching to a new data set was a good idea. Here's feedback: 
- This chart has a better story behind it. 
- You're missing fundamentals - title, legend, etc.
- x-axis should be called "baseball statistics" - it's clearer. 



# Resources

## Javascript

#### Check if array
http://stackoverflow.com/questions/767486/how-do-you-check-if-a-variable-is-an-array-in-javascript

#### Associative arrays - Javascript dict
http://blog.xkoder.com/2008/07/10/javascript-associative-arrays-demystified/

#### Check if key is in object
http://stackoverflow.com/questions/455338/how-do-i-check-if-an-object-has-a-key-in-javascript

#### Check if number
http://stackoverflow.com/questions/18082/validate-decimal-numbers-in-javascript-isnumeric

#### Functions are first class objects in Javascript
http://helephant.com/2008/08/19/functions-are-first-class-objects-in-javascript/

#### How to abbreviate numbers in tooltip in Javascript
(Not good - gives $0.854B)http://stackoverflow.com/questions/455338/how-do-i-check-if-an-object-has-a-key-in-javascript
http://www.raymondcamden.com/2012/07/06/Simple-JavaScript-number-format-function-and-an-example-of-Jasmine

## Tools
#### JS lint
helps validate JSON
 
#### Google developers PSI tools to help optimize front-end code; good for tests
PageSpeed Insights API.

PageSpeed Insights is a tool that helps developers optimize their web pages by analyzing the pages and generating tailored suggestions to make the pages faster. You can use the PageSpeed Insights API to programmatically generate PageSpeed scores and suggestions.

https://developers.google.com/speed/docs/insights/v1/getting_started

## D3
### D3 aggregate d3.nest()
http://bl.ocks.org/phoebebright/raw/3176159/

### D3 sum
https://github.com/mbostock/d3/wiki/Arrays#nest_rollup

### Add class to D3 object - .classed()
http://jaketrent.com/post/d3-class-operations/

### Add rect with text in it
http://bl.ocks.org/mbostock/7341714

## Dimple.js

### How to add a title to chart
http://stackoverflow.com/questions/25416063/title-for-charts-and-axes-in-dimple-js-charts

### How to make the legend interactive
http://dimplejs.org/advanced_examples_viewer.html?id=advanced_interactive_legends

### How to add a button
http://dimplejs.org/advanced_examples_viewer.html?id=advanced_responsive_sizing

## Data Viz experts

#### Scott Murray
#### Cole Nussbaumer

## Project Resources

### Topojson
Getting the topojson data files
US States
http://mapstarter.com/

US Counties
http://bl.ocks.org/mbostock/raw/4090846/us.json
Russia
http://bl.ocks.org/KoGor/5685876
Unemployment
http://bl.ocks.org/mbostock/4060606

World
http://bl.ocks.org/mbostock/raw/4090846/world-50m.json

How to convert shapefiles into topojson
http://stackoverflow.com/questions/16358472/svg-topojson-for-world-map-with-us-states

Link to topojson
https://cdnjs.cloudflare.com/ajax/libs/topojson/1.6.19/topojson.js

Topojson API docs
https://github.com/mbostock/topojson/wiki/API-Reference

### States Hash abbreviation
https://gist.github.com/mshafrir/2646763

### Maps colors

Ordinal color scale
https://github.com/mbostock/d3/wiki/Ordinal-Scales#categorical-colors

### D3 Maps tutorial

Great step-by-step tutorial based on Mike Bostock's counties map
http://socialinnovationsimulation.com/2013/07/11/tutorial-making-maps-on-d3/

D3 GeoJSON map with states
https://d3-geomap.github.io/map/choropleth/us-states/


### Export CSV in R
write.table(companies, file = "companies.csv", na = "", row.names = FALSE, quote = TRUE, sep = ",", eol = "\n", dec = ".")
