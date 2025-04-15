"""Testes para o módulo do conector Jira."""

import unittest
from unittest.mock import patch, MagicMock
import os

from mcp.jira.connector import JiraConnector


class TestJiraConnector(unittest.TestCase):
    """Testes para a classe JiraConnector."""
    
    @patch('os.getenv')
    @patch('jira.JIRA')
    @patch('rich.console.Console.print')
    def test_init_success(self, mock_print, mock_jira, mock_getenv):
        """Testa a inicialização bem-sucedida do conector Jira."""
        # Configura os mocks
        mock_getenv.return_value = 'dummy_value'
        mock_jira_instance = MagicMock()
        mock_jira.return_value = mock_jira_instance
        
        # Cria uma instância do conector
        connector = JiraConnector()
        
        # Verifica que o cliente Jira foi inicializado corretamente
        mock_jira.assert_called_once()
        self.assertEqual(connector.client, mock_jira_instance)
        
        # Verifica que a mensagem de sucesso foi exibida
        mock_print.assert_called_once()
    
    @patch('os.getenv')
    @patch('jira.JIRA')
    def test_init_missing_env_vars(self, mock_jira, mock_getenv):
        """Testa erro de inicialização quando faltam variáveis de ambiente."""
        # Configura o mock para retornar None para uma variável
        mock_getenv.side_effect = lambda x: None if x == 'JIRA_API_TOKEN' else 'dummy_value'
        
        # Verifica que um ValueError é lançado
        with self.assertRaises(ValueError):
            JiraConnector()
        
        # Verifica que o cliente Jira não foi inicializado
        mock_jira.assert_not_called()
    
    @patch('os.getenv')
    @patch('jira.JIRA')
    @patch('rich.console.Console.print')
    def test_get_issue_success(self, mock_print, mock_jira, mock_getenv):
        """Testa a função get_issue quando bem-sucedida."""
        # Configura os mocks
        mock_getenv.return_value = 'dummy_value'
        
        # Cria um mock para o cliente Jira e sua resposta
        mock_jira_instance = MagicMock()
        mock_issue = MagicMock()
        mock_issue.key = 'PROJ-123'
        mock_issue.fields.summary = 'Test Issue'
        mock_issue.fields.status.name = 'In Progress'
        mock_issue.fields.assignee.displayName = 'Test User'
        mock_issue.fields.created = '2023-01-01'
        mock_issue.fields.updated = '2023-01-02'
        mock_issue.fields.description = 'Test Description'
        
        mock_jira_instance.issue.return_value = mock_issue
        mock_jira.return_value = mock_jira_instance
        
        # Cria uma instância do conector e chama get_issue
        connector = JiraConnector()
        result = connector.get_issue('PROJ-123')
        
        # Verifica que o resultado contém os dados esperados
        self.assertEqual(result['key'], 'PROJ-123')
        self.assertEqual(result['summary'], 'Test Issue')
        self.assertEqual(result['status'], 'In Progress')
        self.assertEqual(result['assignee'], 'Test User')
        self.assertEqual(result['description'], 'Test Description')
    
    @patch('os.getenv')
    @patch('jira.JIRA')
    @patch('rich.console.Console.print')
    def test_search_issues_success(self, mock_print, mock_jira, mock_getenv):
        """Testa a função search_issues quando bem-sucedida."""
        # Configura os mocks
        mock_getenv.return_value = 'dummy_value'
        
        # Cria mocks para o cliente Jira e sua resposta
        mock_jira_instance = MagicMock()
        mock_issue1 = MagicMock()
        mock_issue1.key = 'PROJ-123'
        mock_issue1.fields.summary = 'Test Issue 1'
        mock_issue1.fields.status.name = 'In Progress'
        mock_issue1.fields.assignee.displayName = 'Test User 1'
        
        mock_issue2 = MagicMock()
        mock_issue2.key = 'PROJ-124'
        mock_issue2.fields.summary = 'Test Issue 2'
        mock_issue2.fields.status.name = 'Open'
        mock_issue2.fields.assignee.displayName = 'Test User 2'
        
        mock_jira_instance.search_issues.return_value = [mock_issue1, mock_issue2]
        mock_jira.return_value = mock_jira_instance
        
        # Cria uma instância do conector e chama search_issues
        connector = JiraConnector()
        result = connector.search_issues('project = PROJ')
        
        # Verifica que o resultado contém os dados esperados
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['key'], 'PROJ-123')
        self.assertEqual(result[0]['summary'], 'Test Issue 1')
        self.assertEqual(result[1]['key'], 'PROJ-124')
        self.assertEqual(result[1]['summary'], 'Test Issue 2')


if __name__ == '__main__':
    unittest.main()
