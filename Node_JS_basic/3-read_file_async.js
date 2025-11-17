const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Read the file asynchronously
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split file content into lines, filter out empty lines
      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // Remove the header line
      lines.shift();

      // Initialize the structure to count students
      const students = {};
      let totalStudents = 0;

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (firstname && field) {
          totalStudents += 1;

          if (!students[field]) {
            students[field] = [];
          }

          students[field].push(firstname);
        }
      });

      // Log total number of students
      console.log(`Number of students: ${totalStudents}`);

      // Log the number of students and their names for each field
      for (const [field, names] of Object.entries(students)) {
        console.log(
          `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`,
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
