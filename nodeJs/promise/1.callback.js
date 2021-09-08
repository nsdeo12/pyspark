const list=['Man','Woman','Child']
const allKind=list.map(function (x) {
    x=x+' kind'
    return x
})

console.log(list,allKind)