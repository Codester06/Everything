const storeBtn = document.getElementById('store-btn');
const retrBtn = document.getElementById('retrieve-btn');

storeBtn.addEventListener('click', () => {
    const userID = 'u123'
    const user = { name: 'MAX', age: 30 }
    document.cookie = `udi = ${userID}; max-age = 360`;
    document.cookie = `user=${JSON.stringify(user)}`
})

retrBtn.addEventListener('click', () => {
    // console.log(document.cookie.split(';'))
    console.log(document.cookie)
    const cookieData = document.cookie.split(';');
    const data = cookieData.map(i => {
        return i.trim();
    }) 
    console.log(data[1].split('='));   //user value
});
