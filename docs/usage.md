# Guia de Uso - GenAI App Jira GitHub

## Configuração Inicial

Antes de usar a aplicação, você precisa configurar as credenciais de acesso ao Jira e GitHub. Siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/tiagonpsilva/genai-app-mcp-jira-github.git
   cd genai-app-mcp-jira-github
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`
   - Edite o arquivo `.env` com suas credenciais do Jira e GitHub

## Iniciando a Aplicação

Para iniciar a aplicação, execute o seguinte comando na raiz do projeto:

```bash
python main.py
```

Isso iniciará a interface de linha de comando interativa.

## Tipos de Consultas Suportadas

Atualmente, a aplicação suporta os seguintes tipos de consultas:

### Consultas ao Jira

1. **Listar issues do projeto**
   ```
   Listar issues do projeto
   ```
   ou
   ```
   Mostrar issues do projeto
   ```

2. **Detalhes de uma issue específica**
   ```
   Mostrar detalhes da issue PROJ-123
   ```
   ou
   ```
   Detalhes da tarefa PROJ-123
   ```

## Exemplos de Uso

```
Como posso ajudar? Listar issues do projeto

┌─ Resposta ────────────────────────────────────────────────────────────────┐
│ Issues recentes no projeto:                                               │
│                                                                           │
│ PROJ-123: Implementar autenticação de usuários                           │
│ Status: Em Andamento | Responsável: João Silva                           │
│                                                                           │
│ PROJ-124: Corrigir bug na página de checkout                             │
│ Status: Aberto | Responsável: Maria Oliveira                             │
│                                                                           │
│ PROJ-125: Atualizar documentação da API                                  │
│ Status: Concluído | Responsável: Carlos Santos                            │
└───────────────────────────────────────────────────────────────────────────┘

Como posso ajudar? Mostrar detalhes da issue PROJ-123

┌─ Resposta ────────────────────────────────────────────────────────────────┐
│ PROJ-123: Implementar autenticação de usuários                           │
│                                                                           │
│ Status: Em Andamento                                                     │
│ Responsável: João Silva                                                  │
│ Criado em: 2025-04-01T10:30:45.000+0000                                  │
│ Atualizado em: 2025-04-10T15:22:18.000+0000                              │
│                                                                           │
│ Descrição:                                                               │
│ Implementar sistema de autenticação de usuários utilizando OAuth 2.0     │
│ com suporte a login via Google e GitHub.                                 │
└───────────────────────────────────────────────────────────────────────────┘
```

## Comandos da CLI

- Para sair da aplicação, digite `exit`, `sair` ou `quit`
- Use Ctrl+C para interromper a execução

## Próximos Passos

Próximas funcionalidades planejadas:

- Integração com GitHub para consultas entre Jira e GitHub
- Implementação completa do LlamaIndex para processamento avançado de consultas
- Criação de relatórios e métricas de desenvolvimento
- Interface web para visualização de dados