node_color = {
    'bus': 'C0',
    'trolley': 'C1',
    'tram': 'C2',
    'subway': 'C4',
}

node_marker = {
    'bus': 'o',
    'trolley': 'v',
    'tram': 's',
    'subway': 'X'
}

node_size = {
    'bus': 0.4,
    'trolley': 0.4,
    'tram': 0.4,
    'subway': 1,
}

edge_width = {
    'bus': 0.1,
    'trolley': 0.1,
    'tram': 0.1,
    'subway': 0.25,
}

edge_linestyle = {
    'bus': 'solid',
    'trolley': 'dashed',
    'tram': 'dotted',
    'subway': 'dashdot',
}

zorder = {
    'bus': 5,
    'trolley': 6,
    'tram': 7,
    'subway': 8,
}

supernode_color = 'C3'
supernode_marker = '*'
supernode_size = 2
superedge_width = 0.3
supernode_linestyle = 'solid'
supernode_zorder = 9

extent_whole = [28.98, 31.34, 59.53, 60.37]  # whole area
scale_whole = 9
factor_whole = 1

whole_area = (extent_whole, scale_whole, factor_whole)

extent_center = [30.17, 30.42, 59.91, 60.00]  # city center
scale_center = 12
factor_center = 3

city_center = (extent_center, scale_center, factor_center)

extent_vaska = [30.19, 30.32, 59.92, 59.96]  # vaska
scale_vaska = 13
factor_vaska = 5

vaska_area = (extent_vaska, scale_vaska, factor_vaska)


def get_node_props(t: str, factor: float) -> tuple:
    color = node_color[t]
    marker = node_marker[t]
    size = node_size[t] * factor
    width = edge_width[t] * factor
    linestyle = edge_linestyle[t]
    zorder_ = zorder[t]
    
    return color, marker, size, width, linestyle, zorder_


def get_supernode_props(factor: float) -> tuple:
    return (
        supernode_color,
        supernode_marker,
        supernode_size * factor,
        superedge_width * factor,
        supernode_linestyle,
        supernode_zorder,
    )
