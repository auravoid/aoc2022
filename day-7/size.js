const input = require('fs').readFileSync(`./input.txt`, 'utf-8').split('\n')

class SysTree {
  constructor() {
    this.view = {}
    this.pwd = []
  }

  add(item) {
    let curDir = this.pwd.reduce((curDir, d) => curDir[d], this.view)
    curDir[item[1]] = !isNaN(item[0]) ? parseInt(item[0]) : {}
  }

  cd(name) {
    if (name === '/') this.pwd = []
    else if (name === '..') this.pwd.pop()
    else this.pwd.push(name)
  }
}

const tree = new SysTree()

for (let i = 0; i < input.length; i++) {
  let ins = input[i].split(' ')
  if (ins[0] === '$') {
    if (ins[1] === 'cd') tree.cd(ins[2])
  } else {
    tree.add(ins)
  }
}

let dirs = {}

const search = (dir = '', branch = tree.view) => {
  let size = 0
  for (let [a, z] of Object.entries(branch)) {
    if (!isNaN(z)) size += z
    else size += search(`${dir}/${a}`, branch[a])
  }
  dirs[dir ? dir : '/'] = size
  return size
}

search()

dirs = Object.fromEntries(Object.entries(dirs).sort((a, b) => a[1] - b[1]))

console.log(
  Object.values(dirs)
    .filter((n) => n < 100000)
    .reduce((a, n) => a + n, 0),
)

let spcNeed = 30000000 - (70000000 - dirs['/']),
  delDir = Object.keys(dirs).filter((dir) => dirs[dir] >= spcNeed)[0]

console.log(dirs[delDir])
