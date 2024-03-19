import spacy  
nlp = spacy.load('en_core_web_md')

watched_movie ='''Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator'''

model_description = nlp(watched_movie)  
most_similar = 0

movies_list = open("movies.txt") # Open TXT file with descriptions of movies 

# Read one line at a time in the TXT file to check similarity betweeen movies' descriptions and the model description

while True:
    
    content = movies_list.readline()
    if not content:
        movies_list.close()
        break

    title = content[0:7]
    description = content[9:]
    similarity = nlp(description).similarity(model_description)

    if similarity > most_similar:
       most_similar = similarity
       recommended_movie = title
       
print("We recommend you watching", recommended_movie, "which is the most similar to the movie you watched.")      