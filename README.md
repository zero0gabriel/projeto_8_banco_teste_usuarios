# Sistema de Cadastro de Utilizadores (Flask)

Aplicação web desenvolvida em Python com Flask para gestão de utilizadores e autenticação[cite: 1].

## 📋 Sobre a Aplicação
O projeto faz a ligação entre rotas web e uma base de dados através de um módulo auxiliar (`banco.py`)[cite: 1]. Conta com:
* **Página de Login (`/`)**: Rota inicial que carrega a interface de acesso[cite: 1].
* **Página de Registo (`/cadastrar`)**: Recolhe nome, email e senha do formulário, aplicando criptografia de hash (`generate_password_hash`) para segurança das credenciais antes de armazenar[cite: 1].
