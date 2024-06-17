# Hello World Chrome Extension

This repository contains a simple Chrome extension that stores a value using the `chrome.storage` API and a Python script to fetch that value from the local LevelDB database on disk.

## Extension

The extension consists of the following files:

- `manifest.json`
- `background.js`
- `popup.html`
- `popup.js`

### manifest.json

```json
{
  "manifest_version": 3,
  "name": "Hello World Extension",
  "version": "1.0",
  "description": "A simple hello world Chrome extension.",
  "permissions": ["storage"],
  "background": {
    "service_worker": "background.js"
  },
  "action": {
    "default_popup": "popup.html"
  }
}
