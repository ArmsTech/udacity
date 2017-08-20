// globals: jQuery

import getMapLocations from 'js/mapLocations';

export default function mapViewModel () {
  this.mapLocations = getMapLocations();

  this.filterMapLocationsByText = function filterLocationsByText(text) {
    this.mapLocations.map((mapLocation) => {
      // Case-insensitive filtering
      let [mapLocationName, filterText] = [
        mapLocation.name, text].map((item) => item.toLowerCase());

      mapLocation.visible(mapLocationName.startsWith(filterText));
    });
  };

  this.showMapLocationDetails = function showLocationDetails() {
    console.log(this);
  };

  const $filterInput = $('#filterInput');

  $filterInput.keyup(() => {
    const inputText = $filterInput.val();
    this.filterMapLocationsByText(inputText);
  });
}
