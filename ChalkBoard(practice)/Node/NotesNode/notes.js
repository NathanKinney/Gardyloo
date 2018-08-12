
// moduel to  read/ write files
const fs = require('fs');

var fetchNotes = () => {
    //if file try to read it for duplicatenotes, if no file do nothing
  try {
    var notesString = fs.readFileSync('notes-data.json');
    //turns into json
    return JSON.parse(notesString);
  } catch (e) {
    return [];
  }
};

var saveNotes = (notes) => {
    // writes file in string format
    fs.writeFileSync('notes-data.json', JSON.stringify(notes));
};

//build out add functionality
var addNote = (title, body) => {
  var notes = fetchNotes();
  var note = {
    title,
    body
  };
  var duplicateNotes = notes.filter((note) => note.title === title);

// if no match length will be 0 so it'll be pushed onto the array
  if (duplicateNotes.length === 0) {
    notes.push(note);
    saveNotes(notes);
    return note;
  }
};

var getAll = () => {
  return fetchNotes()
};

var getNote = (title) => {
  var notes = fetchNotes();
  var filterNotes = notes.filter((note) => note.title === title);
  return filterNotes[0];
};

var removeNote = (title) => {
  //fetch notes
    var notes = fetchNotes()
  //filter notes, removing the one with title of argument
    var filteredNotes = notes.filter((note) => note.title !== title)
    saveNotes(filteredNotes)

    return notes.length !== filteredNotes.length
};
var logNote = (note) => {
    console.log('---')
    console.log(`Title: ${note.title}`)
    console.log(`Body: ${note.body}`)
}



module.exports = {
  addNote,
  getAll,
  getNote,
  removeNote,
  logNote,
};
