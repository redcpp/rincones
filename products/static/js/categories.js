String.prototype.format = function()
{
   var content = this;
   for (var i=0; i < arguments.length; i++)
   {
        var replacement = '{' + i + '}';
        content = content.replace(replacement, arguments[i]);
   }
   return content;
};

$(document).ready(function () {
    var products_url = $("#categories").attr('products-url');
    $.ajax({
        url: $("#categories").attr('data-categories-url'),
        dataType: 'json',
        success: function (data) {
            if (data.categories) {
                var data_json = $.parseJSON(data.categories);
                for (var i = 0; i < data_json.length; i++) {
                    var fields = data_json[i].fields;
                    var text = '<li><a href="{0}?slug={1}">{2}</a></li>'.format(products_url, fields.slug, fields.title);
                    $("#categories").append(text);
                }
            }
        }
    });
});
