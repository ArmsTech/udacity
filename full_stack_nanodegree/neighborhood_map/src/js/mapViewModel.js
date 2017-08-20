// globals: jQuery

import getMapLocations from 'js/mapLocations';

export default function mapViewModel () {
  this.mapLocations = getMapLocations();

  this.filterMapLocationsByText = function filterLocationsByText(text) {
    this.mapLocations.map((mapLocation) => {
      mapLocation.visible(mapLocation.name.startsWith(text));
    });
  };
}
