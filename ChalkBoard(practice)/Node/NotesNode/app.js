console.log('starting app.')

const fs = require('fs')
const os = require('os')
const _ = require('lodash')
const notes = require('./notes.js')

// console.log(_.isString(true))
// console.log(_.isString('Nathan'))
var filteredArray = _.uniq(['Nathan','Nathan',1,1,2,3,4])
console.log(filteredArray)





// var add = notes.add(7,8)
// console.log(add)
// var res = notes.addNote()
// console.log(res)

// var user = os.userInfo()
//
//
// fs.appendFile('greetings.txt', `Hello ${user.username}! You are ${notes.age}`, function (err){
//     if(err){
//         console.log('Unable to write file')
//     }
// })
