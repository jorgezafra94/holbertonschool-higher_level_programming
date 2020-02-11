#!/usr/bin/node
/* read a file */
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) {
    console.error(err);
  }
});
