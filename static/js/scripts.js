/*!
* Start Bootstrap - Blog Post v5.0.8 (https://startbootstrap.com/template/blog-post)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-post/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

let pid = document.querySelector("[data-id-page]").getAttribute("data-id-page");
let nid = document.querySelector(`[data-id-nav='${pid}']`);
console.log(123456);

if (pid == nid.getAttribute("data-id-nav")) {
    nid.classList.add("active");
}
