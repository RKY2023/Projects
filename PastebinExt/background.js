// let selectedOption = "";
// chrome.action.onClicked.addListener(function (tab) {
//     chrome.action.setPopup({ tabId: tab.id, popup: "popup.html" });
//   });
  chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === "getSelectedOption") {
      chrome.storage.local.get("selectedOption", function (data) {
        sendResponse({ selectedOption: data.selectedOption });
      });
      return true;
    } else if (request.action === "setSelectedOption") {
      chrome.storage.local.set({ selectedOption: request.selectedOption });
    }
  });
  
  chrome.action.onClicked.addListener(function (tab) {
    chrome.action.setPopup({ tabId: tab.id, popup: "popup.html" });
  });