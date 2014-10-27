jQuery(document).ready(function($) {
    if ($('#id_date').length > 0) {
        $('#id_date').pickadate({
            selectYears: true,
            selectMonths: true,
            formatSubmit: 'yyyy-mm-dd',
            format: 'yyyy-mm-dd'
        });
    }

    if ($('.table-transactions').length > 0) {

        $('.table-transactions').dataTable();

    }
});
