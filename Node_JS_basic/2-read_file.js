const fs = require('fs');

function countStudents(path) {
  try {
    // Read file synchronously
    const data = fs.readFileSync(path, { encoding: 'utf-8' });
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Remove header
    const students = lines.slice(1);

    if (students.length === 0) {
      console.log('Number of students: 0');
      return;
    }

    console.log(`Number of students: ${students.length}`);

    // Object to store field groups
    const fields = {};

    for (const line of students) {
      const parts = line.split(',');

      if (parts.length >= 4) {
        const firstname = parts[0];
        const field = parts[3];

        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      }
    }

    // Log results per field
    for (const [field, list] of Object.entries(fields)) {
      console.log(
        `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
