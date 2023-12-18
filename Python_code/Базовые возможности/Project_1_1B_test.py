
import unittest
from unittest.mock import patch
from io import StringIO

class TestFullNameInitials(unittest.TestCase):
    
    @patch('builtins.input', return_value='Js')
    def test_short_name_input(self, mock_input):
        with self.assertRaises(ValueError) as context:
            full_name = input("Введите имя и фамилию: \n").title().split()
            if len(full_name) < 2:
                raise ValueError("Введите имя и фамилию раздельно через клавишу пробел!")
            first_name, last_name = full_name
            if len(first_name) < 3 or len(last_name) < 3:
                raise ValueError("Имя или фамилия слишком короткие!")
            initials = first_name[:3] + last_name[0]
            print(f"{first_name} {last_name}: {initials}")
        self.assertEqual(str(context.exception), "Введите имя и фамилию раздельно через клавишу пробел!")
        
    @patch('builtins.input', side_effect=['John Doe'])
    def test_valid_input(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            full_name = input("Введите имя и фамилию: \n").title().split()
            if len(full_name) < 2:
                raise ValueError("Введите имя и фамилию раздельно через клавишу пробел!")
            first_name, last_name = full_name
            if len(first_name) < 3 or len(last_name) < 3:
                raise ValueError("Имя или фамилия слишком короткие!")
            initials = first_name[:3] + last_name[0]
            print(f"{first_name} {last_name}: {initials}")
            self.assertEqual(mock_stdout.getvalue(), "John Doe: JohD\n")

if __name__ == '__main__':
    unittest.main(exit=False)