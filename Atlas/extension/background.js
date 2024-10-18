chrome.runtime.onInstalled.addListener(() => {
    console.log("AI Integration Extension Installed");
  });
  
  // Example to listen for a tab update event
  chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.active) {
      console.log('Tab updated:', tab.url);
    }
  });
  