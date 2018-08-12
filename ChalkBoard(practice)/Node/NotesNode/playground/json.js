// var obj = {
//     name: 'Nathan'
// }
//
// var stringObj = JSON.stringify(obj)

// var personString = '{"name": "Nathan","age": 27}'
// var person = JSON.parse(personString)

const fs = require('fs')
//OBJECT
var orignalNote = {
    title: 'Some title',
    body: 'Some body'
}
// STRING
var originalNoteString = JSON.stringify(orignalNote)
fs.writeFileSync('notes.json', originalNoteString)
var noteString = fs.readFileSync('notes.json')

//OBJECT
var note = JSON.parse(noteString)
console.log(typeof note)
console.log(note.title)