function readNumber() {
    let num;
    do {
        num = prompt("Enter a number please?", 0);
    } while ( !isFinite(num) );
    if (num === null || num === '') return null;
        return +num;
}
alert(`Read: ${readNumber()}`);

function ucFirst(str) {
    if (!str) return str;
    return str[0].toUpperCase() + str.slice(1);
}
alert( ucFirst("john") ); // John

function truncate(str, maxlength) {
    return (str.length > maxlength) ?
    str.slice(0, maxlength - 1) + '…' : str;
}

let styles = ["Jazz", "Blues"];
styles.push("Rock-n-Roll");
styles[Math.floor((styles.length - 1) / 2)] = "Classics";
alert( styles.shift() );
styles.unshift("Rap", "Reggae");

function sumInput() {
    let numbers = [];
    while (true) {
    let value = prompt("A number please?", 0);
        if (value === "" || value === null || !isFinite(value)) break;
        numbers.push(+value);
    }
    let sum = 0;
    for (let number of numbers) {
        sum += number;
    }
    return sum;
}
alert( sumInput() );

function filterRange(arr, a, b) {
    return arr.filter(item => (a <= item && item <= b));
}
let arr = [5, 3, 8, 1];
let filtered = filterRange(arr, 1, 4);
alert( filtered );
alert( arr );

function filterRangeInPlace(arr, a, b) {
    for (let i = 0; i < arr.length; i++) {
        let val = arr[i];
        if (val < a || val > b) {
            arr.splice(i, 1);
            i--;
        }
    }
}

arr = [5, 3, 8, 1];
filterRangeInPlace(arr, 1, 4);
alert( arr ); // [3, 1]
arr = [5, 2, 1, -10, 8];
arr.sort((a, b) => b - a);
alert( arr );

function groupById(array) {
    return array.reduce((obj, value) => {
        obj[value.id] = value;
        return obj;
    }, {})
}

let map = new Map();
map.set("name", "John");
let keys = Array.from(map.keys());
keys.push("more");
alert(keys);
        
function sumSalaries(salaries) {
    let sum = 0;
    for (let salary of Object.values(salaries)) {
        sum += salary;
    }
    return sum;
}
let salaries = {
    "John": 100,
    "Pete": 300,
    "Mary": 250
};
alert( sumSalaries(salaries) );

let user = {
    name0: "John",
    years: 30
};
let {name0, years: age, isAdmin = false} = user;
alert( name0 ); 
alert( age ); 
alert( isAdmin ); 

function topSalary(salaries) {
    let maxSalary = 0;
    let maxName = null;
    for(const [name, salary] of Object.entries(salaries)) {
        if (maxSalary < salary) {
        maxSalary = salary;
        maxName = name;
        }
    }
    return maxName;
}

function getWeekDay(date) {
    let days = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA'];
    return days[date.getDay()];
}

let date = new Date(2014, 0, 3);
alert( getWeekDay(date) );
function getLocalDay(date) {
    let day = date.getDay();
    if (day == 0) { // weekday 0 (sunday) is 7 in european
        day = 7;
    }
    return day;
}

function formatDate(date) {
    let diff = new Date() - date; 
    if (diff < 1000) {
        return 'right now';
    }
    let sec = Math.floor(diff / 1000); 
    if (sec < 60) {
        return sec + ' sec. ago';
    }
    let min = Math.floor(diff / 60000);
    if (min < 60) {
        return min + ' min. ago';
    }
    let d = date;
    d = [
        '0' + d.getDate(),
        '0' + (d.getMonth() + 1),
        '' + d.getFullYear(),
        '0' + d.getHours(),
        '0' + d.getMinutes()
    ].map(component => component.slice(-2)); // take last 2 digits of every component
    return d.slice(0, 3).join('.') + ' ' + d.slice(3).join(':');
}
alert( formatDate(new Date(new Date - 1)) );
alert( formatDate(new Date(new Date - 30 * 1000)) ); 
alert( formatDate(new Date(new Date - 5 * 60 * 1000)) ); 
alert( formatDate(new Date(new Date - 86400 * 1000)) );

user = {
    name: "John Smith",
    age: 35
};
let user2 = JSON.parse(JSON.stringify(user));

let room = {
    number: 23
};
let meetup = {
    title: "Conference",
    occupiedBy: [{name: "John"}, {name: "Alice"}],
    place: room
};
room.occupiedBy = meetup;
meetup.self = meetup;
alert( JSON.stringify(meetup, function replacer(key, value) {
    return (key != "" && value == meetup) ? undefined : value;
}));