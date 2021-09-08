var testPromise=new Promise((resolve,reject)=>{
    let x=2
    let y=4
    if (x===y){
        resolve
    }else {reject}
})
testPromise.then(function(){
    console.log('values are equal');
}).catch(function () {
    console.log('Error:values are not equal');
})

console.log(testPromise)