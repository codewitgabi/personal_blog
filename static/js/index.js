var navIcon = document.getElementById("nav-search-icon");
var searchInputBox = document.getElementById("search-input-box");
var navToggleOpen = document.getElementById("nav-toggle-open");
var navToggleClose = document.getElementById("nav-toggle-close");
var navLinks = document.getElementById("nav-links");


navIcon.addEventListener("click", () => {
	if (searchInputBox.style.display === "block") {
		searchInputBox.style.display = "none";
	} else {
		searchInputBox.style.display = "block";
	}
});

navToggleOpen.addEventListener("click", () => {
	navLinks.style.top = "0";
});

navToggleClose.addEventListener("click", () => {
	navLinks.style.top = "-100vh";
});


var likeBtn = document.getElementById("like-btn");
var unlikeBtn = document.getElementById("unlike-btn");
var reactBtns = document.getElementsByClassName("react-btns")

likeBtn.addEventListener("click", () => {
	likeBtn.classList.add("hide");
	unlikeBtn.classList.remove("hide");
})

unlikeBtn.addEventListener("click", () => {
	unlikeBtn.classList.add("hide");
	likeBtn.classList.remove("hide");
})

for (let i = 0; i < reactBtns.length; i++) {
	reactBtns[i].addEventListener("click", function () {
		alert(this.dataset.react);
	})
}

// uncomment the code below to use on scroll to remove nav search bar
/*
window.addEventListener("scroll", () => {
	searchInputBox.style.display = "none";
});
*/