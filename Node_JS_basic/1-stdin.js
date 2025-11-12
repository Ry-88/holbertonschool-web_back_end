process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}\n`);
});

process.stdin.on('exit', () => {
  console.log('This important software is now closing');
});

process.on('SIGINT', () => {
  console.log('\nThis important software is now closing');
  process.exit();
});
