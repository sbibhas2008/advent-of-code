const fs = require('fs');

const input = fs.readFileSync('input.txt', 'utf8');
const [stacks, procedure] = input.split('\n\n');

const stacksLookup = {};
const prepareForLookup = stacks.split('\n').split(' ');
//   .filter((i) => i !== ' ')
//   .join()
//   .replaceAll('[', '')
//   .replaceAll(']', '')
//   .replaceAll(',', '')
//   .replaceAll('\n', '');
console.log(prepareForLookup);
