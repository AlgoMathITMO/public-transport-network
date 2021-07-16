from typing import Tuple

import numpy as np
import pandas as pd
from scipy import stats
from scipy.spatial import distance_matrix
from sklearn.cluster import KMeans
from tqdm import tqdm
from matplotlib import pyplot as plt

from ptn.utils import jaccard_coef


def kmeans_inertia(ar: np.ndarray, kmin: int = 2, kmax: int = 20) -> pd.Series:
    ks = np.arange(kmin, kmax + 1)
    inertia = []

    for k in tqdm(ks):
        kmeans = KMeans(n_clusters=k).fit(ar)
        inertia.append(kmeans.inertia_)

    return pd.Series(inertia, index=ks)


def dmdbscan(ar: np.ndarray, k: int = 3) -> np.ndarray:
    """Based on this paper:
        https://iopscience.iop.org/article/10.1088/1755-1315/31/1/012012/pdf
    """
    
    distances = distance_matrix(ar, ar)

    k_closest_distances = distances[
        np.arange(distances.shape[0]),
        distances.argsort(axis=0)[k],
    ]

    k_closest_distances.sort()
    
    return k_closest_distances


def match_clusters(clusters1: pd.Series, clusters2: pd.Series) -> Tuple[pd.Series, float]:
    clusters1_ids = {
        i: set(clusters1[clusters1 == i].index.tolist())
        for i in sorted(clusters1.unique())
    }

    clusters2_ids = {
        i: set(clusters2[clusters2 == i].index.tolist())
        for i in sorted(clusters2.unique())
    }

    assert len(clusters1_ids) == len(clusters2_ids)
    
    jaccard_coefs = np.array([
        [
            jaccard_coef(c1, c2)
            for c1 in clusters1_ids.values()
        ]
        for c2 in clusters2_ids.values()
    ])
    jaccard_coefs = pd.DataFrame(
        jaccard_coefs,
        index=list(clusters1_ids),
        columns=list(clusters2_ids),
    )

    score = jaccard_coefs.max(axis=1).min()
    
    permutation = {}

    for i, row in jaccard_coefs.iterrows():
        j = row.argmax()

        if j in permutation.values():
            raise ValueError

        permutation[i] = j
        
    return clusters2.apply(permutation.get), score



def plot_clusters(clusters: pd.Series, tsne: pd.DataFrame, coords: pd.DataFrame, cluster_names: dict):
    fig, axes = plt.subplots(ncols=2)
    fig.set_size_inches(8, 4)

    dfs = [tsne, coords]
    titles = ['(a)', '(b)']
    
    markers = ['o', 's', 'v', 'x', '+', '2']

    for ax, df, title in zip(axes, dfs, titles):
        for i in sorted(clusters.unique()):
            cluster = df[clusters == i]
            cluster_name = cluster_names[i]
            
            cluster_size = round(cluster.shape[0] / clusters.shape[0] * 100, 1)
            
            marker = markers[i % len(markers)]

            ax.scatter(
                *cluster.values.T,
                color=f'C{i}',
                marker=marker,
                s=1,
                label=f'{cluster_name} ({cluster_size}\% of nodes)',
            )

        ax.axis('off')
        ax.set_title(title, y=-0.05)

    axes[-1].legend(loc='upper left', bbox_to_anchor=(0.75, 1))


def plot_separate_clusters(
        features: pd.DataFrame,
        clusters: pd.Series,
        cluster_names: dict,
        ncols: int = 3,
):
    n_clusters = clusters.nunique()

    nrows = n_clusters // ncols + int(n_clusters % ncols > 0)

    fig, axes = plt.subplots(ncols=ncols, nrows=nrows)
    fig.set_size_inches(3 * ncols, 2.2 * nrows)
    fig.subplots_adjust(wspace=0.3, hspace=0.3)
    axes = axes.flatten()

    vmin = features.min().min()
    vmax = features.max().max()

    for i, ax in zip(sorted(clusters.unique()), axes):
        cluster = features[clusters == i]
        cluster_name = cluster_names[i]
        cluster_mean = cluster.mean(axis=0)
        
        cluster_size = round(cluster.shape[0] / clusters.shape[0] * 100, 1)

        legend = True

        for _, row in cluster.iterrows():
            # label = f'{cluster_name} ({cluster.shape[0]} nodes)' if legend else None
            # legend = False

            ax.plot(row, c=f'C{i}', lw=0.1)

        ax.plot(cluster_mean, c='k', ls='dashed', lw=1, zorder=2)
    
        ax.set_title(f'{cluster_name} ({cluster_size}\% of nodes)')
        
        ax.tick_params(labelbottom=False)
        ax.set_ylim(vmin, vmax)

        # ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.01))

    for i in range(n_clusters, len(axes)):
        axes[i].axis('off')


def get_one_vs_rest_cluster_statistics(
        features: pd.DataFrame,
        clusters: pd.Series,
) -> pd.DataFrame:
    unique_clusters = sorted(clusters.unique())

    one_vs_rest_cluster_statistics = pd.DataFrame(dtype=float, index=features.columns, columns=unique_clusters)

    for i in unique_clusters:
        mask = clusters == i

        for col in features.columns:
            s1 = features.loc[mask, col]
            s2 = features.loc[~mask, col]

            statistic = stats.ttest_ind(s1, s2, equal_var=False).statistic
            one_vs_rest_cluster_statistics.loc[col, i] = statistic

    return one_vs_rest_cluster_statistics


def plot_cluster_features(
        features: pd.DataFrame,
        clusters: pd.Series,
        cluster_names: dict,
        orient: str = 'v',
):
    mean = features.mean(axis=0)

    one_vs_rest_cluster_statistics = get_one_vs_rest_cluster_statistics(features, clusters)

    if orient == 'v':
        nrows = 2
        ncols = 1
        figsize = (0.35 * features.shape[1], 4)
    else:
        nrows = 1
        ncols = 2
        figsize = (0.35 * features.shape[1] * 2.2, 2)
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols)
    fig.set_size_inches(*figsize)
    fig.subplots_adjust(hspace=0.05, wspace=0.5)
    ax1, ax2 = axes.flatten()
    
    markers = ['o', 's', 'v', 'x', '+', '2']

    for i in sorted(np.unique(clusters)):
        mask = clusters == i
        cluster_name = cluster_names[i]
        cluster_mean = features[mask].mean(axis=0)
        
        marker = markers[i % len(markers)]
        
        cluster_size = round(mask.sum() / clusters.shape[0] * 100, 1)

        statistics = one_vs_rest_cluster_statistics[i]

        ax1.plot(cluster_mean.values, lw=1, c=f'C{i}', marker=marker, markersize=3)

        ax2.plot(statistics.values, lw=1, c=f'C{i}', marker=marker, markersize=3,
                 label=f'{cluster_name} ({cluster_size}\% of nodes)')

    ax1.plot(mean, c='k', lw=1, ls='dashed', label='mean')
    ax2.plot(mean * 0, lw=1, c='k', ls='dashed')

    columns = pd.Series(features.columns)

    for ax in [ax1, ax2]:
        ax.set_xticks(columns.index)
        ax.set_xticklabels(columns.values, rotation=45, ha='right')

    if orient == 'v':
        ax1.tick_params(bottom=False, labelbottom=False, labeltop=False)

    ax1.set_ylabel('feature means')
    ax2.set_ylabel('2-sample t-test statistics')

    if orient == 'v':
        ax2.legend(loc='center left', bbox_to_anchor=(1, 1))
    else:
        ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
