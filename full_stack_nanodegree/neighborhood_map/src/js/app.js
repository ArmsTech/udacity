import 'bootstrap/dist/css/bootstrap.min.css';
import * as ko from 'knockout';

import "css/style";
import initMap from 'js/googleMaps';
import mapViewModel from 'js/mapViewModel';

ko.applyBindings(new mapViewModel());

// Add initMap to global space for google api callback
window.initMap = initMap;
