"""Testes para o módulo CLI."""

import unittest
from unittest.mock import patch, MagicMock
import os
from io import StringIO
import sys

from cli.config import check_environment


class TestCliConfig(unittest.TestCase):
    """Testes para as funções de configuração da CLI."""
    
    @patch('os.getenv')
    @patch('rich.console.Console.print')
    def test_check_environment_all_vars_present(self, mock_print, mock_getenv):
        """Testa a função check_environment quando todas as variáveis estão presentes."""
        # Configura o mock para retornar valores não vazios para todas as variáveis
        mock_getenv.return_value = 'dummy_value'
        
        # Executa a função
        result = check_environment()
        
        # Verifica que a função retornou True
        self.assertTrue(result)
        
        # Verifica que a função Console.print não foi chamada (sem mensagens de erro)
        mock_print.assert_not_called()
    
    @patch('os.getenv')
    @patch('rich.console.Console.print')
    def test_check_environment_missing_vars(self, mock_print, mock_getenv):
        """Testa a função check_environment quando algumas variáveis estão ausentes."""
        # Configura o mock para retornar None para algumas variáveis
        def getenv_side_effect(var_name):
            if var_name == 'JIRA_URL' or var_name == 'JIRA_API_TOKEN':
                return None
            return 'dummy_value'
        
        mock_getenv.side_effect = getenv_side_effect
        
        # Executa a função
        result = check_environment()
        
        # Verifica que a função retornou False
        self.assertFalse(result)
        
        # Verifica que a função Console.print foi chamada pelo menos uma vez
        mock_print.assert_called()
        

if __name__ == '__main__':
    unittest.main()
