const fs = require('node:fs');
const readline = require('node:readline');

let seeds = []
let maps = {
    "s2s" : [],
    "s2f" : [],
    "f2w" : [],
    "w2l" : [],
    "l2t" : [],
    "t2h" : [],
    "h2l" : [],
}

let firstLine = true
let keys = Object.keys(maps)
let curr_map = -1

 // map : [dest, source, range]
function getDestination(idx, initial){
    let dest = -1
    // loop through every source value in the map
    for (let i = 0; i < maps[keys[idx]].length; i++){
        let source = parseInt(maps[keys[idx]][i][1])
        let range = parseInt(maps[keys[idx]][i][2])

        // check to see if it falls within range of mapped source values
        if(initial >= source && initial <= source + range -1){
            let diff = Math.abs(initial - source)
            dest = parseInt(maps[keys[idx]][i][0]) + diff
        }
    }
    // if the seed has no mapped value, it maps to itself
    if(dest < 0){
        dest = initial
    }

    return dest

}

async function solve() {
  const fileStream = fs.createReadStream('5/part1/input.txt');

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });
  // Note: we use the crlfDelay option to recognize all instances of CR LF
  // ('\r\n') in input.txt as a single line break.

  for await (const line of rl) {
    // get the list of seeds to plant
    if(firstLine){
        seeds = line.split(":")[1].split(" ")
        seeds.shift() // remove empty element
        firstLine = false
        continue
      }
      
      // convert the maps to a dictionary of maps
      // each map is an n x 3 array
      if(line){
        if(line.includes(":")){
            curr_map += 1
            continue
        }
        
        maps[keys[curr_map]].push(line.split(" "))
      }
  }

  let lowest = Number.MAX_VALUE

  for (const seed of seeds){
    // get destination for the seed
    let dest = getDestination(0, parseInt(seed))

    // use the destination from each map, pass it into the next one
    for(let i = 1; i < keys.length; i++){
        dest = getDestination(i, dest)
    }

    if(dest < lowest){
        lowest = dest
    }
  }

  console.log(lowest)
}

solve(); 

