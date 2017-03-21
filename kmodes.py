import numpy
# from kmodes import kprototypes
from kmodes import kmodes

columns = [
    "size",
    "sex",
    "age",
    "outdoorness",
    "fur length",
    "pawing at the door",
    "making muffins",
    "setting belly trap",
    "rubbing self on corners",
    "loving boxes",
    "contortionism",
    "drooling",
    "random sprinting",
    "loving oddly specific vegetarian foods",
    "hiding under the sheets",
    "preferring men",
    "attacking toes",
    "knocking things over",
    "loving keyboards",
    "staring intensely at the wall",
    "blep",
    "drinking from the faucet",
    "freaking out about half-empty food bowl",
    "standing on hind legs",
]

data = numpy.genfromtxt('data-clean.csv', delimiter=',', skip_header=1)

km = kmodes.KModes(n_clusters=4, init='Huang', n_init=5, verbose=1)

clusters = km.fit_predict(data)

# Print the cluster centroids
print(km.cluster_centroids_)

# kproto = kprototypes.KPrototypes(n_clusters=4, init='Cao', verbose=2)
# clusters = kproto.fit_predict(data, categorical=range(5, 24))
#
# # Print cluster centroids of the trained model.
# print(kproto.cluster_centroids_)
# # Print training statistics
# print(kproto.cost_)
# print(kproto.n_iter_)
