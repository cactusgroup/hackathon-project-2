//Lets require/import the HTTP module
var http = require('http');
var connect = require('connect');

var firebase = require('firebase');

firebase.initializeApp({
  serviceAccount: "/root/CUNYDiscourse/noteHarvest-b2f97dca9bcd.json",
  databaseURL: "https://noteharvest-c626c.firebaseio.com/"
});

var connect = require('connect');
var serveStatic = require('serve-static');
connect().use(serveStatic(__dirname)).listen(8080, function(){
    console.log('Server running on 8080...');
});