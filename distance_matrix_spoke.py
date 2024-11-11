import pandas as pd
import numpy as np
import googlemaps

API_KEY='YOUR_API_KEY_HERE'
gmaps = googlemaps.Client(key=API_KEY)

origins = [
    "Singapore 528765",
]

destinations = [
    "Singapore 458278",
    "Singapore 486442",
    "Singapore 529536",
    "Singapore 428802",
    "Singapore 427543",
    "Singapore 449269",
    "Singapore 519612",
    "Singapore 397693",
    "Singapore 530205",
    "Singapore 556083",
    "Singapore 339511",
    "Singapore 038983",
    "Singapore 545078",
    "Singapore 188024",
    "Singapore 018972",
    "Singapore 179103",
    "Singapore 307683",
    "Singapore 018984",
    "Singapore 307591",
    "Singapore 238839",
    "Singapore 807011",
    "Singapore 018935",
    "Singapore 239917",
    "Singapore 309433",
    "Singapore 239351",
    "Singapore 238859",
    "Singapore 238872",
    "Singapore 238801",
    "Singapore 237994",
    "Singapore 238879",
    "Singapore 259727",
    "Singapore 247933",
    "Singapore 098375",
    "Singapore 098537",
    "Singapore 259760",
    "Singapore 099253",
    "Singapore 289215",
    "Singapore 159953",
    "Singapore 268802",
    "Singapore 278967",
    "Singapore 275748",
    "Singapore 138617",
    "Singapore 138632",
    "Singapore 278628",
    "Singapore 597071",
    "Singapore 127371",
    "Singapore 678077",
    "Singapore 667979",
    "Singapore 658713",
]

# Split the destinations into two batches (25 destinations each)
batch1_destinations = destinations[:25]
batch2_destinations = destinations[25:]

# Function to make the API call and extract the distances
def get_distances(origins, destinations):
    matrix = gmaps.distance_matrix(origins, destinations, mode="driving")
    
    distances = []
    for row in matrix['rows']:
        distances.extend([element['distance']['value'] if element['status'] == 'OK' else None for element in row['elements']])
    return distances

# Get distances for batch 1 (first 25 destinations)
distances_batch1 = get_distances(origins, batch1_destinations)

# Get distances for batch 2 (remaining destinations)
distances_batch2 = get_distances(origins, batch2_destinations)

# Combine the distances from both batches
all_distances = distances_batch1 + distances_batch2

# Convert the distance matrix to a DataFrame
df = pd.DataFrame(all_distances, index=destinations, columns=origins)

# Save to CSV
df.to_csv('distances_from_spoke.csv', index=True)

print("Distance matrix saved to 'distances_from_spoke.csv'")