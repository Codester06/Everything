const storeBtn = document.getElementById('store-btn');
const retrBtn= document.getElementById('retrieve-btn');

const userId = 'u123';
const user = {
    name: 'max',
    age:'23',
    hobbies: ['sports','cooking']
}

storeBtn.addEventListener('click', () =>{
sessionStorage.setItem('uid', userId);
localStorage.setItem('user', JSON.stringify(user));

})

retrBtn.addEventListener('click', () =>{
    const extracted = sessionStorage.getItem('uid');
    const extractedUser = localStorage.getItem('user')
    console.log(extractedUser)
    if(extracted){
            console.log("here is the id" + extracted)
    }
    else{
        console.log("there is no id")
    }

});
