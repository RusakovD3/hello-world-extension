chrome.runtime.onInstalled.addListener(() => {
    chrome.storage.sync.set({ hello: 'world' }, () => {
      console.log('Value is set to "world".');
    });
  });
  