// Iterate through the localizedRuleNames in ruleResults and 
// return an array of their strings.
function ruleList(results) {
  var localizedRuleNamesArray = [];
  for (rules in results.formattedResults.ruleResults) {
    localizedRuleNamesArray.push(results.formattedResults.ruleResults[rules].localizedRuleName)
  }
  return localizedRuleNamesArray;
}

// Iterate through pageStats in the psiResults object and 
// return the total number of bytes to load the website.
function totalBytes(results) {
  var totalBytes = 0;
  var RESOURCES = ["totalRequestBytes", "htmlResponseBytes", "cssResponseBytes", "imageResponseBytes",
    "javascriptResponseBytes", "otherResponseBytes"];
  var stats = results.pageStats;

  for (i in RESOURCES) {
    var val = RESOURCES[i];
    var byteVal = parseInt(stats[val]);
    totalBytes += byteVal;
  }
  return totalBytes;
}

// Below, you'll find a sample PS Insights JSON
// and two console.log statements to help you test your code!

psinsights = {
 "kind": "pagespeedonline#result",
 "id": "/speed/pagespeed",
 "responseCode": 200,
 "title": "PageSpeed Home",
 "score": 90,
 "pageStats": {
  "numberResources": 22,
  "numberHosts": 7,
  "totalRequestBytes": "2761",
  "numberStaticResources": 16,
  "htmlResponseBytes": "91981",
  "cssResponseBytes": "37728",
  "imageResponseBytes": "13909",
  "javascriptResponseBytes": "247214",
  "otherResponseBytes": "8804",
  "numberJsResources": 6,
  "numberCssResources": 2
 },
 "formattedResults": {
  "locale": "en_US",
  "ruleResults": {
    "AvoidBadRequests": {
      "localizedRuleName": "Avoid bad requests",
      "ruleImpact": 0.0
    },
    "MinifyJavaScript": {
      "localizedRuleName": "Minify JavaScript",
      "ruleImpact": 0.1417,
      "urlBlocks": [
      {
        "header": {
       "format": "Minifying the following JavaScript resources could reduce their size by $1 ($2% reduction).",
       "args": [
        {
         "type": "BYTES",
         "value": "1.3KiB"
        },
        {
         "type": "INT_LITERAL",
         "value": "0"
        }
       ]
        },
        "urls": [
        {
          "result": {
         "format": "Minifying $1 could save $2 ($3% reduction).",
         "args": [
          {
           "type": "URL",
           "value": "http://code.google.com/js/codesite_tail.pack.04102009.js"
          },
          {
           "type": "BYTES",
           "value": "717B"
          },
          {
           "type": "INT_LITERAL",
           "value": "1"
          }
         ]
        }
       },
       {
        "result": {
         "format": "Minifying $1 could save $2 ($3% reduction).",
         "args": [
          {
           "type": "URL",
           "value": "http://www.gmodules.com/ig/proxy?url\u003dhttp%3A%2F%2Fjqueryjs.googlecode.com%2Ffiles%2Fjquery-1.2.6.min.js"
          },
          {
           "type": "BYTES",
           "value": "258B"
          },
          {
           "type": "INT_LITERAL",
           "value": "0"
          }
         ]
        }
       }
      ]
     }
    ]
   },
   "SpriteImages": {
    "localizedRuleName": "Combine images into CSS sprites",
    "ruleImpact": 0.0
   }
  }
 },
 "version": {
  "major": 1,
  "minor": 11
 }
};

// Try logging the outputs below to test your code!
console.log(ruleList(psinsights));
console.log(totalBytes(psinsights));