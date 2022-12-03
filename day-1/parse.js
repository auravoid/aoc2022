const fs = require('fs')
const data = fs.readFileSync('./input.txt', 'utf8')

const dataArray = data.split(/\r?\n\r?\n/)

const parsedData = []

dataArray.forEach((item) => {
  let itemArray = item.split(/\r?\n/)
  itemArray = itemArray.reduce((a, b) => Number(a) + Number(b))
  parsedData.push(itemArray)
})

// To get part 1 answer
const greatestNumber = parsedData.reduce((a, b) => Math.max(a, b))
console.log(greatestNumber)

// To get part 2 answer
const topThree = parsedData.sort((a, b) => b - a).slice(0, 3)
const topThreeTotal = topThree.reduce((a, b) => Number(a) + Number(b))
console.log(topThreeTotal)
