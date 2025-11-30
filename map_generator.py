import csv

html_head = """
<!DOCTYPE html>
<html>
<head>
    <title>Geotagged Drone Map</title>
    <meta charset="utf-8" />
    <style> #map { height: 90vh; width: 100%; } </style>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
</head>
<body>
<h2>Drone Image GPS Map</h2>
<div id="map"></div>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
var map = L.map('map').setView([22.4170, 82.0414], 16);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);
"""

html_points = ""

with open("output.csv", newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        lat = row["lat"]
        lon = row["lon"]
        file = row["file"]
        html_points += f"""
L.marker([{lat}, {lon}]).addTo(map)
.bindPopup("<b>{file}</b><br>Lat: {lat}<br>Lon: {lon}");
"""

html_end = """
</script>
</body>
</html>
"""

with open("map.html", "w", encoding="utf-8") as f:
    f.write(html_head + html_points + html_end)

print("✔ Map Generated: Open map.html")
