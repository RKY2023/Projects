chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === "retrieveText") {
    var element = document.getElementById('test-text');
    var textContent = null;
    if (element) {
      textContent = element.value;
    }
    sendResponse({ textContent: textContent });
  }
});