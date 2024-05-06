export default function appendToEachArrayValue(array, appendString) {
  const correctArray = [];
  for (const idx of array) {
    const value = idx;
    correctArray.push(appendString + value);
  }

  return correctArray;
}
