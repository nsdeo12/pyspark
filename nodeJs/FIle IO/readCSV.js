var fs= require('fs')
var data =fs.readFileSync('./csvData.csv').toString()
console.log(data);

var rows=data.split('\n')
console.log(rows);
rows.forEach((row) => {
    let column=row.split(',')
    console.log(column);

})