document.addEventListener("DOMContentLoaded", function () {
  var selectOption = document.getElementById("selectOption");
  var saveButton = document.getElementById("saveButton");
  var textInput = document.getElementById("textInput");
  var pasteButton = document.getElementById("pasteButton");

  // chrome.storage.local.get("selectedOption", function (data) {
  //   const selectedOption = data.selectedOption;
  //   if (selectedOption) {
  //     selectOption.value = selectedOption;
  //   }
  // });

  // saveButton.addEventListener("click", function () {
  //   const selectedOption = selectOption.value;
  //   chrome.storage.local.set({ selectedOption }, function () {
  //     chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  //       const tab = tabs[0];
  //       chrome.scripting.executeScript({
  //         target: { tabId: tab.id },
  //         function: setOptionValue,
  //         args: [selectedOption],
  //       });
  //     });
  //   });
  // });
  // Send a message to the background script to retrieve the selected option
  chrome.runtime.sendMessage({ action: "getSelectedOption" }, function (
    response
  ) {
    const selectedOption = response.selectedOption;
    if (selectedOption) {
      selectOption.value = selectedOption;
    }
  });

  saveButton.addEventListener("click", function () {
    const selectedOption = selectOption.value;

    // Send a message to the background script to save the selected option
    chrome.runtime.sendMessage({
      action: "setSelectedOption",
      selectedOption,
    });

    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      const tab = tabs[0];
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: setOptionValue,
        args: [selectedOption],
      });
    });
  });

  function setOptionValue(selectedOption) {
    // Your code to handle the selected option in the content script
    // For example, you can pass the value to the content script using chrome.runtime.sendMessage()
    chrome.runtime.sendMessage({ action: "setSelectedOption", selectedOption });
  }

  pasteButton.addEventListener("click", function () {
    const textToPaste = textInput.value;
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      const tab = tabs[0];
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: pasteText,
        args: [textToPaste],
      });
    });
  });

  function setOptionValue(selectedOption) {
    const options = document.getElementById("postform-expiration").options;
    for (let i = 0; i < options.length; i++) {
      if (options[i].value === selectedOption) {
        options[i].selected = true;
        break;
      }
    }
  }
  function pasteText(textToPaste) {
    const textarea = document.querySelector("textarea");
    textarea.value = textToPaste;
    const textarea2 = document.querySelector(".bootstrap-tagsinput input");
    textarea2.value = textToPaste;
  }
});
