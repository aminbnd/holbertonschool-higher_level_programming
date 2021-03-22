#!/usr/bin/node

let i = 0;
process.argv.forEach((val, index) => {
  i++;
});
if (i < 2) {
  console.log('No argument');
} else if (i === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
