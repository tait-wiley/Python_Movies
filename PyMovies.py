

movies = ["Wall-E (2008)",
"The Ring (2002)", 
"Minions (2015)", 
"The Mummy (1999)",
"Mean Girls (2004)",
"Million Dollar Baby (2004)",
"The Desolation of Smaug (2013)",
"Love Actually (2003)",
"Scarface (1983)",
"Oldboy (2003)", 
"Die Hard (1988)",
"The Bourne Identity (2002)",
"The Secret Life of Walter Mitty (2013)",
"The Incredibles (2004)",
"Battleship (2012)",
"The Strangers (2008)",
"Ratatouille (2007)",
"Toy Story (1995)",
"Dogville (2003)",
"Million Dollar Baby (2004)",
"The Desolation of Smaug (2013)",
"Love Actually (2003)",
"Scarface (1983)",
"Oldboy (2003)",
"Stalker (1979)",
"Up (2009)",
"Thor: Ragnarok (2017)",
"The Matrix Revolutions (2003)",
"What We Do in the Shadows (2014)",
"Deadpool (2016)"
]


all_ratings = [
[5,5,4,4,3,1,2,3,4,4,4,3,4,0,0,0,1,2,3,4,4,4,1,4,0,0,0,1,2,5],  
[5,0,1,2,3,1,2,3,4,4,4,5,4,2,1,0,1,2,0,5,0,4,1,4,2,0,0,1,0,5],  
[5,2,3,4,4,0,0,0,4,5,0,3,0,0,0,3,4,0,1,4,4,4,0,4,0,3,0,1,2,5],  
[5,0,4,0,0,4,2,3,0,0,4,0,3,0,1,0,1,2,3,0,2,0,1,0,0,0,4,0,1,5],  
[5,4,3,2,1,1,2,3,4,3,4,3,4,0,3,0,1,2,4,4,4,4,1,4,0,0,0,1,2,5],  
]


friend = 0
count = 0
fullCount = 0

while friend <= 4:
    for x in all_ratings[friend]:
        if x > 0:
            count += 1
        
    fullCount += count
    count = 0
    friend += 1

print('Each has seen an average of', fullCount/5, 'movies')

print('\nThe most popular movies  were:')

newMovies = movies[:]
for x in range(30):
    newMovies[x] = 0
    
friend = 0
listSpot = 0

while friend <= 4:
    for x in all_ratings[friend]:
        if x > 0:
            newMovies[listSpot] += 1
        listSpot += 1
    listSpot = 0
    friend += 1

listSpot = 0
for x in newMovies:
    if x == max(newMovies):
        print(movies[listSpot])
    listSpot += 1
        
print('\nThe least popular movies were:')

friend = 0
listSpot = 0
for x in range(30):
    newMovies[x] = 0

while friend <= 4:
    for x in all_ratings[friend]:
        if x == 0:
            newMovies[listSpot] += 1
        listSpot += 1
    listSpot = 0
    friend += 1


listSpot = 0
for x in newMovies:
    if x == max(newMovies):
        print(movies[listSpot])
    listSpot += 1


print('\nThe highest rated movies were:')


moviesTotal = movies[:]
for x in range(30):
    moviesTotal[x] = 0

avgCount = movies[:]
for x in range(30):
    avgCount[x] = 0

listSpot = 0
friend = 0
rating = 0

while rating < 30:
    while friend < 5:
        moviesTotal[listSpot] += all_ratings[friend][rating]
        if (all_ratings[friend][rating]) > 0:
            avgCount[listSpot] += 1
        friend += 1

    listSpot += 1
    friend = 0
    rating += 1


listSpot = 0
for x in avgCount:
    moviesTotal[listSpot] /= avgCount[listSpot]
    listSpot += 1

listSpot = 0
for x in moviesTotal:
    if x == max(moviesTotal):
        print(movies[listSpot])
    listSpot += 1

print('\nThe lowest rated movies were:')

moviesTotal = movies[:]
for x in range(30):
    moviesTotal[x] = 0

avgCount = movies[:]
for x in range(30):
    avgCount[x] = 0

listSpot = 0
friend = 0
rating = 0

while rating < 30:
    while friend < 5:
        moviesTotal[listSpot] += all_ratings[friend][rating]
        if (all_ratings[friend][rating]) > 0:
            avgCount[listSpot] += 1
        friend += 1

    listSpot += 1
    friend = 0
    rating += 1


listSpot = 0
for x in avgCount:
    moviesTotal[listSpot] /= avgCount[listSpot]
    listSpot += 1

listSpot = 0
for x in moviesTotal:
    if x == min(moviesTotal):
        print(movies[listSpot])
    listSpot += 1
        


    


