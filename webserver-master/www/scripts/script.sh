#!/bin/bash
#
# Generate HTNL for display.
#
printf "<!DOCTYPE html>
<html>
  <head>
    <meta charset=\"utf-8\">
    <title>WebServer Test Script</title>
  </head>
  <body>
    <p>Hello, world!</p>
    <pre>$*</pre>
  </body>
</html>
"


