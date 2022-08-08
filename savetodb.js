const fs = require('fs');

const connectionString = process.env.DATABASE_URL;

const { Client } = require('pg');

const client = new Client({
  connectionString: connectionString,
  ssl: { rejectUnauthorized: false }
});


var storage;

try {
	storage = fs.readFileSync('./world.zip', { encoding: 'hex' });
  } catch(err) {
	console.log(err)
	return
  }
  //console.log(storage);
  client.connect();


const insertQuery = `
insert into files values('world.zip', bytea('`+ storage +`'))`;

const updateQuery = `
update files set file=bytea('`+ storage +`') where filename='world.zip'`;

const retreiveQuery = `
select convert_from(file, 'UTF-8') as file from files where filename='world.zip'`;

client.query(updateQuery, (err, res, fields) => {
    if (err) {
        console.error(err);
        return;
	}
  console.log('**script**: updated db')
  client.end();
});
