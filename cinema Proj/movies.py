import os

def ShowMovies():   
    movies = [
        "Jurassic Cabin", 
        "The Dark Night",
        "The Nightmare on First Street",
        "Quantum Mania",
        "The Game of Thorns",
        "The Shape of Time"
    ]
    #asking the user what movie they would like to see, then it would take them to their selected movie and save the choice to a reciept file (text)
    print("Which movie would you like to see")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie}")
    while True:
        try:
            Answer = int(input("please choose selected movies with numbers, (1-6): "))
            if Answer == 1:
                youMovie = movies[Answer - 1]
                print(f"Great! you chose: {youMovie}")
                with open("reciept.txt", "a") as file:
                    file.write(f"\nMovie: {youMovie}" + '\n')
                    break
                
        
            elif Answer == 2:
                youMovie = movies[Answer - 1]
                print(f"Great you chose: {youMovie}")
                with open("reciept.txt", "a") as file:
                    file.write(f"\nMovie: {youMovie}" + '\n')
                    break
                
        
            elif Answer == 3:
                youMovie = movies[Answer - 1]
                print(f"Great you chose: {youMovie}")
                with open("reciept.txt", "a") as file:
                    file.write(f"\nMovie: {youMovie}" + '\n')
                    break
                
            elif Answer == 4:
                youMovie = movies[Answer - 1]
                print(f"Great you chose: {youMovie}")
                with open("reciept.txt", "a") as file:
                    file.write(f"\nMovie: {youMovie}" + '\n')
                    break
                
            elif Answer == 5:
                youMovie = movies[Answer - 1]
                print(f"Great you chose: {youMovie}")
                with open("reciept.txt", "a") as file:
                    file.write(f"\nMovie: {youMovie}" + '\n')
                    break
                
            elif Answer == 6:
                youMovie = movies[Answer - 1]
                print(f"Great you chose: {youMovie}")
                with open("reciept.txt", "a") as file:
                    file.write(f"\nMovie: {youMovie}" + '\n')
                    break
                
            else:
                print("Please select using numbers one through six")
                continue
                
        except ValueError:
            print("Error")

        



    
