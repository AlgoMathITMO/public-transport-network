from pathlib import Path

root_dir = Path(__file__).absolute().parent

data_dir = root_dir / 'data'

# raw data
raw_data_dir = data_dir / 'raw'
raw_osm_data_fpath = raw_data_dir / 'spb_osm.json.zip'
raw_routes_data_fpath = raw_data_dir / 'spb_routes.csv'

# preprocessed data
infrastructure_fpath = data_dir / 'infrastructure.json'
stops_fpath = data_dir / 'stops.json'
routes_fpath = data_dir / 'routes.json'

# supernodes
supernodes_fpath = data_dir / 'supernodes.json'

# supernode edges
edges_lspace_fpath = data_dir / 'edges_lspace.json'
edges_pspace_fpath = data_dir / 'edges_pspace.json'

# infrastructure attributes
supernode_attributes_fpath = data_dir / 'supernode_attributes.json'
