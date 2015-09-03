/*
var awesomeThoughts = "I am Anna and I am AWESOME";

console.log(awesomeThoughts);

var funThoughts = awesomeThoughts.replace("AWESOME", "FUN")

console.log(funThoughts)

$("#main").append(funThoughts)
*/
// var formattedName = HTMLheaderName.replace("%data%", "Anna")

// var formattedRole = HTMLheaderRole.replace("%data%", "Data Analyst")

// $("#main").prepend(formattedRole)
// $("#main").prepend(formattedName)

var bio = {
    "name": "Anna",
    "role": "Presales Engineer",
    "contacts":  {
        "email": "annax.li10@gmail.com",
        "phone": "213.514.3729",
        "twitter": "@ax_li",
        "location": "San Mateo"
    },
    "welcomeMessage": "Hello!",
    "skills": ["talking", "cooking", "learning"]
};

$("#main").append(bio.name)

bio.work = {
    "position": "Technical Writer",
    "employer": "Semarchy",
    "city": "Menlo Park"
}

bio["education"] = {
    "schools": [
        {
            "name": "Stanford",
            "dates": "2012-2013",
            "location": "Stanford",
            "degree": "BA"
        },
        {
            "name": "USC",
            "dates": "2007-2011",
            "location": "Los Angeles",
            "degree": "BA"
        },
        {
            "name": "MRGS",
            "dates": "2003-2007",
            "location": "Auckland",
            "degree": "High school diploma"
        }
    ],
    "onlineCourses": [
        {
            "title": "Intro to Data Science",
            "school": "Udacity",
            "dates": "Jan 2015"
        },
        {
            "title": "Data Wrangling",
            "school": "Udacity",
            "dates": "March 2015"
        },
        {
            "title": "Exploratory Data Analysis",
            "school": "Udacity",
            "dates": "May 2015"
        },
        {
            "title": "Intro to Machine Learning",
            "school": "Udacity",
            "dates": "Aug 2015"
        }
    ]
}

// $("#main").append(bio.work["position"])
// $("#main").append(bio.education.name)


var education = {
    "schools": ["MRGS", "USC", "Stanford"],
    "school cities": ["Auckland", "Los Angeles", "Stanford"],
    "majors": ["Comm", "Journalism"],
    "graduation": [2011, 2013]
}

if (document.getElementsByClassName("education-entry").length === 0) {
    document.getElementById("education").style.display = "none";
}
