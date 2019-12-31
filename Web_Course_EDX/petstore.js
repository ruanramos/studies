
/**
 * This function should calculate the total amount of pet food that should be
 * ordered for the upcoming week.
 * @param numAnimals the number of animals in the store
 * @param avgFood the average amount of food (in kilograms) eaten by the animals
 * 				each week
 * @return the total amount of pet food that should be ordered for the upcoming
 * 				 week, or -1 if the numAnimals or avgFood are less than 0 or non-numeric
 */
function calculateFoodOrder(numAnimals, avgFood) {
    // IMPLEMENT THIS FUNCTION!
    try {
        if (numAnimals >= 0 && avgFood >= 0)
        return numAnimals * avgFood;
        else return -1;
    } catch (error) {
        return -1;
    }
}

/**
 * Determines which day of the week had the most nnumber of people visiting the
 * pet store. If more than one day of the week has the same, highest amount of
 * traffic, an array containing the days (in any order) should be returned.
 * (ex. ["Wednesday", "Thursday"]). If the input is null or an empty array, the function
 * should return null.
 * @param week an array of Weekday objects
 * @return a string containing the name of the most popular day of the week if there is only one most popular day, and an array of the strings containing the names of the most popular days if there are more than one that are most popular
 */
function mostPopularDays(week) {
    // IMPLEMENT THIS FUNCTION!
    let max = -1, index = 0;
    for (let i = 0; i < week.length; i++) {
        const a = week[i].traffic;
        if (a > max) {
            max = a;
            index = i;
        }
    }
    return week[index].name;
}


/**
 * Given three arrays of equal length containing information about a list of
 * animals - where names[i], types[i], and breeds[i] all relate to a single
 * animal - return an array of Animal objects constructed from the provided
 * info.
 * @param names the array of animal names
 * @param types the array of animal types (ex. "Dog", "Cat", "Bird")
 * @param breeds the array of animal breeds
 * @return an array of Animal objects containing the animals' information, or an
 *         empty array if the array's lengths are unequal or zero, or if any array is null.
 */
function createAnimalObjects(names, types, breeds) {
    // IMPLEMENT THIS FUNCTION!
    console.log("AA")
    animals = [];
    for (let i = 0; i < names.length; i++) {
        let an = new Animal(names[i], types[i], breeds[i]);
        console.log(an);
        animals.push(an);
    }
    return animals;
}

/////////////////////////////////////////////////////////////////
//
//  Do not change any code below here!
//
/////////////////////////////////////////////////////////////////


/**
 * A prototype to create Weekday objects
 */
function Weekday (name, traffic) {
    this.name = name;
    this.traffic = traffic;
}

/**
 * A prototype to create Item objects
 */
function Item (name, barcode, sellingPrice, buyingPrice) {
     this.name = name;
     this.barcode = barcode;
     this.sellingPrice = sellingPrice;
     this.buyingPrice = buyingPrice;
}
 /**
  * A prototype to create Animal objects
  */
function Animal (name, type, breed) {
    this.name = name;
     this.type = type;
     this.breed = breed;
}


/**
 * Use this function to test whether you are able to run JavaScript
 * from your browser's console.
 */
function helloworld() {
    return 'hello world!!!!!!!!!!!!!!!!!';
    let a = new Animal("aaa", "bbb", "ccc");
    localStorage.animal = JSON.stringify(a);
    
}


function b() {
    let a = $(".week")[3];
    a.hide();
}

function a() {
    localStorage.count++;
    console.log("entered " + localStorage.count + " times");
    if(localStorage.count > 5) console.log(JSON.parse(localStorage.animal).type);
}
localStorage.count = 0;


function init() {
    $(".week").click(b);
    listItems();
    // buttons();
    inputs();
}

function inputs() {
    $('button').on({
        mouseenter: function() {
            // $(this).hide();
        },
        mouseleave: function() {
            $(this).css('background-color: red');
        },
        click: function() {
            $(this).css("background: url('http://boygeniusreport.files.wordpress.com/2016/11/puppy-dog.jpg')");
        }
    })
}

function buttons() {
    $('button').hover(function() {
        $(this).css('background-color', 'white');
    }, function() {
        $(this).css('background-color', 'black');
    })
}


function listItems() {
    $('li').mouseenter( function() {
        let a = $(this);
        a.css('color', 'red');
        a.css('font-size', '150%');
    });
    $('li').mouseleave(function() {
        let a = $(this);
        a.css('color', 'black');
        a.css('font-size', '100%');
    });
}

init()