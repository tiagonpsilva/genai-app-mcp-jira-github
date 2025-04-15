"""Implementação do conector MCP para Jira usando LlamaIndex."""

import os
from typing import Dict, List, Any, Optional

import requests
from jira import JIRA
from rich.console import Console

# Quando a implementação estiver completa, importaremos LlamaIndex:
# from llama_index import VectorStoreIndex, Document
# from llama_index.readers.jira import JiraReader

console = Console()

class JiraConnector:
    """Conector MCP para Jira usando LlamaIndex.
    
    Esta classe implementa a integração com o Jira através do protocolo MCP,
    utilizando LlamaIndex para indexar e consultar dados do Jira.
    """
    
    def __init__(self):
        """Inicializa o conector Jira com as credenciais das variáveis de ambiente."""
        self.jira_url = os.getenv("JIRA_URL")
        self.jira_username = os.getenv("JIRA_USERNAME")
        self.jira_api_token = os.getenv("JIRA_API_TOKEN")
        self.jira_project = os.getenv("JIRA_PROJECT")
        
        # Valida as credenciais
        if not all([self.jira_url, self.jira_username, self.jira_api_token, self.jira_project]):
            raise ValueError("Credenciais do Jira não configuradas corretamente.")
        
        # Inicializa o cliente Jira
        self.client = JIRA(
            server=self.jira_url,
            basic_auth=(self.jira_username, self.jira_api_token)
        )
        
        # Validação da conexão com o Jira
        try:
            self.client.projects()
            console.print("[green]Conexão com Jira estabelecida com sucesso![/green]")
        except Exception as e:
            raise ConnectionError(f"Erro ao conectar com o Jira: {str(e)}")
        
        # Em uma implementação completa, inicializaríamos o LlamaIndex aqui
        # self._initialize_index()
    
    def _initialize_index(self):
        """Inicializa o índice LlamaIndex com dados do Jira.
        
        Esta função será implementada futuramente para criar o índice vetorial
        com os dados do Jira usando LlamaIndex.
        """
        pass
        # Implementação futura usando LlamaIndex
        # reader = JiraReader(
        #     jira_client=self.client,
        #     project_name=self.jira_project
        # )
        # issues = reader.load_data()
        # documents = [Document(text=str(issue)) for issue in issues]
        # self.index = VectorStoreIndex.from_documents(documents)
    
    def get_issue(self, issue_key: str) -> Dict[str, Any]:
        """Obtém os detalhes de uma issue do Jira.
        
        Args:
            issue_key: Chave da issue no Jira (ex: PROJ-123)
            
        Returns:
            Dicionário com os detalhes da issue
        """
        try:
            issue = self.client.issue(issue_key)
            return {
                "key": issue.key,
                "summary": issue.fields.summary,
                "status": issue.fields.status.name,
                "assignee": issue.fields.assignee.displayName if issue.fields.assignee else "Não atribuído",
                "created": issue.fields.created,
                "updated": issue.fields.updated,
                "description": issue.fields.description or "Sem descrição"
            }
        except Exception as e:
            console.print(f"[bold red]Erro ao obter issue {issue_key}:[/bold red] {str(e)}")
            return {}
    
    def search_issues(self, jql: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Pesquisa issues no Jira usando JQL (Jira Query Language).
        
        Args:
            jql: Query JQL para pesquisa
            max_results: Número máximo de resultados
            
        Returns:
            Lista de issues encontradas
        """
        try:
            issues = self.client.search_issues(jql, maxResults=max_results)
            result = []
            
            for issue in issues:
                result.append({
                    "key": issue.key,
                    "summary": issue.fields.summary,
                    "status": issue.fields.status.name,
                    "assignee": issue.fields.assignee.displayName if issue.fields.assignee else "Não atribuído"
                })
            
            return result
        except Exception as e:
            console.print(f"[bold red]Erro ao pesquisar issues:[/bold red] {str(e)}")
            return []
    
    def process_query(self, query: str) -> str:
        """Processa uma consulta em linguagem natural sobre dados do Jira.
        
        Args:
            query: Consulta em linguagem natural
            
        Returns:
            Resposta processada para o usuário
        """
        # Implementação simplificada para demonstração
        # Em uma implementação completa, utilizaríamos LlamaIndex para processar a consulta
        
        # Alguns exemplos de consultas básicas que podemos tratar
        if "listar issues" in query.lower() or "mostrar issues" in query.lower():
            try:
                issues = self.search_issues(f"project = {self.jira_project}", max_results=5)
                if not issues:
                    return "Nenhuma issue encontrada no projeto."
                
                result = "[bold]Issues recentes no projeto:[/bold]\n\n"
                for issue in issues:
                    result += f"[blue]{issue['key']}[/blue]: {issue['summary']}\n"
                    result += f"Status: {issue['status']} | Responsável: {issue['assignee']}\n\n"
                
                return result
            except Exception as e:
                return f"[bold red]Erro ao listar issues:[/bold red] {str(e)}"
        
        elif "detalhes" in query.lower() and any(key in query for key in ["issue", "tarefa", "card"]):
            # Extrai a chave da issue da consulta (formato: PROJ-123)
            import re
            issue_key_match = re.search(r'([A-Z]+-\d+)', query)
            
            if issue_key_match:
                issue_key = issue_key_match.group(1)
                issue = self.get_issue(issue_key)
                
                if issue:
                    result = f"[bold blue]{issue['key']}[/bold blue]: {issue['summary']}\n\n"
                    result += f"Status: {issue['status']}\n"
                    result += f"Responsável: {issue['assignee']}\n"
                    result += f"Criado em: {issue['created']}\n"
                    result += f"Atualizado em: {issue['updated']}\n\n"
                    result += f"Descrição:\n{issue['description']}"
                    
                    return result
                else:
                    return f"Não foi possível encontrar a issue {issue_key}."
            else:
                return "Por favor, especifique a chave da issue (ex: PROJ-123)."
        
        # Resposta padrão para consultas não reconhecidas
        return """[yellow]Ainda não consigo processar esta consulta específica.[/yellow]
        
Consultas suportadas atualmente:
- "Listar issues do projeto"
- "Mostrar detalhes da issue PROJ-123"

Em breve teremos suporte para mais tipos de consultas!"""
