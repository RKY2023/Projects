
chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.tabs.executeScript(tabs[0].id, { file: 'content_script.js' }, function () {
      // Establish a connection with the content script here
    });
  });
function retrieveAndPrintText() {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.sendMessage(tabs[0].id, { action: "retrieveText" }, function (response) {
        if (response && response.textContent) {
          console.log("Text Content: ", response.textContent);
        } else {
          console.log("Element with ID 'test-text' not found.");
        }
      });
    });
  }
  
  chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    if (changeInfo.status === "complete") {
      retrieveAndPrintText();
    }
  });
  
  retrieveAndPrintText();