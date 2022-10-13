Unobtrusive JavaScript
----------------------

This directory contains four versions illustrating the path towards
unobtrusive JavaScript:

- [v0](v0) Is the first version where CSS, JS, and HTML are all mixed
           together in a single HTML file.
- [v0.5](v0.5) Registers the event handler in a script rather than in 
               the HTML tags.
- [v0.8](v0.8) Pulls styling into a separate file and makes sure to
               install the event handler only when the DOM is loaded.
- [v1](v1) Also pulls out the script into a separate file.