const fs = require('fs');

const prepareInput = (sampleInput) => {
  const inputList = [];
  const refinedInput = sampleInput.split('\n\n');
  refinedInput.forEach((item) => {
    const smallItem = item.split('\n');
    const filterd = smallItem.filter((item) => item);
    inputList.push(filterd);
  });
  return inputList;
};

const elves = (input) => {
  const eachCarrying = [];
  input.forEach((item) => {
    const currentCalories = item.reduce((accumulator, value) => {
      return accumulator + parseInt(value, 10);
    }, 0);
    eachCarrying.push(currentCalories);
  });
  const top3 = eachCarrying.sort((a, b) => {
    return b - a;
  });
  console.log('Answer 1', top3[0]);
  console.log('Answer 2', top3[0] + top3[1] + top3[2]);
};

const main = () => {
  const input = fs.readFileSync('input.txt', 'utf8');
  const refinedInput = prepareInput(input);
  elves(refinedInput);
};

main();
