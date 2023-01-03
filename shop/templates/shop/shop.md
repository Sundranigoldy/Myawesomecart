Till now we made an
2 apps 
1 blog
2shop
To add connection betn all html files and basefile
we use django syntax {% url 'appname:htmlfilename' %}
and add in apps views.py
app_name = "nameofapp"

<!-- now in shop we base html and index html 
where we added items in slide and we are starting with cart
for cart will use notes here.. -->
whnever performing task try to see which button is creating an error than go oon that function..


CART

session storage is an JS function..

sessionStorage.setItem('good','good')
if this doesnt work than we can use local storage
session storage  woprks til the session is expired.

localstorage.setItem('golldy', 'good')
it takes key value pair and it would be an problem hence to solve this we use stringify
JQUERY IS ALSO USED..
 TO START JQUERY U NEED TO IMPORT THAT 1ST


1. WE USE  BELOW SYNTAX WHETHER AFTER CLICKING WHETHER WE ARE GETTING AN OUTOUT IN JS OR NOT
$('.cart').click(function(){
    console.log('clicked'); 
     
jQuery syntax is tailor-made for selecting HTML elements and performing some action on the element(s). Basic syntax is: $(selector).action() 

2. var idstr = this.id.toString();
Here we are storing id of everytime "add to cart" is clicked in variable idstr as a string..

3. to add to the cart..
if (cart[idstr] != undefined) {
      cart[idstr] = cart[idstr] + 1;
    }
    else {
      cart[idstr] = 1;
    }
    console.log(cart);
    localStorage.setItem('cart', JSON.stringify(cart));
  });

4. to update to local storage we use 
localStorage.setItem('cart', JSON.stringify(cart));
need to understand abt stringify..


5. we have made one cart name navbar and in that we use
(<span id="cart">0</span>) to counter cart with id
and we had use JS to target by using id
document.getElementById('cart').innerHTML=Object.keys(cart).length;

where objects.keys(cart).length is we are targeting length of cart using this.
6. data-html="true"
meaning to accept the html in js we have to use this if we are using bootstrap..
7. to add +&- button


function updateCart(cart) {
    // console.log(cart);
    for (var item in cart) {
      // adding an plus and minus btn using innerhtml...
      document.getElementById('div' + item).innerHTML = "<button id ='minus" + item + "'class='btn btn-primary minus'>-</button><span id= 'val" + item + "''>" + cart[item] + "</span> <button id='plus" + item + "'class='btn btn-primary plus'>+</button>";
    }
  };
  $('.divpr').on("click", "button.minus", function(){
    // console.log("minus clicked");
    // without using slicing this.id gives id of clicked and with we get "pr" hence to remove that
    // we are using slice(6, ) which means remove anything takes whole string from 6th value.
    a =this.id.slice(7, );
    // console.log(a);
    // to minus from cart
    cart['pr'+a] = cart['pr'+a]-1;
    // it should not go below to zero so
    cart['pr'+a] = Math.max(0,cart['pr'+a]);
  // to catch and add to html
    document.getElementById('valpr'+a).innerHTML =cart['pr'+a];
    updateCart(cart);
  });
  $('.divpr').on("click", "button.plus", function(){
    // console.log("plus clicked");
    a =this.id.slice(6, );
    // console.log(a);
    cart['pr'+a] = cart['pr'+a]+1;
    document.getElementById('valpr'+a).innerHTML =cart['pr'+a];
    updateCart(cart);
  });

8. to save in localstorage.
localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
9.// $('.cart').click(function () this is static method and currently when adding clearcart button
  // we have to do things dyanmically hence we arew using Jquery on method
  $('.divpr').on('click', 'button.cart', function () {
    var idstr = this.id.toString();
    if (cart[idstr] != undefined) {
      cart[idstr] = cart[idstr] + 1;
    } else {
      cart[idstr] = 1;
    }
    updateCart(cart);
  });
10. 
 // to capture name here we have given name id 
      popstr = popstr + document.getElementById('name' + item).innerHTML.slice(0, 19) + "..." + "Qty:" + cart[item] + '<br>';
      i = i + 1;
11.
// to update the cart with +&- functinality
  function updateCart(cart) {
    // #to add in cart no. of items we have used sum...
    var sum = 0;
