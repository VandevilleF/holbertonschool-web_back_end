import { createClient } from "redis";

const client = createClient();

client.on('error' , err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const schools = {
  "Portland": "50",
  "Seattle": "80",
  "New York": "20",
  "Bogota": "20",
  "Cali": "40",
  "Paris": "2"
};

for (let city in schools) {
  client.hset('HolbertonSchools', city, schools[city], (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log('Reply: ', reply)
    }
  });
}


client.hgetall('HolbertonSchools', (err, value) => {
  if (err) {
    console.error(err);
  } else {
    console.log(value);
  }
});
