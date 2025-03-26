import { createClient } from "redis";
const { promisify } = require('util');

const client = createClient();

client.on('error' , err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log('Reply: ', reply);
    }
  });
}

async function displaySchoolValue(schoolName) {
  // convert client.get to a promise
  // With the bind() method, an object can borrow a method from another object.
  const getAsynch = promisify(client.get).bind(client);
  try {
    const value = await getAsynch(schoolName);
    console.log(value);
  } catch (err) {
    console.error(err);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
