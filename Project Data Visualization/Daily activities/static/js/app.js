//app.js

const mysql = require('mysql');
const connection = mysql.createConnection({
  host: 'Local instance MySQL',
  user: 'root',
  password: 'Mun&maj@0723',
  database: 'activities_db'
});
connection.connect((err) => {
  if (err) throw err;
  console.log('Connected!');
});
