"""Configurações e verificações de ambiente para a CLI."""

import os
from rich.console import Console

console = Console()

def check_environment() -> bool:
    """Verifica se todas as variáveis de ambiente necessárias estão configuradas.
    
    Returns:
        bool: True se todas as variáveis necessárias estão presentes, False caso contrário
    """
    required_vars = {
        'JIRA_URL': 'URL da instância do Jira (ex: https://seu-dominio.atlassian.net)',
        'JIRA_USERNAME': 'Seu email de login no Jira',
        'JIRA_API_TOKEN': 'Token de API do Jira',
        'JIRA_PROJECT': 'Código do projeto no Jira (ex: PROJ)'
    }
    
    missing_vars = []
    
    for var, description in required_vars.items():
        if not os.getenv(var):
            missing_vars.append(f"[bold]{var}[/bold]: {description}")
    
    if missing_vars:
        console.print("[bold red]Erro: Variáveis de ambiente não configuradas:[/bold red]")
        for var in missing_vars:
            console.print(f"  - {var}")
        console.print("\n[yellow]Por favor, crie um arquivo .env na raiz do projeto com as variáveis necessárias.[/yellow]")
        console.print("[yellow]Você pode usar o arquivo .env.example como referência.[/yellow]")
        return False
    
    return True
