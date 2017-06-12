var https   = require("https");
var fs      = require("fs");
const path  = require('path');

function generateInvoice(invoice, filename, success, error) {
    var postData = JSON.stringify(invoice);
    var options = {
        hostname  : "invoice-generator.com",
        port      : 443,
        path      : "/",
        method    : "POST",
        headers   : {
            "Content-Type": "application/json",
            "Content-Length": Buffer.byteLength(postData)
        }
    };

    var file = fs.createWriteStream(filename);

    var req = https.request(options, function(res) {
        res.on('data', function(chunk) {
            file.write(chunk);
        })
        .on('end', function() {
            file.end();

            if (typeof success === 'function') {
                success();
            }
        });
    });
    req.write(postData);
    req.end();

    if (typeof error === 'function') {
        req.on('error', error);
    }
}

var file_path = process.argv.slice(2)[0];
var json_file = process.argv.slice(3)[0];

fs.readFile(json_file, 'utf8', function (err, data) {
    if (err) throw err;
    var invoice = JSON.parse(data);

    generateInvoice(invoice, file_path, function() {
        console.log("Saved invoice to:", file_path);
    }, function(error) {
        console.error(error);
    });
})
