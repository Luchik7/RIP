$(function() {
    var $from = $('.from');
    var $to = $('.to');
    var $function = $('.function');
    var $button = $('.graph');
    var $output = $('.output');

    const delta = 0.1;
    let graph_legend = [];
    let color = 1;

    $button.on('click', function (e) {
        e.preventDefault();

        let from = parseFloat($from.val());
        let to = parseFloat($to.val());
        let x = from;
        let arraylen = ((to - from) / delta) + 1;

        let points = new Array(arraylen);
        for ( let i = 0; i < arraylen; i++ ) {
            points[i] = new Array(2);
        }

        let i = 0;
        while (i < arraylen) {
            const y = eval($function.val());
            points[i][0] = x;
            points[i][1] = y;
            i = i + 1;
            x = x + delta;
        }

        var graph = {};
        graph['label'] = $function.val();
        graph['color'] = color;
        color = color + 1;
        graph['data'] = points;
        graph_legend.push(graph);

        $.plot($output, graph_legend, {});
    });

});


