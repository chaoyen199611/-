var map = L.map('map').setView([22.63470, 120.28037], 12);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var locations = [
    ["壽山動物園停車場", 22.63470, 120.28037],
    ["凱旋青樹", 22.63832, 120.31768],
    ["中三經五路口", 22.72344, 120.30111],
    ["漯底山自然公園",22.77105, 120.25343]
    
    
    
];

for (var i = 0; i < locations.length; i++) {
    marker = new L.marker([locations[i][1], locations[i][2]])
      .bindPopup(locations[i][0])
      .addTo(map);
}
