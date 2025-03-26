const kue = require('kue');

const queue = kue.createQueue();

const job_data = {
  phoneNumber: "string",
  message: "string",
}

const job = queue.create('push_notification_code', {
  job_data
}).save((err) => {
  if (err) {
    console.log('Notification job failed');
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', (result) => {
  console.log('Notification job completed')
})
