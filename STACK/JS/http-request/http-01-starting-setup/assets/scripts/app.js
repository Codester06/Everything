const xhr = new XMLHttpRequest();

xhr.open('GET','https://jsonplaceholder.typicode.com/posts');
// console.log(xhr)
xhr.responseType = 'json'
xhr.onload = function() {
    // console.log(xhr.response)
    // const listOfPosts = JSON.parse(xhr.response)
    const listOfPosts = xhr.response
    console.log(listOfPosts)
}
xhr.send();