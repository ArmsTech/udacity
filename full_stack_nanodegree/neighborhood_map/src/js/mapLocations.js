import MapLocation from 'js/mapLocation';

const locations = [
{name: "Brendan"},
{name: "Brenda"},
{name: "Brend"},
{name: "Bren"}
];

export default function getMapLocations () {
  return locations.map((location) => {
    return new MapLocation(location);
  });
}
