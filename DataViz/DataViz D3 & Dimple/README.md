# Summary 

My data visualization compares which states and districts in the U.S. have the greatest amount of growth in terms of private companies. The stacked bar chart shows the percentage growth from 2013 to 2014 and segments the data by industries. The data comes from Inc. (http://www.inc.com/). This visualization is directed to people interested in founding a company and who want to know which industries in which states are growing the fastest. 

# Design
- Based on the dataset from Inc. 5000, I decided that a chart that showed the fastest growing companies in the U.S. would be most interesting. I chose a bar chart because it would be easy to compare the height of the bars and the x variable (states) is categorical
- After creating a mock up of the chart on paper and getting initial feedback, I discovered that the chart was too simple - people wanted 

# Feedback 

### On paper chart

### Iteration 1
#### Person1: Looks like you have to put index.html in a folder, then make a subfolder called ./data/ and put companies.csv in there. Then running the Python command from the main folder worked.

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

### Future Development
#### Person1: 
If you want to get fancy, you could make it so when you click in the legend, the chart redraws and reorders based on only that industry.

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

## Dimple.js

### How to add a title to chart
http://stackoverflow.com/questions/25416063/title-for-charts-and-axes-in-dimple-js-charts

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
