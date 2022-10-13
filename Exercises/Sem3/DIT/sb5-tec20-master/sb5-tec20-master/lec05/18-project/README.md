A minimal TypeScript project
----------------------------

This directory contains an example of a Node.js project implemented in TypeScript.

[tsconfig.json](tsconfig.json) contains an example TypeScript configuration produced by `tsc -init`.

To install the type definitions and make the VS Code warnings disappear run:
```
 $ npm install
```

Now you can compile the project with
```
 $ tsc 18-node-proj.ts
```
(or `npm run build`)

and run the resulting Node server JavaScript code as usual:
```
 $ node 18-node-proj.js
```