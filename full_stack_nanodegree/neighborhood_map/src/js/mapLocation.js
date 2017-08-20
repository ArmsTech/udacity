import * as ko from 'knockout';

class MapLocation {
  constructor(location, visible=true) {
    this.name = location.name;
    this.visible = ko.observable(visible);
  }
}

export default MapLocation;
