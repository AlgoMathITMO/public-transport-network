# public-transport-network

Analysis of public transportation systems using network science.

## Raw data

The analysis is based on the public infrastructure data of St. Petersburg, Russia. The two sources of raw data are:

* `data/raw/spb_routes.csv` - data on public transport routes (bus, trolley, tram). Downloaded from [this page](http://data.gov.spb.ru/opendata/7830001067-routes_transport/).
* `data/raw/osm.zip`* - data from [OpenStreetMap](https://www.openstreetmap.org/). Downloaded via [Overpass API](https://overpass-turbo.eu/) using the following queries:
  1. St. Petersburg (relation [337422](https://www.openstreetmap.org/relation/337422)):
    ```
    [out:json];
    area(3600337422)->.a;
    (
      node(area.a);
      way(area.a);
      relation(area.a);
    );
    out;
    ```
  2. Leningrad oblast (relation [176095](https://www.openstreetmap.org/relation/176095)):
    ```
    [out:json];
    area(3600176095)->.a;
    (
      node(area.a);
      way(area.a);
      relation(area.a);
    );
    out;
    ```
  \* The file size is about 250 MB, therefore it cannot fit inside a Git repo. You can download it using [this Google Drive link](https://drive.google.com/drive/folders/1Z_oSs5Vk4LSxwjc10iVa9mazBvWHuCf6?usp=sharing).

## Further pipeline

All procedures are executed in the corresponding jupyter-notebooks (directory `pipeline/`) in the order suggested by their corresponding names (i.e. `pipeline/1_data-preprocessing.ipynb`).
