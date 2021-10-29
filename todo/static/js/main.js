
//Last Version


var listItems = document.querySelectorAll(".breakfast");
var listLinks = document.querySelectorAll(".breakfast span");
var item_amounts = document.getElementById("item_amount");

//Adding counter items-cart 
item_cnt = 0;
item_amounts.innerHTML = item_cnt;

//Alert when the user click add element to the cart
//Adding elements to the cart
for (i = 0; i < listLinks.length; i++) {
	listLinks[i].addEventListener("click", () => {
		alert("You added one item to the cart. Check your cart.");
		item_cnt++;
		item_amounts.innerHTML = item_cnt;
	});
	//event for create the child in the cart
	listLinks[i].addEventListener("click", function (item) {
		addItem(item.path[1]);
	});
}

//Element total
var nf = Intl.NumberFormat("de-DE");
var total = document.getElementById("total-value");
var totalValue = 0.0;
total.innerText = `$${nf.format(totalValue)} COP`;

function addItem(child) {
	var srcImage = child.children[0].src;
	var title = child.children[1].innerText;
	var value = child.children[2].innerText;
	var numValue = extractNum(value);
	var element = document.getElementById("items");
	var item = document.createElement("div");
	item.setAttribute("class", "item");
	item.innerHTML =
		`<img src="${srcImage}" alt="img" class="img-item">` +
		'<div class="no-margin description-item">' +
		`<h5 class="title no-margin">${title}</h5>` +
		`<h5 class="value no-margin">${value}</h5>` +
		"</div>" +
		'<svg class="trash-can" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="none" viewBox="0 0 24 24"><path fill="white" d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2H8c-1.1 0-2 .9-2 2v10zM9 9h6c.55 0 1 .45 1 1v8c0 .55-.45 1-1 1H9c-.55 0-1-.45-1-1v-8c0-.55.45-1 1-1zm6.5-5l-.71-.71c-.18-.18-.44-.29-.7-.29H9.91c-.26 0-.52.11-.7.29L8.5 4H6c-.55 0-1 .45-1 1s.45 1 1 1h12c.55 0 1-.45 1-1s-.45-1-1-1h-2.5z"></path></svg>';
	element.appendChild(item);
	totalValue += numValue;
	total.innerText = `$${nf.format(totalValue)} COP`;
	var trashCan = item.children[2];
	trashCan.addEventListener("click", function (item) {
		removeItemCart(item.path[1]);
		item_cnt--;
		item_amounts.innerHTML = item_cnt;
	});
}

//Show and hidde cart button
var cart = document.getElementById("button-cart");
var statusCart = false;
cart.addEventListener("click", () => {
	var displayCart = document.getElementById("cart");
	if (statusCart) {
		displayCart.style.display = "none";
		statusCart = false;
	} else {
		displayCart.style.display = "initial";
		statusCart = true;
	}
});

//removing items from the cart
function removeItemCart(item) {
	var value = item.children[1].children[1].innerText;
	var numValue = extractNum(value);
	totalValue -= numValue;
	total.innerText = `$${nf.format(totalValue)} COP`;
	item.remove();
}

//function extract number of text and covert to int
function extractNum(string) {
	numString = string.match(/(\d+.\d+)/)[0].replace(".", "");
	return parseInt(numString);
}

//button clear cart
const buttonClear = document.querySelector(
	"#cart .btns-clear-checkout .btn-clear"
);
buttonClear.addEventListener("click", clearCart);

//function clear cart
function clearCart() {
	let items = document.getElementById("items");
	totalValue = 0;
	total.innerText = `$${nf.format(totalValue)} COP`;
	item_cnt = 0;
	item_amounts.innerHTML = item_cnt;
	while (items.firstChild != null) {
		items.removeChild(items.firstChild);
	}
}
