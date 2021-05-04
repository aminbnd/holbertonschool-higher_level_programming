#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const file = process.argv[2];
const outputText = process.argv[3];
fs.writeFile(file, outputText, 'utf-8', (err) => {
  if (err) throw err;
});
