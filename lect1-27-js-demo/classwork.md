# Lecture 3 Activity

You're going to be figuring out how to take a web page and make it more interactive!

## 1) Set up
1. Open up your dev environment and grab the demo code from earlier (I'm sure you were following along in the demo :) but just in case, [here's a GitHub link](https://github.com/csc4351-f22/setup-and-demos/lect1-27-js-demo))
2. Make a directory called `static` in the demo code folder, and within that folder, make a file called `script.js`.
3. Inside `static/script.js`, write the following line:
```
alert('Hello world!');
```
4. Now let's connect our JS file to HTML. Inside the `<head>` tags, similar to CSS, let's add a script to link to this file:
```
<script type="text/javascript" src="/static/script.js"></script>
```
5. Run `python3 main.py` to check that the script runs. When you load your page, you should now see your alert pop up.

## 2) Basic user interaction - button
1. Add a simple [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button) element to your HTML file. Give it an id, which will help you refer to it in JS code.
```
<button id="myCoolButton">Click here!</button> 
```
2. Now we're going to use JS to make something happen when you click the button! We do this by using the [DOM API](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents) to access an HTML element in JS code and add some sort of logic when an event happens (i.e. click, hover, scroll). Read [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#addeventlistener_and_removeeventlistener) about what event listeners are and how they work. In your JS file, add the following code. 
```
window.onload = () => { // onload makes sure the content is loaded on page first
    document.getElementById('myCoolButton').addEventListener('click', () => {
        // Anything you want to do when this button is clicked should be added below
        console.log('Button was clicked!'); // console.log is like printing in JS!
    });
};
```
3. Let's make sure that this logged. Open [your developer tools](https://balsamiq.com/support/faqs/browserconsole/#google-chrome), click the "Console", refresh the page, and click the button to see if something is logged! Your dev tools will be important to check for errors, print statements, and overall debugging.

## 3) Interaction with the DOM
1. Now, let's make the button a little more functional. Instead of logging a statement, let's change the color of all the flashed messages from red to green when the button is pressed.

There are a couple ways to do this, and you should feel free to explore the `document.getElementsByClassName()` function if you don't want to change the HTML, or just want to play with a different way to select elements in the DOM from your JavaScript.

For the rest of us, let's add an `id` to the `<ul`> element containing our flashed messages:
```
<ul id="flashes" class=flashes>
```
And select that element with
```
document.getElementById('flashes')
```

inside your event listener.

2. Let's change the CSS on that element we just selected! See the [tutorial here](https://www.w3schools.com/js/js_htmldom_css.asp) -- you'll need to set the `style.color` attribute to `green` when the button is clicked!
3. Run your app again, enter an invalid ID, and then click your button to see if the message color changes.

## 4) Client-side form validation
1. Now, we're going to explore the real power of Javascript: cutting the server out of interactions that it doesn't need to be involved in. Previously, our app was running logic on the BACKEND to see if the form input was valid (i.e. matched your campus ID). But we don't need a whole HTTP request to do that! Let's just have client-side Javascript do the check. 

To start, add a function to your `script.js` called `validateForm()`:  
```
function validateForm() {
}
```
2. Selecting forms in JS works a little differently. The `document` object has a `forms` field that contains an ordered list of all the forms. Since there's only one form on the page, you can select it with `document.forms[0]`. Then, within the form, we need to select the actual input element we want. So the full selector to get the value of the input is `document.forms[0].elements[0].value`.

Now, fill in the `validateForm()` function so that it checks if the input value was equal to your campus ID. If it was, return `true` -- this will allow the form to go through. If not, return `false` and raise an alert saying an invalid ID was entered.

3. To wire up your function, you'll need to add an `onSubmit` attribute to your HTML form:
```
<form method="POST" action="/login" onsubmit="return validateForm()">
```
4. Run your app again and verify that the form rejects bad input on the client side! You now shouldn't need your Flask logic checking the input -- you can just redirect to the welcome page whenever a POST is received at the form's action endpoint.
5. Stuck? Try the examples [here](https://www.w3schools.com/js/js_validation.asp) and look at the docs [here](https://developer.mozilla.org/en-US/docs/Web/API/Document/forms)


## 5) More user interaction - inputs
**Things are going to get more difficult from here on out. There will be less handholding for the individual steps. If you've seen JavaScript before and/or you're comfortable with the tech stack so far, these steps should be an appropriate level of challenge for you. If you haven't and you have leftover time, give it a whirl and see how far you get :)**
1. **We're switching tech stacks!** Go into the code from your individual assignments. We're going to be adding doing some JavaScript search functionality on it. 
2. Make a new input search bar, at the top of your page.  Ignore the search from before and all the books we're already showing.  Give your new input a clear and useful ID.
3. Add a JS file in your `static` folder.
4. Update your JS code to follow the following interaction: (1) User types in text in the new input, (2) User clicks the existing button to submit, **(3) You alert the text that was typed in**. You will need to add code for #3.
Here's how you can access what the user typed into the input and set it to a variable (you have to figure out where to put the code):
```
const userText = document.getElementById('PUT_INPUT_ID_HERE').value;
```

## 6) Passing user data to the backend (Flask!)
1. Web apps often have multiple endpoints to get different data/HTML pages from. Create a *new* endpoint in our Flask web server to take in our user's search text. In `app.py` (`main.py`, whatever you called it), create a new variable endpoint `/search/<user_text>` that allows us to pass a variable from the client to the server *through the URL*. *Read* this [documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules) on how variable endpoints work. The function logic in it should simply print the `user_text` on the server and `return {'userText': user_text}`.
2. Now, *when the user clicks the submit button* after entering text, let's send that search text from the client (browser) to the server (on Flask). The code below will create an endpoint that matches what you created in the previous step, and then send a request over the internet to get back the server's response. Use the following code and put it *in the right place* in `script.js`. You will be leveraging the [fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). You have to figure out where to put the code to make it execute when the user clicks the button.
```
const url = '/search/' + userText; // This should remind you of APIs in Python!
window.fetch(url).then(response => response.json()) // So should JSON conversion!
    .then(data => { // .then will only run the function *once* the data is fetched from the internet
        console.log(data); // See what this logs!
    });
```

## 7) Returning back new search data
1. In `app.py`, update your new Flask endpoint to return back the books *for that specific text that the user searched*. Look at how we fetch the book data in our '/' route and use the same helper function `book_search` (or whatever you used), but with the user's text. The response can be returned as a Python dictionary, which will be automatically converted to JSON. Instead of returning an HTML response (via `render_template`), we are now returning a JSON response with data that we can parse on the client in JS.
```
return {
    'books': books, # books is an array of strings, see how we got this array in our other route!
}
```
2. Use `console.log` to make sure that you are successfully getting this data back in JS. This data will be returned as a JavaScript object, which you can then access using `myObject['myKey']` or `myObject.myKey`.

## 8) Add this new data from the backend to your UI
1. Now let's take the data that our server returns, *loop* through each article headline in the list, and add each to the web page. ere's an example of how to create a new HTML element, but you're going to have to figure out how to add each new element to the existing DOM (this may require adding another `id` to your container `div` in `index.html`.
```
const newDiv = document.createElement('div');
newDiv.textContent = 'New text!!!!'; // Sets the text of the element
```
2. If everything worked as planned, then when the user enters text in the input and clicks the button, you will see book data related to the search show up now on the web page! (it doesn't have to be pretty)

## 9) Stretch goal - clean up the page!
1. Figure out how to also *remove* the old content from the DOM. So when the user searches, they will see the old book data go away and the new book data take its place. Google is your BFF!
