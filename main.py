from Functions import *

points = [[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
points_cluster1 = []
points_cluster2 = []
points_cluster3 = []
init_data = initializer(points)
temporal_sequence_clusters = init_data['sequence_clusters']
sequence_clusters = []
condition = True


while condition:
    # Define new iterable
    if len(sequence_clusters) == 0:
        c1 = recalculate_centroid(init_data['points_cluster1'])
        c2 = recalculate_centroid(init_data['points_cluster2'])
        c3 = recalculate_centroid(init_data['points_cluster3'])
    else:
        c1 = recalculate_centroid(points_cluster1)
        c2 = recalculate_centroid(points_cluster2)
        c3 = recalculate_centroid(points_cluster3)
        sequence_clusters = []
        points_cluster1 = []
        points_cluster2 = []
        points_cluster3 = []

    for point in points:

        # Calculate distance
        distance_point_centroid1 = abs((point[0] - c1[0])) + abs((point[1] - c1[1]))
        distance_point_centroid2 = abs((point[0] - c2[0])) + abs((point[1] - c2[1]))
        distance_point_centroid3 = abs((point[0] - c3[0])) + abs((point[1] - c3[1]))

        # Set distances into Dictionary
        distances_point = {
            1: distance_point_centroid1,
            2: distance_point_centroid2,
            3: distance_point_centroid3
        }

        # Get min distance and set points to every cluster and sequence clusters
        if min(distances_point, key=distances_point.get) == 1:
            points_cluster1.append(point)
            sequence_clusters.append(1)
        elif min(distances_point, key=distances_point.get) == 2:
            points_cluster2.append(point)
            sequence_clusters.append(2)
        else:
            points_cluster3.append(point)
            sequence_clusters.append(3)

    if sequence_clusters == temporal_sequence_clusters:
        condition = False
    else:
        temporal_sequence_clusters = sequence_clusters

results = zip(points, sequence_clusters)

for result in results:
    print(f'The point {result[0]} is into cluster {result[1]}')

























