console.log('非源码，仅用作演示。下载源码请访问：https://www.17sucai.com');"use strict";(function(){function a(f){return document.querySelector(f)}function e(f){f.preventDefault();alertify.reset()}function d(f){(c||function(){})("send","event","button","click","demo",f)}function b(h,f){var g=a(h);if(g){g.addEventListener("click",function(i){i.preventDefault();d(h);f()})}}var c=c||function(){};b("#alertify-alert",function(f){alertify.alert("This is an alert dialog");return false});b("#alertify-confirm",function(f){alertify.confirm("This is a confirm dialog",function(g){g.preventDefault();alertify.success("You've clicked OK")},function(g){g.preventDefault();alertify.error("You've clicked Cancel")})});b("#alertify-click-to-close",function(f){alertify.closeLogOnClick(true).log("Click me to close!")});b("#alertify-disable-click-to-close",function(f){alertify.closeLogOnClick(true).log("Click me to close!").closeLogOnClick(false).log("You can't click to close this!")});b("#alertify-reset",function(f){alertify.okBtn("Go For It!").reset(f).alert("Custom values were reset")});b("#alertify-log-template",function(f){alertify.setLogTemplate(function(g){return"log message: "+g}).log("This is the message")});b("#alertify-max-log-items",function(f){alertify.maxLogItems(1).log("This is the first message");setTimeout(function(){alertify.log("The second message will force the first to close.")},1000)});b("#alertify-prompt",function(f){alertify.defaultValue("Default value").prompt("This is a prompt dialog",function(h,g){g.preventDefault();alertify.success("You've clicked OK and typed: "+h)},function(g){g.preventDefault();alertify.error("You've clicked Cancel")})});b("#alertify-ajax",function(f){alertify.confirm("Confirm?",function(g){g.preventDefault();alertify.alert("Successful AJAX after OK")},function(g){g.preventDefault();alertify.alert("Successful AJAX after Cancel")})});b("#alertify-promise",function(f){if("function"!==typeof Promise){alertify.alert("Your browser doesn't support promises");return}alertify.confirm("Confirm?").then(function(g){g.event.preventDefault();alertify.alert("You clicked the "+g.buttonClicked+" button!")})});b("#alertify-notification",function(f){alertify.log("Standard log message")});b("#alertify-notification-html",function(f){alertify.log("<img src='https://placehold.it/256x128'><h3 class='font-18'>This is HTML</h3>")});b("#alertify-notification-callback",function(f){alertify.log("Standard log message with callback",function(g){g.preventDefault();alertify.log("You clicked the notification")})});b("#alertify-success",function(f){alertify.success("Success log message")});b("#alertify-success-callback",function(f){alertify.success("Standard log message with callback",function(){alertify.success("You clicked the notification")})});b("#alertify-error",function(f){alertify.error("Error log message")});b("#alertify-error-callback",function(f){alertify.error("Standard log message with callback",function(g){g.preventDefault();alertify.error("You clicked the notification")})});b("#alertify-delay",function(f){alertify.delay(10000).log("Hiding in 10 seconds")});b("#alertify-forever",function(f){alertify.delay(0).log("Will stay until clicked")});b("#alertify-labels",function(f){alertify.okBtn("Accept").cancelBtn("Deny").confirm("Confirm dialog with custom button labels",function(g){g.preventDefault();alertify.success("You've clicked OK")},function(g){g.preventDefault();alertify.error("You've clicked Cancel")})});b("#alertify-log-position",function(){alertify.delay(1000);alertify.log("Default bottom left position");setTimeout(function(){alertify.logPosition("top left");alertify.log("top left")},1500);setTimeout(function(){alertify.logPosition("top right");alertify.log("top right")},3000);setTimeout(function(){alertify.logPosition("bottom right");alertify.log("bottom right")},4500);setTimeout(function(){alertify.reset();alertify.log("Back to default")},6000)})})();console.log('非源码，仅用作演示。下载源码请访问：https://www.17sucai.com');