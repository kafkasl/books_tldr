# The Pragmatic Programmer

## Basic tools

### Achieving master with your text editor

What fluency looks like when editing text:

* When editing text, move and make selections by character, word, line, and paragraph.
* When editing code, move by various syntactic units (matching delimiters, functions, modules, ...).
* Reindent code following changes.
* Comment and uncomment blocks of code with a single command.
* Undo and redo changes.
* Split the editor window into multiple panels, and navigate between them.
* Navigate to a paritcular line number.
* Sort selected lines.
* Search for both strings and regular expressions, and repeat previous searches.
* Temporarily create multiple cursors based on a selection or on a pattern match, and edit the text at each in parallel.
* Display compilation errors in the current project.

Challenges to master text editing:

* No more autorepeat.
Everyone does it: you need to delete the last word you typed, so you press down on backspace and wait for autorepeat to kick in. In fact, we bet that your brain has done this so much that you can judge pretty much exactly when to release the key. 
So turn off autorepeat, and instead learn the key sequences to move, select, and delete by characters, words, lines, and blocks.

* This one is going to hurt.
Lose the mouse/trackpad. For one whole week, edit using just the keyboard. You'll discover a bunch of stuff that you can't do without pointing and clicking, so now's the time to learn. Keep notes (we recommend going old-school and using pencil and paper) of the key sequences you learn.
You'll take a productivity hit for a few days. But, as you learn to do stuff without moving your hands away from the home position, you'll find that your editing becomes faster and more fluent than it ever was in the past.

* Look for integrations. While writing this chapter, Dave wondered if he could preview the final layout (a PDF file) in an editor buffer. One download later, the layout is sitting alongside the original text, all in the editor. Keep a list of things you'd like to bring into your editor, then look for them.

* Somewhat more ambitiously, if you can't find a plugin or extension that does what you want, write one. Andy is fond of making custom, local file-based Wiki plugins for his favorite editors. If you can't find it, build it!

### Debugging checklist

* is the problem being reported a direct result of the underlying bug, or merely a symptom?
* Is the bug _really_ in the framework you're using? Is it in the OS? Or is it in your code?
* If you explained this problem in detail to a coworker, what would you say?
* If the suspect code passes its unit tests, are the tests complete enough? What happens if you run the the tests with _this_ data?
* Do the conditions that caused this bug exist anywhere else in the system? Are there other bugs still in the larval stage, just waiting to hatch?

### Binary chop

When facing a bug, chop in half the problem source to pinpoint where the problem comes from. Applies to many different situations, e.g.:

* Split a dataset in half until you find the part that introduces the bug.
* If there are multiple releases (or commits) between last known working version and the bug version, split the history in half until you find the offending change.
* If you have a huge stack trace, go to middle frame. Is the problem there already? Yes? Go up the stack trace. No? Go down. Repeat in any case until you find the offending frame.
