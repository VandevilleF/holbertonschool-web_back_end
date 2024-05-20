export default function getStudentIdsSum(students) {
  const initalValue = 0;
  return students.reduce((accumulator, student) => accumulator + student.id, initalValue);
}
