export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city)
  .map((student) => {
    const SGrade = newGrades.find((grade) => grade.studentId === student.id);
    return { ...student, grade: SGrade ? SGrade.grade : 'N/A', };
  });
}
