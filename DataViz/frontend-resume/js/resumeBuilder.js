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
    "tech": {"position": "Technical Writer",
    "employer": "Semarchy",
    "city": "Menlo Park"
    },
    "journalism": {"position": "Journalist",
    "employer": "Poynter",
    "city": "St. Petersburg"
    }
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



var education = {
    "schools": ["MRGS", "USC", "Stanford"],
    "school cities": ["Auckland", "Los Angeles", "Stanford"],
    "majors": ["Comm", "Journalism"],
    "graduation": [2011, 2013]
}

bio.skills = {
    "Media": ["Final Cut Pro", "Wordpress", "Photoshop"],
    "SQL" : "Oracle SQL",
    "AWS" : ["EC2", "RDS"]
}


$("#main").append(bio.work["position"])
$("#main").append(bio.education.name)

console.log(bio);

// append skills info to resume

var bioSkillsLength = Object.keys(bio.skills).length
if (bioSkillsLength > 0) {

    $("#header").append(HTMLskillsStart);
    for (skillsList in bio.skills) {
        // console.log(bio.skills[skillsList]);
        if (bio.skills[skillsList].constructor === Array) {
            for (var skill in bio.skills[skillsList]) {
                var formattedSkill = HTMLskills.replace("%data%", bio.skills[skillsList][skill]);
                $("#skills").append(formattedSkill);    
                
            }
        } else {
            var formattedSkill = HTMLskills.replace("%data%", bio.skills[skillsList]);
            $("#skills").append(formattedSkill); 
        }   
    }
}

// append work/employer info

var bioWorkLength = Object.keys(bio.work).length;
if (bioWorkLength > 0) {
    for (job in bio.work) {
        $("#workExperience").append(HTMLworkStart);
        var employer = HTMLworkEmployer.replace("%data%", bio.work[job]["employer"])
        var position = HTMLworkTitle.replace("%data%", bio.work[job]["position"]);
        var formattedEmployerPosition = employer + position
        $(".work-entry:last").append(formattedEmployerPosition)
    }
    
}
