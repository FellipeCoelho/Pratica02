from src.phonebook import Phonebook


class TestPhonebook:

    # Testes Nome
    def test_add_name_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Numero adicionado"

        response = phonebook.add("Ana", "8199999999")

        assert expected_response == response

    def test_add_name_invalid_1_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.add("#Ana", "8199999999")

        assert expected_response == response

    def test_add_name_invalid_2_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.add("@Ana", "8199999999")

        assert expected_response == response

    def test_add_name_invalid_3_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.add("!Ana", "8199999999")

        assert expected_response == response

    def test_add_name_invalid_4_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.add("$Ana", "8199999999")

        assert expected_response == response

    def test_add_name_invalid_5_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.add("%Ana", "8199999999")

        assert expected_response == response

    def test_add_name_invalid_type_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.add(1234567, "8199999999")

        assert expected_response == response

    def test_add_name_exists_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Nome já existe"
        phonebook.add("Ana", "8199999999")

        response = phonebook.add("Ana", "8199999999")

        assert expected_response == response

    def test_add_name_blank_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.add(" ", "8199999999")

        assert expected_response == response

    def test_add_name_none_number_valid(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.add(None, "8199999999")

        assert expected_response == response

    # Testes Numero

    def test_add_name_valid_number_blank(self):
        phonebook = Phonebook()
        expected_response = "Numero invalido"

        response = phonebook.add("Ana", " ")

        assert expected_response == response

    def test_add_name_valid_number_none(self):
        phonebook = Phonebook()
        expected_response = "Numero invalido"

        response = phonebook.add("Ana", None)

        assert expected_response == response

    def test_add_name_valid_number_char(self):
        phonebook = Phonebook()
        expected_response = "Numero invalido"

        response = phonebook.add("Ana", "ABCDEF")

        assert expected_response == response

    def test_add_name_valid_number_type(self):
        phonebook = Phonebook()
        expected_response = "Numero invalido"

        response = phonebook.add("Ana", 888888888)

        assert expected_response == response

    # Testes Lookup

    def test_lookup_name_valid(self):
        phonebook = Phonebook()
        expected_response = '190'

        response = phonebook.lookup("POLICIA")

        assert expected_response == response

    def test_lookup_name_invalid_1(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.lookup("#Ana")

        assert expected_response == response

    def test_lookup_name_invalid_2(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.lookup("@Ana")

        assert expected_response == response

    def test_lookup_name_invalid_3(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.lookup("!Ana")

        assert expected_response == response

    def test_lookup_name_invalid_4(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.lookup("$Ana")

        assert expected_response == response

    def test_lookup_name_invalid_5(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.lookup("%Ana")

        assert expected_response == response

    def test_lookup_name_blank(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.lookup(" ")

        assert expected_response == response

    def test_lookup_name_none(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.lookup(None)

        assert expected_response == response

    def test_lookup_name_invalid(self):
        phonebook = Phonebook()
        expected_response = "Nome invalido"

        response = phonebook.lookup(12345)

        assert expected_response == response

    # Testes Get Name

    def test_get_name(self):
        phonebook = Phonebook()
        expected_response = 'POLICIA'

        response = phonebook.get_names()

        assert expected_response == response

    # Testes Get Number

    def test_get_number(self):
        phonebook = Phonebook()
        expected_response = '190'

        response = phonebook.get_numbers()

        assert expected_response == response

    # Testes Clear

    def test_clear(self):
        phonebook = Phonebook()
        expected_response = 'phonebook limpado'

        response = phonebook.clear()

        assert expected_response == response

    # Testes Search

    def test_search_sucess(self):
        phonebook = Phonebook()
        expected_response = [{'POLICIA', '190'}]

        response = phonebook.search('POLICIA')

        assert expected_response == response

    def test_search_none(self):
        phonebook = Phonebook()
        expected_response = []

        response = phonebook.search('Patrício')

        assert expected_response == response

    # Testes delete

    def test_search_none(self):
        phonebook = Phonebook()
        expected_response = 'Numero deletado'

        response = phonebook.delete('POLICIA')

        assert expected_response == response

    # TDD change number

    def test_change_number_valid(self):
        phonebook = Phonebook()
        expected_response = 'Numero alterado'

        response = phonebook.change_number('POLICIA', '193')

        assert expected_response == response

    def test_change_number_name_not_found(self):
        phonebook = Phonebook()
        expected_response = 'Nome nao encontrado'

        response = phonebook.change_number('Patricio', '193')

        assert expected_response == response

    def test_change_number_invalid_name_1(self):
        phonebook = Phonebook()
        expected_response = 'Nome invalido'

        response = phonebook.change_number('#POLICIA', '193')

        assert expected_response == response

    def test_change_number_invalid_name_2(self):
        phonebook = Phonebook()
        expected_response = 'Nome invalido'

        response = phonebook.change_number('@POLICIA', '193')

        assert expected_response == response

    def test_change_number_invalid_name_3(self):
        phonebook = Phonebook()
        expected_response = 'Nome invalido'

        response = phonebook.change_number('!POLICIA', '193')

        assert expected_response == response

    def test_change_number_invalid_name_4(self):
        phonebook = Phonebook()
        expected_response = 'Nome invalido'

        response = phonebook.change_number('$POLICIA', '193')

        assert expected_response == response

    def test_change_number_invalid_name_5(self):
        phonebook = Phonebook()
        expected_response = 'Nome invalido'

        response = phonebook.change_number('%POLICIA', '193')

        assert expected_response == response

    def test_change_number_blank_name(self):
        phonebook = Phonebook()
        expected_response = 'Nome invalido'

        response = phonebook.change_number(' ', '193')

        assert expected_response == response

    def test_change_number_null_name(self):
        phonebook = Phonebook()
        expected_response = 'Nome invalido'

        response = phonebook.change_number(None, '193')

        assert expected_response == response

    def test_change_number_invalid_type_name(self):
        phonebook = Phonebook()
        expected_response = 'Nome invalido'

        response = phonebook.change_number(123, '193')

        assert expected_response == response

    def test_change_number_invalid_blank(self):
        phonebook = Phonebook()
        expected_response = 'Numero invalido'

        response = phonebook.change_number('POLICIA', ' ')

        assert expected_response == response

    def test_change_number_invalid_name(self):
        phonebook = Phonebook()
        expected_response = 'Numero invalido'

        response = phonebook.change_number('POLICIA', None)

        assert expected_response == response

    def test_change_number_invalid_type(self):
        phonebook = Phonebook()
        expected_response = 'Numero invalido'

        response = phonebook.change_number('POLICIA', 123)

        assert expected_response == response

    def test_change_number_invalid_string(self):
        phonebook = Phonebook()
        expected_response = 'Numero invalido'

        response = phonebook.change_number('POLICIA', 'ABCDE')

        assert expected_response == response

    #TDD get name by number

    def test_get_name_by_number_valid(self):
        phonebook = Phonebook()
        expected_response = 'POLICIA encontrado'

        response = phonebook.get_name_by_number('190')

        assert expected_response == response

    def test_get_name_by_number_not_found(self):
        phonebook = Phonebook()
        expected_response = 'Nome nao encontrado'

        response = phonebook.get_name_by_number('193')

        assert expected_response == response

    def test_get_name_by_number_invalid_type(self):
        phonebook = Phonebook()
        expected_response = 'Numero invalido'

        response = phonebook.get_name_by_number(123)

        assert expected_response == response

    def test_get_name_by_number_invalid_string(self):
        phonebook = Phonebook()
        expected_response = 'Numero invalido'

        response = phonebook.get_name_by_number('ABC')

        assert expected_response == response

    def test_get_name_by_number_none(self):
        phonebook = Phonebook()
        expected_response = 'Numero invalido'

        response = phonebook.get_name_by_number(None)

        assert expected_response == response

    def test_get_name_by_number_blank(self):
        phonebook = Phonebook()
        expected_response = 'Numero invalido'

        response = phonebook.get_name_by_number(' ')

        assert expected_response == response