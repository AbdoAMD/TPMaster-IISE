import unittest
from unittest.mock import patch
import os

# La fonction à tester
def log_error(message):
         
    import logging
    logging.error(message)

def read_file(file_path):
    """
    Tente de lire un fichier. Si le fichier n'est pas trouvé, lève une exception
    et enregistre l'erreur dans error.log.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        log_error(f"Le fichier '{file_path}' n'a pas été trouvé.")
        raise FileNotFoundError(f"Le fichier '{file_path}' n'a pas été trouvé.")

# Classe de tests unitaires
class TestFileFunctions(unittest.TestCase):

    def setUp(self):
        """Nettoie le fichier error.log avant chaque test."""
        if os.path.exists('error.log'):
            os.remove('error.log')

    def test_read_file_file_not_found(self):
        """Vérifie que FileNotFoundError est levée quand le fichier n'existe pas."""
        with self.assertRaises(FileNotFoundError):
            read_file('inexistant.txt')

    @patch('logging.error')  # Patch de la fonction logging.error pour tester qu'elle est appelée
    def test_log_error_called(self, mock_log_error):
        """Vérifie que log_error est appelé quand le fichier n'existe pas."""
        try:
            read_file('inexistant.txt')
        except FileNotFoundError:
            pass
        mock_log_error.assert_called_with("Le fichier 'inexistant.txt' n'a pas été trouvé.")

    def test_error_log_contains_error_message(self):
        """Vérifie que l'erreur est bien enregistrée dans le fichier error.log."""
        try:
            read_file('inexistant.txt')
        except FileNotFoundError:
            pass
        with open('error.log', 'r') as log_file:
            log_content = log_file.read()
            self.assertIn("Le fichier 'inexistant.txt' n'a pas été trouvé.", log_content)

if __name__ == '__main__':
    unittest.main()
