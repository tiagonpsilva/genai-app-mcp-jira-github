# Contribuindo para o GenAI App - Integração Jira e GitHub

Primeiramente, obrigado por considerar contribuir para este projeto! Pessoas como você ajudam a tornar este projeto melhor para todos.

## Como contribuir

### Reportando bugs

1. **Verifique se o bug já foi reportado** - Busque nas issues do projeto para verificar se o problema já foi reportado.
2. **Verifique se o bug foi corrigido** - Tente reproduzir o problema usando a última versão da branch `main`.
3. **Isole o problema** - Crie um caso de teste reduzido e um exemplo vivo que reproduza o problema.
4. **Abra uma nova issue** - Se o problema ainda não foi reportado, abra uma nova issue detalhando:
   - Título claro e descritivo
   - Passos para reproduzir o problema
   - Comportamento esperado vs comportamento atual
   - Versões relevantes de pacotes/ambiente

### Sugerindo melhorias

1. **Verifique se a sugestão já existe** - Busque nas issues existentes para ver se sua sugestão já foi proposta.
2. **Abra uma nova issue** - Descreva claramente:
   - O problema atual e por que sua sugestão o resolve
   - Como a sua sugestão beneficia a maioria dos usuários
   - Referências ou exemplos relevantes

### Contribuindo com código

1. **Fork o repositório** - Crie um fork do projeto para sua conta.
2. **Clone seu fork** - `git clone https://github.com/seu-usuario/genai-app-mcp-jira-github.git`
3. **Crie uma branch para sua feature** - `git checkout -b feature/minha-nova-feature`
4. **Instale as dependências de desenvolvimento** - `pip install -e ".[dev]"`
5. **Faça suas alterações**:
   - Siga o estilo de código existente
   - Escreva testes para suas alterações
   - Documente seu código
   - Mantenha um histórico de commits limpo e claro
6. **Execute os testes** - `pytest`
7. **Commit suas alterações** - Use mensagens de commit claras seguindo o padrão [Conventional Commits](https://www.conventionalcommits.org/)
8. **Push para sua branch** - `git push origin feature/minha-nova-feature`
9. **Abra um Pull Request** - Descreva claramente o problema e a solução

## Padrões de código

- Siga a [PEP 8](https://www.python.org/dev/peps/pep-0008/) para código Python
- Use docstrings no formato [NumPy/SciPy](https://numpydoc.readthedocs.io/en/latest/format.html)
- Escreva testes para novas funcionalidades
- Mantenha a cobertura de testes acima de 80%
- Execute `black` e `isort` para formatação de código antes de commits

## Processo de revisão

1. Ao menos um mantenedor do projeto deve aprovar qualquer pull request
2. Todos os testes automatizados devem passar
3. O código deve seguir as diretrizes de estilo

## Comunicação

- Use issues do GitHub para discussões relacionadas ao projeto
- Para discussões mais amplas, use as discussões do GitHub

Obrigado por contribuir!