var moonWalkers = [
  "Neil Armstrong",
  "Buzz Aldrin",
  "Pete Conrad",
  "Alan Bean",
  "Alan Shepard",
  "Edgar Mitchell",
  "David Scott",
  "James Irwin",
  "John Young",
  "Charles Duke",
  "Eugene Cernan",
  "Harrison Schmitt"
];

function alphabetizer(names) {
  var namesArray =[]; 
  for (name in names) {
    var splitName = names[name].trim().split(' ');
    var reversedName = splitName[1] + ', ' + splitName[0];
    namesArray.push(reversedName);
  };
  namesArray.sort();
  return namesArray;
}

// Try logging your results to test your code!
console.log(alphabetizer(moonWalkers));