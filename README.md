# Soluvas Open Data

Open Data collections for common purposes.

**Encoding**: Some Open Data we found have mixed encoding, usually `Windows-1252`. In our data sets everything is in `UTF-8`.

**Metadata**: All data is described using [Data Packages](http://specs.frictionlessdata.io/data-packages/), specifically [Tabular Data Packages](http://specs.frictionlessdata.io/tabular-data-package/) for CSV files.

## Jakarta Smart City

Source: http://smartcity.jakarta.go.id

* `kecamatan.all.json` is retrieved from http://api.jakarta.go.id/v1/kecamatan?shape=true then converted to CSV using https://konklone.io/json/ 
* `rumahsakitumum.all.json` is retrieved from http://api.jakarta.go.id/v1/rumahsakitumum?shape=true then converted to CSV using https://konklone.io/json/
