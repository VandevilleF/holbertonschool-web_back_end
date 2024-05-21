export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  const result = [];
  set.forEach(element => {
    if ( element.startsWith(startString)) {
      result.push(element.slice(startString.length));
    }
  });
  return result.join('-');
}
