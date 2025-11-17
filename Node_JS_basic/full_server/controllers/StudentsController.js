const { readDatabase } = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    const dbFile = process.argv[2];

    try {
      const students = await readDatabase(dbFile);
      let response = 'This is the list of our students';

      const sortedFields = Object.keys(students).sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base' }));

      sortedFields.forEach((field) => {
        const list = students[field].join(', ');
        response += `\nNumber of students in ${field}: ${students[field].length}. List: ${list}`;
      });

      res.status(200).send(response);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const dbFile = process.argv[2];
    const { major } = req.params;

    if (!['CS', 'SWE'].includes(major)) {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const students = await readDatabase(dbFile);
      const list = students[major] || [];
      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
