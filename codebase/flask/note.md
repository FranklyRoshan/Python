
To generate a basic HTML structure (boilerplate) in Visual Studio Code, type an exclamation mark ! and press Enter or Tab.  This triggers Emmet, which expands the shortcut into the standard <!DOCTYPE html>, <html>, <head>, and <body> tags. 

For viewing the HTML source code of an existing webpage in any browser, press Ctrl + U (Windows/Linux) or Command + Option + U (Mac) to open the raw source in a new tab.

---

Running document.body.contentEditable = true in your Chrome browser console transforms the entire webpage into a live, editable document. This allows you to directly click on any text, image, or layout element and modify, rewrite, or delete it right on your screen.

How to Use It
Open Chrome DevTools by pressing F12 or Ctrl + Shift + J (Windows/Linux) / Cmd + Option + J (macOS).Click on the Console tab.
Paste the following line and press 
Enter:javascriptdocument.body.contentEditable = true

Use code with caution.
Close the console and click anywhere on the webpage to start typing, editing, or deleting text.

Key Use Cases
Quick Mockups: Test how a new headline or button label looks directly inside the live layout.
Clean Screenshots: Safely remove sensitive data, names, or clutter from a page before taking a screenshot
Layout Testing: See how the website layout handles much longer or shorter text blocks.

Important Caveats
Temporary Changes: All modifications happen exclusively in your browser's local memory. Refreshing the page will instantly wipe out your changes and restore the original website content.
Better Alternative: If you want to achieve the exact same effect but preserve native keyboard navigation tabs, you can also use document.designMode = "on" in the console.

Pro-Tip: The Bookmarklet Trick
If you use this feature frequently, you can save it as a bookmark to trigger it with a single click
Create a new bookmark in your browser toolbar.
Set the name to "Edit Page"
Paste this exact code snippet into the URL field:
javascriptjavascript:void(document.body.contentEditable=document.body.contentEditable==='true'?'false':'true');

---