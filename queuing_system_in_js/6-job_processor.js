const kue = require('kue');

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.on('job enqueue', (id, type) => {
  if (type === 'push_notification_code') {
    kue.Job.get(id, (err, job) => {
      if (!err) {
        const { phoneNumber, message } = job.data.job_data;
        sendNotification(phoneNumber, message);
      } else {
        console.error(err);
      }
    });
  }
});
