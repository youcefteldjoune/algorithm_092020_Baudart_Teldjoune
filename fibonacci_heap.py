class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.

    https://en.wikipedia.org/wiki/Heap_(data_structure)

    CETTE CLASSE JUSTE POUR L'AUTOCOMPLETION DE VOTRE EDITEUR
    NE VOUS EN OCCUPER PAS
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        def insert(self, value):
        i = 0
        while i <= len(self.trees):
            self.trees.append([value])
            break
        print("insert success")
        return self.trees

    def find_min(self):
        array_min = []
        for val in self.trees:
            array_min.append(val)
        a = sorted(array_min)
        print("le minimum est trouver")
        return a[0]

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        def delete_min(self):
        x = self.find_min()
        for v in self.trees:
            if x == v:
                min = v
                self.trees.remove(v)
                print("le minimum est suprimer")
                # print(min[0])
                return min[0]
        
       


    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        def merge(self):
        delete = self.delete_min()
        # print(delete)
        # print(self.trees)
        for o in self.trees:
            x = len(o)
            for v in self.trees:
                y = len(v)
                if x == y:
                    self.trees[0].append(delete)
            print("merge success")
            return None


class FibonacciHeap(Heap):
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement

    https://en.wikipedia.org/wiki/Fibonacci_heap

    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
    def insert(self, value):
        i = 0
        while i <= len(self.trees):
            self.trees.append([value])
            break
        print("insert success")
        return self.trees

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
       def find_min(self):
        array_min = []
        for val in self.trees:
            array_min.append(val)
        a = sorted(array_min)
        print("le minimum est trouver")
        return a[0]

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        def delete_min(self):
        x = self.find_min()
        for v in self.trees:
            if x == v:
                min = v
                self.trees.remove(v)
                print("le minimum est suprimer")
                # print(min[0])
                return min[0]

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        def merge(self):
        delete = self.delete_min()
        # print(delete)
        # print(self.trees)
        for o in self.trees:
            x = len(o)
            for v in self.trees:
                y = len(v)
                if x == y:
                    self.trees[0].append(delete)
            print("merge success")
            return None
