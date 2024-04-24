#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');

function computeCompletedTasks (apiUrl) {
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode !== 200) {
      console.error(`Error: Received status code ${response.statusCode} from API`);
    } else {
      const taskData = JSON.parse(body);
      const completedTasksByUser = {};

      taskData.forEach(task => {
        if (task.completed) {
          const userId = task.userId;
          completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
        }
      });
      console.log(completedTasksByUser);
    }
  });
}

// Check if API URL is provided as a command-line argument
if (process.argv.length !== 3) {
  console.log('Usage: node script.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
computeCompletedTasks(apiUrl);
