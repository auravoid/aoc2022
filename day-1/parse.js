const fs = require('fs')
const data = fs.readFileSync('./input.txt', 'utf8')

const dataArray = data.split(/\r?\n\r?\n/)

const parsedData = []

dataArray.forEach((item) => {
  let itemArray = item.split(/\r?\n/)
  itemArray = itemArray.reduce((a, b) => Number(a) + Number(b))
  parsedData.push(itemArray)
})

const greatestNumber = parsedData.reduce((a, b) => Math.max(a, b))
console.log(greatestNumber)
