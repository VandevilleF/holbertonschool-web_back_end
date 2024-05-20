export default function getListStudentIds(value) {
  if (!Array.isArray(value)) {
    return [];
  } else {
    return value.map((element) => element.id);
  }
}
