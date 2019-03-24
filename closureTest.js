function celebrityName (firstName) {
    var nameIntro = "This celebrity is ";
    // this inner function has access to the outer function's variables, including the parameter​
   function lastName (theLastName) {
        return nameIntro + firstName + " " + theLastName;
    }
    return lastName;
}

//console.log(celebrityName);

var mjName = celebrityName ("Michael"); // At this juncture, the celebrityName outer function has returned.​

console.log(mjName);

mjName('Jackson');

console.log(mjName);

