import pandas as pd
import numpy as np
import googlemaps

API_KEY='YOUR_API_KEY_HERE'
gmaps = googlemaps.Client(key=API_KEY)

origins = [
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

# Set batch size for 100-element maximum
batch_size = 10
num_origins = len(origins)
num_destinations = len(destinations)

# Create an empty array to hold the full distance matrix
distance_matrix = np.zeros((num_origins, num_destinations))

# Loop over origins in batches
for i in range(0, num_origins, batch_size):
    origin_batch = origins[i:i+batch_size]
    
    # Loop over destinations in batches
    for j in range(0, num_destinations, batch_size):
        destination_batch = destinations[j:j+batch_size]
        
        # Request distance matrix for current batch of origins and destinations
        matrix = gmaps.distance_matrix(origin_batch, destination_batch, mode="driving")
        
        # Extract distances and fill in the matrix
        for k, row in enumerate(matrix['rows']):
            for l, element in enumerate(row['elements']):
                if element['status'] == 'OK':
                    distance_matrix[i+k, j+l] = element['distance']['value']
                else:
                    distance_matrix[i+k, j+l] = None  # Handle any unavailable distances

# Flip (transpose) the matrix
distance_matrix = distance_matrix.T

# Convert the transposed matrix to a DataFrame
df = pd.DataFrame(distance_matrix, index=destinations, columns=origins)

# Save to CSV
df.to_csv('distances.csv', index=True)

print("Distance matrix saved to 'distances.csv'")