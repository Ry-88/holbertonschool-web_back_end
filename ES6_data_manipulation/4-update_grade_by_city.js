export default function updateStudentGradeByCity(list, city, newGrades) {
  if (!Array.isArray(list)) {
    return [];
  }

  return list
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find((g) => g.studentId === student.id);
      const grade = gradeObj ? gradeObj.grade : 'N/A';
      return { ...student, grade };
    });
}
