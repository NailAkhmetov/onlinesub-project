function burgerMenuAction() {
    let menuList = document.getElementById("menu-list");

    if (menuList.style.display === "none" || !menuList.style.display) {
        menuList.style.display = "block";
        setTimeout(() => {
            menuList.style.opacity = "1";
            menuList.style.maxHeight = "300px";
            menuList.style.padding = "13px 0";
        }, 100);
    } else {
        menuList.style.opacity = "1";
        menuList.style.maxHeight = "0";
        menuList.style.padding = "0";

        setTimeout(() => {
            menuList.style.display = "none"; 
        }, 300); 
    }
}


window.onload = function() {
    let menuList = document.getElementById("menu-list");
    menuList.style.display = "none"; 
    menuList.style.opacity = "1";     
    menuList.style.maxHeight = "0";   
    menuList.style.padding = "0";      
};

document.addEventListener("DOMContentLoaded", function() {
    if (!sessionStorage.getItem("preloaderShown")) {
        const preloader = document.getElementById("preloader");
        setTimeout(() => {
            preloader.classList.add("hidden");
        }, 5000);
        sessionStorage.setItem("preloaderShown", "true");
    } else {
        document.getElementById("preloader").classList.add("hidden");
    }
});
