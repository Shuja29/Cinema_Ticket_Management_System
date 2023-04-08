movie = []
def addMovie():
    confirm = "y"
    while confirm =="y":
        serialno=eval(input("Enter serial no of respective movie:"))
        name = input("Enter name of movie:")
        genre = input("Enter genre of movie:")
        origin = input("Enter origin:")
        language = input("Enter language of movie:")
        movie.append(serialno)
        movie.append(name)
        movie.append(genre)
        movie.append(origin)
        movie.append(language)
        confirm = input("Do you want to add another record?")


def view_mov():
    print("Serial no\t\t""Name","\t\tGenre","\t\tOrigin","\t\tLanguage")
    for i in range(0,len(movie),5):
        print(format(movie[i],"5"), "\t", format(movie[i + 1],"8"), "\t",format(movie[i + 2],"8"), "\t", format(movie[i + 3],"8"),"\t", movie[i + 4])

def search_mov():
    serialno = eval(input("Enter the serial number of movie you want to search:"))
    print("Serial no\t\t Name", "\t\tGenre", "\t\tOrigin", "\t\tLanguage")
    for i in range(0,len(movie),5):
        if serialno == movie[i]:
            print(format(movie[i], "5"), "\t", format(movie[i + 1], "8"), "\t", format(movie[i + 2], "8"), "\t",format(movie[i + 3], "8"), "\t", movie[i + 4])
        if serialno not in movie:
            print("Record not found")
def update_mov():
      confirm ="y"
      while confirm =="y":
        serialno=eval(input("Enter serial no you want to update:"))
        for i in range (0,len(movie),5):
          if serialno==movie[i]:
           choice = input("What do you want to update? \nEnter the number corresponding to your choice: 1. Movie name 2. Genre 3. Origin 4. Language")
           if choice == "1":
               movie[i + 1] = input("Enter the new name of the movie :")
           elif choice == "2":
               movie[i + 2] = input("Enter updated genre :")
           elif choice == "3":
               movie[i + 3] = input("Enter updated origin :")
           elif choice == "4":
               movie[i + 4] = input("Enter updated language :")
           else:
               break
        confirm = input("Do you want to update another record :")
