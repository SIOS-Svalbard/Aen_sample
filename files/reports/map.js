/**
 * @file
 * Set behaviors related to dataTables Features.


 (function ($) {
  Drupal.behaviors.ForenaMap = {
    attach: function (context, settings) {
      //See http://www.datatables.net for documentation
        /*var map = new OpenLayers.Map('map');
        var wms = new OpenLayers.Layer.WMS(
              "OpenLayers WMS",
              "https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv? ",
              {'layers':'GEBCO_LATEST'} );
        map.addLayer(wms);
          var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          })
        ],
        view: new ol.View({
          center: ol.proj.fromLonLat([37.41, 8.82]),
          zoom: 4
        })
      });
    }
  };
*/  
      //See http://www.datatables.net for documentation
        /*var map = new OpenLayers.Map('map');
        var wms = new OpenLayers.Layer.WMS(
              "OpenLayers WMS",
              "https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv? ",
              {'layers':'GEBCO_LATEST'} );
        map.addLayer(wms);
var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([37.41, 8.82]),
        zoom: 4
    })
});*/


(function ($) {
  Drupal.behaviors.ForenaDatatablesFeatures = {
    attach: function (context, settings) {
      //See http://www.datatables.net for documentation
      $('.sort table').dataTable({
        "stateSave": true,
        "sDom": '<"top"><"bottom"><"clear">',
        "iDisplayLength": -1,
        "bSort": true,
        "ordering": true,
        "order":[[0,"desc"]] 
        });
    }
  };

})(jQuery);
