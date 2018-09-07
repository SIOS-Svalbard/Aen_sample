/**
 * @file
 * Set behaviors related to dataTables Features.
 */

(function ($) {
  Drupal.behaviors.ForenaDatatablesFeatures = {
    attach: function (context, settings) {
      //See http://www.datatables.net for documentation
      $('.FrxTable table').dataTable({
        "sPaginationType": "full_numbers",
        "stateSave": true,
        "iDisplayLength": 100,
        "bSort": true,
        "aLengthMenu": [[50, 100, 200, 500, -1], [50, 100, 200, 500, "All"]],
        "ordering": true,
        "order":[[1,"desc"]] 
        });
    }
  };
  
})(jQuery);

