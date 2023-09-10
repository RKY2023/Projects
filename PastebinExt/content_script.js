// chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
//     if (request.action === "autoInput") {
//       const selectedOption = request.selectedOption;
//       if (selectedOption) {
//         const textarea = document.querySelector("textarea");
//         textarea.value = selectedOption;
//       }
//     }
//   });
  chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === "setSelectedOption") {
      const selectedOption = request.selectedOption;
      // Your code to handle the selected option in the content script
      const options = document.getElementById("selectOption").options;
        for (let i = 0; i < options.length; i++) {
            if (options[i].value === selectedOption) {
                options[i].selected = true;
                break;
            }
        }
    }
  });