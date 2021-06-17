from pathlib import Path

root_dir = Path(__file__).absolute().parent

data_dir = root_dir / 'data'

# raw data
raw_data_dir = data_dir / 'raw'
raw_osm_data_fpath = raw_data_dir / 'osm.zip'
raw_routes_data_fpath = raw_data_dir / 'spb_routes.csv'

# preprocessed data
preprocessed_dir = data_dir / 'preprocessed'
preprocessed_dir.mkdir(exist_ok=True)

infrastructure_fpath = preprocessed_dir / 'infrastructure.json'
stops_fpath = preprocessed_dir / 'stops.json'
routes_fpath = preprocessed_dir / 'routes.json'

# supernodes
supernodes_dir = data_dir / 'supernodes'
supernodes_dir.mkdir(exist_ok=True)

supernode_threshold_metrics_fpath = supernodes_dir / 'supernode_threshold_metrics.json'
supernodes_fpath = supernodes_dir / 'supernodes.json'

# supernode edges
edges_lspace_fpath = supernodes_dir / 'edges_lspace.json'

edges_pspace_alpha_metrics_fpath = supernodes_dir / 'edges_pspace_alpha_metrics.json'
edges_pspace_fpath = supernodes_dir / 'edges_pspace.json'

temp_dir = data_dir / 'temp'
temp_dir.mkdir(exist_ok=True)

# infrastructure attributes
supernode_attributes_fpath = supernodes_dir / 'supernode_attributes.json'

# supernode features
features_dir = data_dir / 'features'
features_dir.mkdir(exist_ok=True)

infrastructure_features_fpath = features_dir / 'infrastructure_features.json'
graph_features_fpath = features_dir / 'graph_features.json'

# clustering
clustering_dir = data_dir / 'clustering'
clustering_dir.mkdir(exist_ok=True)

supernode_clusters_fpath = clustering_dir / 'supernode_clusters.json'
