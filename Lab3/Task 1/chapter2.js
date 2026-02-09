'use strict';

alert( "I'm JavaScript!" );

let admin, name0; //"name" var is not allowed as a name
name0 = "John";
admin = name0;
alert( admin );

let thirdPlanet = "Earth";
let currentUser = "Aldiyar";

let name1 = "Ilya";
alert( `hello ${1}` ); //1
alert( `hello ${"name1"}` ); //name
alert( `hello ${name1}` ); //Ilya

let name2 = prompt("What is your name?", "");
alert(name2);

let a = 1, b = 1;
alert( ++a ); // 2
alert( b++ ); // 1
alert( a ); // 2
alert( b ); // 2

/*
"" + 1 + 0 = "10"
"" - 1 + 0 = -1
true + false = 1
6 / "3" = 2
"2" * "3" = 6
4 + 5 + "px" = "9px"
"$" + 4 + 5 = "$45"
"4" - 2 = 2
"4px" - 2 = NaN
"  -9  " + 5 = "  -9  5"
"  -9  " - 5 = -14
null + 1 = 1
undefined + 1 = NaN 
" \t \n" - 2 = -2
    
5 > 4 = true
"apple" > "pineapple" = false
"2" > "12" = true
undefined == null = true
undefined === null = false
null == "\n0\n" = false
null === +"\n0\n" = false
*/

let value = prompt('What is the "official" name of JavaScript?', '');
if (value == 'ECMAScript') {
  alert('Right!');
} else {
  alert("You don't know? ECMAScript!");
}

value = prompt('Type a number', 0);
if (value > 0) {
  alert( 1 );
} else if (value < 0) {
  alert( -1 );
} else {
  alert( 0 );
}

let message = (login == 'Employee') ? 'Hello' :
(login == 'Director') ? 'Greetings' :
(login == '') ? 'No login' :
'';

let userName = prompt("Who's there?", '');
if (userName === 'Admin') {
  let pass = prompt('Password?', '');
  if (pass === 'TheMaster') {
    alert( 'Welcome!' );
  } else if (pass === '' || pass === null) {
    alert( 'Canceled' );
  } else {
    alert( 'Wrong password' );
  }
} else if (userName === '' || userName === null) {
  alert( 'Canceled' );
} else {
  alert( "I don't know you" );
}
    
let i = 0;
while (++i < 5) alert( i );
for (let i = 0; i < 5; ++i) alert( i );
for (let i = 0; i < 5; i++) alert( i );
i = 0;
while (i < 3) {
  alert( `number ${i}!` );
  i++;
}

if (browser == 'Edge') {
  alert("You've got the Edge!");
} else if (browser == 'Chrome' || browser == 'Firefox' || browser == 'Safari' || browser == 'Opera') {
  alert( 'Okay we support these browsers too' );
} else {
  alert( 'We hope that this page looks ok!' );
}

function pow(x, n) {
  let result = x;
  for (let i = 1; i < n; i++) {
      result *= x;
  }
  return result;
}
let x = prompt("x?", '');
let n = prompt("n?", '');
if (n < 1) {
  alert(`Power ${n} is not supported, use a positive integer`);
} else {
  alert( pow(x, n) );
}

function ask(question, yes, no) {
  if (confirm(question)) yes();
  else no();
}
ask(
  "Do you agree?",
  () => alert("You agreed."),
  () => alert("You canceled the execution.")
);