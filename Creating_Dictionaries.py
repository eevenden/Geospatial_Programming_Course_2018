#DC dictionary

Wards = {'Ward 1', 'Ward 2', 'Ward 3', 'Ward 4', 'Ward 5', 'Ward 6', 'Ward 7', 'Ward 8'}

Population = {'Ward 1': 82859, 'Ward 2': 77645, 'Ward 3': 83152, 'Ward 4': 83066, 'Ward 5': 82049, 'Ward 6': 84290, 'Ward 7': 73290, 'Ward 8': 81133}

Quadrants = {'Ward 1': 'NW', 'Ward 2': 'NW & SW', 'Ward 3': 'NW', 'Ward 4': 'NW & NE', 'Ward 5': 'NE', 'Ward 6': 'NE & SE', 'Ward 7': 'NE & SE', 'Ward 8': 'SE'}

Centroids = {'Ward 1': 'Long: 397275.23, Lat: 139739.35', 'Ward 2': 'Long: 396243.59, Lat: 136154.69', 'Ward 3': 'Long: 393151.59, Lat: 140946.12', 'Ward 4': 'Long: 397040.94, Lat: 143992.26', 'Ward 5': 'Long: 401259.80, Lat: 139729.13', 'Ward 6': 'Long: 399759.54, Lat: 135440.65', 'Ward 7': 'Long: 404524.96, Lat: 135462.35', 'Ward 8': 'Long: 399427.32, Lat: 130268.42'}

print '-' * 10
for ward in wards.items():
 print "%s has a population of %d, is in quadrant(s) %s, and has centroid coordinates of %s." % (ward, population, quadrant, centroid)