function getRelationship(x, y) {
    var xIsNumeric = !isNaN(parseFloat(x)) && isFinite(x);
    var yIsNumeric = !isNaN(parseFloat(y)) && isFinite(y);
    if (xIsNumeric && yIsNumeric) {
        if (x === y) {
            return '=';
        } else if (x < y) {
            return '<';
        } else if (x > y) {
            return '>';
        } else {
            return 'problem';
        }
    } else if (!xIsNumeric && yIsNumeric) {
        return "Can't compare relationships because " + x + " is not a number.";
    } else if (xIsNumeric && !yIsNumeric) {
        return "Can't compare relationships because " + y + " is not a number.";
    } else if (!xIsNumeric && !yIsNumeric) {
        return "Can't compare relationships because " + x + " and " + y + " are not numbers.";
    };
};

// Try logging these functions to test your code!
console.log(getRelationship(1,4));
console.log(getRelationship(1,1));
console.log(getRelationship("that",2));
console.log(getRelationship("this"," something else"));
console.log(getRelationship(3));
console.log(getRelationship("hi"));
console.log(getRelationship(NaN));
console.log(getRelationship(NaN, undefined));