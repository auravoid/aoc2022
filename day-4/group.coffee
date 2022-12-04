isRangeWithinRange = (firstRange, secondRange) ->
  firstRanges = firstRange.split(',')
  secondRanges = secondRange.split(',')

  for rangeOne in firstRanges
    [r1Start, r1End] = rangeOne.split('-')

    r1Start = parseInt(r1Start)
    r1End = parseInt(r1End)

    if r1End is undefined
      r1End = r1Start

    for rangeTwo in secondRanges
      [r2Start, r2End] = rangeTwo.split('-')

      r2Start = parseInt(r2Start)
      r2End = parseInt(r2End)

      if r2End is undefined
        r2End = r2Start

      if (r1Start >= r2Start && r1End <= r2End) || (r2Start >= r1Start && r2End <= r1End)
        return true

    return false

fs = require 'fs'
fs.readFile 'input.txt', 'utf8', (err, data) ->
    if err
        throw err
    overlaps = 0
    
    inputs = data.split '\n'
    inputs.forEach (input) ->
        cleansed = input.replace(/(\r\n|\n|\r)/gm, "")
        data = cleansed.split ','
    
        if isRangeWithinRange(data[0], data[1])
          overlaps++
        
    console.log "Found #{overlaps} overlaps"
