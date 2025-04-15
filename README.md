# GenAI App - Integração Jira e GitHub

Aplicação de IA Generativa que conecta dados do Jira e GitHub para apoiar processos de engenharia de software.

## 📋 Objetivo

Este projeto tem como objetivo criar um contexto de dados unificado entre Jira e GitHub para apoiar times de desenvolvimento em processos de engenharia de software. Através de uma interface de linha de comando (CLI) com prompt interativo, os usuários podem realizar consultas e obter insights com base nos dados integrados dessas duas plataformas.

## 🏗️ Arquitetura

A arquitetura do sistema é composta por três componentes principais:

```
┌─────────────┐      ┌──────────────────────────────┐      ┌─────────────────┐
│             │      │                              │      │                 │
│    CLI      │◄────►│  MCP Server 1 (LlamaIndex)   │◄────►│    Jira API     │
│  (Python)   │      │  (Jira Connector)            │      │                 │
│             │      │                              │      │                 │
└─────────────┘      └──────────────────────────────┘      └─────────────────┘
       ▲                                                
       │                                                
       ▼                                                
       │             ┌──────────────────────────────┐      ┌─────────────────┐
       │             │                              │      │                 │
       └────────────►│  MCP Server 2 (LlamaIndex)   │◄────►│   GitHub API    │
                     │  (GitHub Connector)          │      │                 │
                     │                              │      │                 │
                     └──────────────────────────────┘      └─────────────────┘
```

### Componentes:

* **CLI**: Interface de linha de comando que oferece um prompt interativo para os usuários realizarem consultas.
* **MCP Server 1 (LlamaIndex)**: Conector de dados do Jira, implementado com LlamaIndex, responsável por extrair e processar informações da API do Jira.
* **MCP Server 2 (LlamaIndex)**: Conector de dados do GitHub, implementado com LlamaIndex, responsável por extrair e processar informações da API do GitHub.

## 🚀 Implementação

### Tecnologias Utilizadas

* **Python**: Linguagem principal de desenvolvimento.
* **LlamaIndex**: Framework para implementação dos conectores MCP, indexação e consulta de dados em aplicações GenAI.
* **MCP Server GitHub**: Implementação oficial do GitHub para o protocolo MCP ([github/github-mcp-server](https://github.com/github/github-mcp-server)).
* **MCP Server Jira**: Implementação do protocolo MCP para Jira ([sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian)).

### Pré-requisitos

* Python 3.10+
* Acesso às APIs do Jira e GitHub
* Credenciais de autenticação para ambas as plataformas

## 🛠️ Instalação e Configuração

```bash
# Clonar o repositório
git clone https://github.com/tiagonpsilva/genai-app-mcp-jira-github.git
cd genai-app-mcp-jira-github

# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas credenciais
```

## 📊 Funcionalidades Principais

- Consulta integrada de issues do Jira e PRs do GitHub
- Rastreamento de ciclo de vida de features entre as plataformas
- Estatísticas e métricas de desenvolvimento
- Identificação de gargalos no processo de desenvolvimento
- Recomendações baseadas em padrões históricos

## 🧩 Como Usar

```bash
# Iniciar a aplicação
python main.py

# Exemplos de consultas:
# - "Quais PRs estão associados à issue PROJ-123?"
# - "Mostrar métricas de tempo de desenvolvimento por tipo de issue"
# - "Listar issues bloqueadas há mais de 3 dias"
```

## 📝 Roadmap

- [ ] MVP com consultas básicas entre Jira e GitHub
- [ ] Implementação de cache para otimizar consultas
- [ ] Dashboard visual para métricas
- [ ] Integração com outros sistemas ALM
- [ ] Análise preditiva para estimativas de tempo

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre o processo de submissão de pull requests.

## 📜 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.