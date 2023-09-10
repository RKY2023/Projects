// Establish a connection with the native messaging host
var port = chrome.runtime.connectNative('com.rk.Ext2py');

// Receive message from the extension popup
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
  console.log(message.script);
  if (message.script) {
    var scriptOutput = 'The output of the Python script';
    exec(`python "${script}"`, (error, stdout, stderr) => {
      console.log(error);
      console.log("\n-----");
      console.log(stdout);
      if (error) {
        console.error(`Error executing Python script: ${error}`);
        sendResponse({ error: error.message });
      } else {
        console.log(`Python script executed successfully`);
        // Process the stdout or any other output as needed
        sendResponse({ success: true, output: stdout });
      }
    });
    // Send the message to the native messaging host
    port.postMessage({ script: message.script });
  } else {
    sendResponse({ error: 'No script file provided.' });
  }
  // Listen for response from the native messaging host
  port.onMessage.addListener(function (response) {
    // Handle the response from the native messaging host
    console.log('Response from native messaging host:', response);
  });

  // Handle any errors with the native messaging host connection
  port.onDisconnect.addListener(function () {
    console.error('Native messaging host disconnected.');
  });
});

