document.addEventListener('DOMContentLoaded', () => {
    chrome.storage.sync.get('hello', (data) => {
      document.getElementById('value').innerText = `Stored value: ${data.hello}`;
    });
  });
  