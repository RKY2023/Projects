document.addEventListener('DOMContentLoaded', function () {
    var executeButton = document.getElementById('executeButton');
  
    executeButton.addEventListener('click', function () {
      // var script = 'D:\Work\HelpDesk\Windows\windows_crons\Ext2py.bat'; // Replace with your Python script
      
      var script = 'TrainTicketer.py';
      
      // Send the script to the background script for execution
      chrome.runtime.sendMessage({ script: script }, function (response) {
        console.log('Python script executed:', response);
      });
      
    });
  });
  // chrome.storage.local.get('scriptOutput', function (data) {
  //   var scriptOutput = data.scriptOutput;
  //   console.log('Python script output:', scriptOutput);
  //   // Handle the output here
  // });