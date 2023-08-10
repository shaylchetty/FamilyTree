class Member:
    def __init__(self, name, gender, mother=None, father=None, spouse=None, children=None, siblings=None):
        self.name = name
        self.gender = gender
        self.mother = mother
        self.father = father
        self.spouse = spouse
        self.children = children
        self.siblings = siblings

    def addSpouse(self, newSpouse):
        if newSpouse is None:
            return
        if self.spouse != newSpouse:
            self.spouse = newSpouse
            if(self.children is not None):
                for child in self.children:
                    self.spouse.addChild(child)
            if newSpouse.spouse != self:
                newSpouse.addSpouse(self)

    def addParent(self, newParent):
        if newParent is None:
            return
        if newParent.gender == 0:
            self.addMother(newParent)
        if newParent.gender == 1:
            self.addFather(newParent)

    def addMother(self, newMother):
        if self.mother != newMother:
            self.mother = newMother
            self.mother.addChild(self)
            if self.siblings is not None:
                for sib in self.siblings:
                    self.mother.addChild(sib)
    
    def addFather(self, newFather):
        if self.father != newFather:
            self.father = newFather
            self.father.addChild(self)
            if self.siblings is not None:
                for sib in self.siblings:
                    self.father.addChild(sib)

    def addSibling(self, newSibling):
        if newSibling == self:
            return
        if self.siblings is None:
            self.siblings = []
        if newSibling not in self.siblings:
            newSibling.addParent(self.mother)
            newSibling.addParent(self.father)
            if newSibling.siblings is None:
                newSibling.siblings = []
            if self not in newSibling.siblings:
                newSibling.siblings.append(self)
            for sib in self.siblings:
                newSibling.addSibling(sib)
            self.siblings.append(newSibling)



    def addChild(self, newChild):
        if self.children is None:
            self.children = []
        if newChild not in self.children:
            newChild.addParent(self)
            for sib in self.children:
                newChild.addSibling(sib)
            if newChild not in self.children:
                self.children.append(newChild)
            if self.spouse is not None:
                self.spouse.addChild(newChild)


    def getRels(self):
        rels = []
        types = [self.mother, self.father, self.spouse, self.siblings, self.children]
        if self.mother is not None:
            rels.append(self.mother)
        if self.father is not None:
            rels.append(self.father)
        if self.spouse is not None:
            rels.append(self.spouse)
        if self.siblings:
            rels.extend(self.siblings)
        if self.children:
            rels.extend(self.children)

        return rels

    def __str__(self) -> str:
        return self.name
    

    def __repr__(self) -> str:
        return self.name
    
    def __eq__(self, other):
        if isinstance(other, Member):
            return self.name == other.name and self.gender == other.gender
        return False
    
    def __hash__(self):
        return hash((self.name, self.gender))


if __name__ == "__main__":
    pass
   


