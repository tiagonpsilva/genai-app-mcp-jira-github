"""Interface de linha de comando interativa para o GenAI App."""

import os
import sys
from typing import Optional, List, Dict, Any

import typer
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print as rprint

from cli.config import check_environment
from mcp.jira.connector import JiraConnector

# Cria instâncias para a CLI
app = typer.Typer(
    name="GenAI Jira GitHub",
    help="Interface de linha de comando para consultas integradas entre Jira e GitHub"
)
console = Console()

def display_welcome():
    """Exibe mensagem de boas-vindas e informações sobre a aplicação."""
    rprint(Panel.fit(
        """[bold green]GenAI App - Integração Jira e GitHub via MCP[/bold green]
        
[yellow]Uma aplicação para consulta integrada de dados do Jira e GitHub
para apoiar processos de engenharia de software.[/yellow]
        
Digite 'exit' ou 'sair' para encerrar a aplicação.
        """,
        title="Bem-vindo!",
        border_style="blue"
    ))

def process_query(query: str, jira_connector: JiraConnector) -> str:
    """Processa a consulta do usuário utilizando o conector MCP do Jira.
    
    Args:
        query: Consulta em linguagem natural
        jira_connector: Instância do conector Jira
        
    Returns:
        Resposta processada para o usuário
    """
    # Futuramente, esta função irá processar a consulta usando o LlamaIndex
    # Por enquanto, implementaremos algumas respostas simuladas para demonstração
    if "issue" in query.lower() or "jira" in query.lower():
        try:
            # Tenta uma consulta básica no Jira
            return jira_connector.process_query(query)
        except Exception as e:
            return f"[bold red]Erro ao consultar o Jira:[/bold red] {str(e)}"
    
    return "[yellow]Ainda não consigo processar este tipo de consulta.[/yellow]"

def interactive_prompt():
    """Inicia o prompt interativo para consultas do usuário."""
    # Inicializa o conector Jira
    try:
        jira_connector = JiraConnector()
    except Exception as e:
        console.print(f"[bold red]Erro ao inicializar o conector Jira:[/bold red] {str(e)}")
        return
    
    # Loop principal da CLI
    while True:
        # Solicita consulta ao usuário
        query = Prompt.ask("\n[bold blue]Como posso ajudar?[/bold blue]")
        
        # Verifica se o usuário deseja sair
        if query.lower() in ["exit", "sair", "quit"]:
            console.print("[green]Encerrando aplicação. Até logo![/green]")
            break
        
        # Processa a consulta
        response = process_query(query, jira_connector)
        
        # Exibe a resposta
        console.print(Panel(response, title="Resposta", border_style="green"))

def run_cli():
    """Função principal que inicia a CLI."""
    # Verifica se o ambiente está configurado corretamente
    if not check_environment():
        return
    
    # Exibe mensagem de boas-vindas
    display_welcome()
    
    # Inicia o prompt interativo
    try:
        interactive_prompt()
    except KeyboardInterrupt:
        console.print("\n[yellow]Operação interrompida pelo usuário.[/yellow]")
    except Exception as e:
        console.print(f"\n[bold red]Erro inesperado:[/bold red] {str(e)}")
    finally:
        console.print("[green]Encerrando aplicação. Até logo![/green]")
