#!/usr/bin/env python3

"""Aplicação principal que inicia a CLI do GenAI App para integração Jira e GitHub."""

import os
from dotenv import load_dotenv
from cli.app import run_cli

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

if __name__ == "__main__":
    run_cli()
