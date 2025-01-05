class TreeNode:
    def __init__(self, name, data=None):
        self.name = name 
        self.data = data  
        self.children = []
    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.name) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


class CarRentalHierarchy:
    def __init__(self):
        self.root = TreeNode("Car Rental System")

    def add_branch(self, path, name, data=None):
     
    
        current_node = self.root
        for node_name in path:
            found = False
            for child in current_node.children:
                if child.name == node_name:
                    current_node = child
                    found = True
                    break
            if not found:
                new_node = TreeNode(node_name)
                current_node.add_child(new_node)
                current_node = new_node
        current_node.add_child(TreeNode(name, data))

    def __repr__(self):
        return repr(self.root)



if __name__ == "__main__":
    hierarchy = CarRentalHierarchy()

    
    hierarchy.add_branch([], "USA")
    hierarchy.add_branch(["USA"], "New York")
    hierarchy.add_branch(["USA", "New York"], "Manhattan Branch", data=["Toyota Corolla", "Ford Mustang"])
    hierarchy.add_branch(["USA", "New York"], "Brooklyn Branch", data=["Chevrolet Silverado", "Toyota Tacoma"])

    hierarchy.add_branch(["USA"], "California")
    hierarchy.add_branch(["USA", "California"], "Los Angeles Branch", data=["Toyota RAV4"])

    hierarchy.add_branch([], "Canada")
    hierarchy.add_branch(["Canada", "Toronto"],"Windsor Assembly", data=["Honda Civic", "Nissan Altima"])
    hierarchy.add_branch(["Canada", "Toroto"],"Brampton Assembly", data=["Honda Civic", "jeep copress"])

 
    print(hierarchy)
