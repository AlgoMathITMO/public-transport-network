# public-transport-network

Analysis of public transportation systems using network science.

## Raw data

The analysis is based on the public infrastructure data of St. Petersburg, Russia. There two sources of raw data are:

* `data/raw/spb_routes.csv` - data on public transport routes (bus, trolley, tram). Downloaded from [this page](http://data.gov.spb.ru/opendata/7830001067-routes_transport/).
* `data/raw/spb_osm.json.zip` - various data from [OpenStreetMap](https://www.openstreetmap.org/). Downloaded via [Overpass API](https://overpass-turbo.eu/) using the following query:
```
[out:json];
// area corresponding to relation: https://www.openstreetmap.org/relation/337422
area(3600337422)->.a;
(
  node(area.a);
  way(area.a);
  relation(area.a);
);
out;
```

## Further pipeline

All procedures are executed in the corresponding jupyter-notebooks (directory `notebooks/`) in the order suggested by their corresponding names (i.e. `notebooks/1_data-preprocessing.ipynb`).
