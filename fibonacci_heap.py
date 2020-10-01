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
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass


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
        def insert_node(self, value):
        nouvel_arbre = ArbreFibo(value)
        self.arbres.append(nouvel_arbre)
        if (self.least is None or value < self.least.value):
            self.least = nouvel_arbre
        self.count = self.count + 1

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        def get_min(self):
        if self.least is None:
            return None
        return self.least.value

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        def extract_min(self):
        plus_petit = self.least
        if plus_petit is not None:
            for nouveau in plus_petit.nouveau:
                self.arbres.append(nouveau)
            self.arbres.remove(plus_petit)
            if self.arbres == []:
                self.least = None
            else:
                self.least = self.arbres[0]
                self.consolidate()
            self.count = self.count - 1
            return plus_petit.value

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        pass
