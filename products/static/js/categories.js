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
    $.ajax({
        url: $("#categories").attr('data-categories-url'),
        dataType: 'json',
        success: function (data) {
            if (data.categories) {
                var data_json = $.parseJSON(data.categories);
                for (var i = 0; i < data_json.length; i++) {
                    var fields = data_json[i].fields;
                    var text = '<li><a href="{% url "products:products" %}?slug={0}">{1}</a></li>'.format(fields.slug, fields.title);
                    $("#categories").append(text);
                }
            }
        }
    });
});
