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
        "ordering": true,
        "order":[[1,"desc"]] 
        });
    }
  };
  
})(jQuery);

