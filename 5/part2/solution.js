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
function getSource(idx, initial){
    let source = -1
    let row = maps[keys[idx]]
    // // check if initial is lower than min dest or greater than max
    
    // loop through every row in the map
    for (let i = 0; i < row.length; i++){
        let dest = parseInt(row[i][0])
        let range = parseInt(row[i][2])

        // check to see if it falls within range of mapped dest values
        if(initial >= dest && initial <= dest + range -1){
            let diff = Math.abs(initial - dest)
            source = parseInt(row[i][1]) + diff
            break
        }
    }
    
    // if the seed has no mapped value, it maps to itself
    if(source < 0){
        source = initial
    }

    return source

}

async function solve() {
  const fileStream = fs.createReadStream('5/part2/input.txt');

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

  // start with location 0, and check the maps in reverse order to get a seed
  for(let i = 0; i <= 382895070; i++){
      let source = getSource(keys.length -1, i)

      for(let j = keys.length-2; j >=0; j--){
        source = getSource(j, source)
    }

    // check if seed exists
    for (let seed_idx= 0; seed_idx < seeds.length -1; seed_idx +=2){
      if(source >= parseInt(seeds[seed_idx]) && source <= parseInt(seeds[seed_idx]) + parseInt(seeds[seed_idx+1])){
        lowest = i
        break
      }
    }

    // the first valid location we find is the answer
    if(lowest < Number.MAX_VALUE){
      break
    }
  }
    
  console.log(lowest)

}

solve(); 

