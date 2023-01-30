import git
from git import Repo

g = git.cmd.Git("C://Users/Erwin/Desktop/erwin/test") # sciezka do foledru git
# g.pull()

while True:
    print("=====================================")
    g.pull()

    print("Podaj numer zadania: ")
    numer=input()
    print("Podaj odpowiedz: ")
    odpowiedz=input()

    x = open("C://Users/Erwin/Desktop/test2/test/halo.txt", "w") #sciezka do pliku txt
    x.write(numer + "" +odpowiedz)
    x.close()

    repo = Repo("C://Users/Erwin/Desktop/test2/test")
    repo.git.add("halo.txt")
    repo.index.commit("udało się")
    origin = repo.remote(name='origin')
    origin.push()

# g.commit("elo")
# g.push()