class Phonebook:

    def __init__(self):
        self.entries = {'JOAO ANTONIO': '199', 'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """

        if name is not None and number is not None:
            if isinstance(name, str) and isinstance(number, str):
                if name.isspace() is True:
                    return 'Nome invalido'
                if number.isspace() is True:
                    return 'Numero invalido'
                if number.isalpha() is True:
                    return 'Numero invalido'

                if '#' in name:
                    return 'Nome invalido'
                if '@' in name:
                    return 'Nome invalido'
                if '!' in name:
                    return 'Nome invalido'
                if '$' in name:
                    return 'Nome invalido'
                if '%' in name:
                    return 'Nome invalido'

                if name in self.entries:
                    return 'Nome já existe'
                else:
                    self.entries[name] = number
                    return 'Numero adicionado'

            else:
                if not isinstance(name, str):
                    return 'Nome invalido'
                if not isinstance(number, str):
                    return 'Numero invalido'
        else:
            if name is None:
                return 'Nome invalido'
            if number is None:
                return 'Numero invalido'



    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if name is not None:
            if isinstance(name, str):
                if name.isspace() is True:
                    return 'Nome invalido'

                if '#' in name:
                    return 'Nome invalido'
                if '@' in name:
                    return 'Nome invalido'
                if '!' in name:
                    return 'Nome invalido'
                if '$' in name:
                    return 'Nome invalido'
                if '%' in name:
                    return 'Nome invalido'

                return self.entries[name]

            else:
                if not isinstance(name, str):
                    return 'Nome invalido'
        else:
            if name is None:
                return 'Nome invalido'



    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return self.entries

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return self.entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        self.entries.pop(name)
        return 'Numero deletado'

#Incluindo a atividade com TDD

    def change_number(self, name, new_number):
        """
                changes the number of an existing name
                :param name: String with name
                :param new_number: number of person in string
                :return: 'Nome invalido' or 'Numero invalido' or 'Nome nao encontrado' or 'Numero alterado'
                """
        if name is not None and new_number is not None:
            if isinstance(name, str) and isinstance(new_number, str):
                if name.isspace() is True:
                    return 'Nome invalido'
                if new_number.isspace() is True:
                    return 'Numero invalido'
                if new_number.isalpha() is True:
                    return 'Numero invalido'

                if '#' in name:
                    return 'Nome invalido'
                if '@' in name:
                    return 'Nome invalido'
                if '!' in name:
                    return 'Nome invalido'
                if '$' in name:
                    return 'Nome invalido'
                if '%' in name:
                    return 'Nome invalido'

                if name not in self.entries:
                    return 'Nome nao encontrado'
                else:
                    self.entries[name] = new_number
                    return 'Numero alterado'

            else:
                if not isinstance(name, str):
                    return 'Nome invalido'
                if not isinstance(new_number, str):
                    return 'Numero invalido'
        else:
            if name is None:
                return 'Nome invalido'
            if new_number is None:
                return 'Numero invalido'

    def get_name_by_number(self, search_number):
        """
                search a name with a given number associate
                :param search_number: number of person in string
                :return 'Numero invalido' or 'Nome nao encontrado' or '{name} encontrado'
                """
        if search_number is not None:
            if isinstance(search_number, str):
                if search_number.isspace() is True:
                    return 'Numero invalido'
                if search_number.isalpha() is True:
                    return 'Numero invalido'
                for name, number in self.entries.items():
                    if search_number in number:
                        return f'{name} encontrado'
                else:
                    return 'Nome nao encontrado'
            else:
                if not isinstance(search_number, str):
                    return 'Numero invalido'
        else:
            if search_number is None:
                return 'Numero invalido'
