from member import Member
from collections import deque


if __name__ == "__main__":
    pass

ThaTha = Member("ThaTha", 1)
Aiya = Member("Aiya", 0)
Aja = Member("Aja", 1)
Aji = Member("Aji", 0)
Nim = Member("Nim", 0)
Kithen = Member("Kithen", 1)
Hiren = Member("Hiren", 1)
Nikita = Member("Nikita", 0)
Rowan = Member("Rowan", 1)
Kieran = Member("Kieran", 1)
Shayl = Member("Shayl", 1)
Dushen = Member("Dushen", 1)
Anita = Member("Anita", 0)
Diyashil = Member("Diyashil", 1)
Rushie = Member("Rushie", 0)
Bhavani = Member("Bhavani", 0)
Neelan = Member("Neelan", 1)
Rhoshni = Member("Rhoshni", 0)

ThaTha.addSpouse(Aiya)
ThaTha.addChild(Dushen)
ThaTha.addChild(Kithen)
ThaTha.addChild(Nim)
Aja.addSpouse(Aji)
Aja.addChild(Anita)
Aja.addChild(Hiren)
Dushen.addSpouse(Anita)
Dushen.addChild(Shayl)
Dushen.addChild(Kieran)
Dushen.addChild(Rowan)
Kithen.addChild(Diyashil)
Kithen.addChild(Rushie)
Nim.addSpouse(Neelan)
Bhavani.addSpouse(Kithen)
Hiren.addSpouse(Rhoshni)
Hiren.addChild(Nikita)



def bfs(start_member):
    visited = set()
    queue = deque([start_member])
    count = 0

    while queue:
        current_member = queue.popleft()

        if current_member not in visited:
            visited.add(current_member)

            relatives = current_member.getRels()
            for relative in relatives:
                queue.append(relative)
    return visited           

def sp(start_member):
    visited = set()
    queue = deque([start_member])
    my_dict = dict()
    my_dict[start_member] = 0


    while queue:
        current_member = queue.popleft()

        if current_member not in visited:
            visited.add(current_member)
            relatives = current_member.getRels()
            for relative in relatives:
                queue.append(relative)
                if relative not in my_dict or my_dict[relative] > my_dict[current_member] + 1:
                    my_dict[relative] = my_dict[current_member] + 1

    
    return my_dict




