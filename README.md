# GenAI App - Integração Jira e GitHub via MCP

Aplicação de IA Generativa que conecta dados do Jira e GitHub para apoiar processos de engenharia de software.

## 💻 Objetivo

Este projeto tem como objetivo criar um contexto de dados unificado entre Jira e GitHub para apoiar times de desenvolvimento em processos de engenharia de software. Através de uma interface de linha de comando (CLI) com prompt interativo, os usuários podem realizar consultas e obter insights com base nos dados integrados dessas duas plataformas.

## 👷‍♂️ Arquitetura

A arquitetura do sistema é composta por três componentes principais:

```
┌─────────────┐      ┌───────────────────────────────┐      ┌─────────────────┐
│           │      │                              │      │                 │
│    CLI    │━━━━━━━┼───────────────────────────────┾━━━━━━━│    Jira API    │
│  (Python)  │      │  MCP Server 1 (LlamaIndex)  │      │                 │
│           │      │     (Jira Connector)         │      │                 │
└─────────────┘      └───────────────────────────────┘      └─────────────────┘
        │                                                      │
        │                                                      │
        │                                                      │
        │      ┌───────────────────────────────┐      ┌─────────────────┐
        │      │                              │      │                 │
        └━━━━━━━┼───────────────────────────────┾━━━━━━━│   GitHub API   │
                │  MCP Server 2 (LlamaIndex)  │      │                 │
                │   (GitHub Connector)        │      │                 │
                └───────────────────────────────┘      └─────────────────┘
```

### Componentes:

* **CLI**: Interface de linha de comando que oferece um prompt interativo para os usuários realizarem consultas.
* **MCP Server 1 (LlamaIndex)**: Conector de dados do Jira, implementado com LlamaIndex, responsável por extrair e processar informações da API do Jira.
* **MCP Server 2 (LlamaIndex)**: Conector de dados do GitHub, implementado com LlamaIndex, responsável por extrair e processar informações da API do GitHub.

## 🚠 Implementação

### Tecnologias Utilizadas

* **Python**: Linguagem principal de desenvolvimento.
* **LlamaIndex**: Framework para implementação dos conectores MCP, indexação e consulta de dados em aplicações GenAI.
* **MCP Server GitHub**: Implementação oficial do GitHub para o protocolo MCP ([github/github-mcp-server](https://github.com/github/github-mcp-server)).
* **MCP Server Jira**: Implementação do protocolo MCP para Jira ([sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian)).

### Estado Atual da Implementação (Branch feature/cli-mcp-server-1)

Esta branch implementa os seguintes componentes:

1. **CLI**: Interface de linha de comando completa com prompt interativo
2. **MCP Server 1 (Jira Connector)**: Conector básico para a API do Jira

O MCP Server 2 (GitHub Connector) será implementado em uma branch futura.

### Estrutura de Diretórios

```
genai-app-mcp-jira-github/
├── cli/                  # Módulo da interface de linha de comando
│   ├── __init__.py
│   ├── app.py           # Implementação principal da CLI
│   └── config.py        # Configurações da CLI
├── docs/                 # Documentação
│   └── usage.md         # Guia de uso da aplicação
├── mcp/                  # Implementações dos conectores MCP
│   ├── __init__.py
│   ├── jira/             # Conector MCP para Jira
│   │   ├── __init__.py
│   │   └── connector.py  # Implementação do conector Jira
│   └── utils/            # Utilitários compartilhados
│       ├── __init__.py
│       └── logger.py      # Configuração de logs
├── tests/                # Testes automatizados
│   ├── __init__.py
│   ├── test_cli.py      # Testes da CLI
│   └── test_jira_connector.py  # Testes do conector Jira
├── .env.example         # Modelo para configurações de ambiente
├── .gitignore           # Arquivos ignorados pelo Git
├── CONTRIBUTING.md       # Guia de contribuição
├── LICENSE              # Licença MIT
├── README.md            # Documentação principal
├── main.py              # Ponto de entrada da aplicação
└── requirements.txt      # Dependências do projeto
```

### Pré-requisitos

* Python 3.10+
* Acesso às APIs do Jira e GitHub
* Credenciais de autenticação para ambas as plataformas

## 💚 Instalação e Configuração

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

## 🖊️ Funcionalidades Atuais

**MVP Base (Branch feature/cli-mcp-server-1):**

- [x] Interface CLI com prompt interativo
- [x] Conector básico para a API do Jira
- [x] Consultas simples de issues do Jira
  - [x] Listar issues do projeto
  - [x] Mostrar detalhes de uma issue específica

## 🚩 Como Usar

```bash
# Iniciar a aplicação
python main.py

# Exemplos de consultas:
# - "Listar issues do projeto"
# - "Mostrar detalhes da issue PROJ-123"
```

Para mais detalhes sobre o uso da aplicação, consulte o [Guia de Uso](docs/usage.md).

## 📝 Roadmap

- [x] MVP com consultas básicas ao Jira
- [ ] Implementação completa do LlamaIndex para o conector Jira
- [ ] Implementação do conector GitHub
- [ ] Integração entre dados do Jira e GitHub
- [ ] Implementação de cache para otimizar consultas
- [ ] Dashboard visual para métricas
- [ ] Integração com outros sistemas ALM
- [ ] Análise preditiva para estimativas de tempo

## 🆕 Contribuição

Contribuições são bem-vindas! Por favor, leia o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre o processo de submissão de pull requests.

## 📜 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
