# Portfólio | Ludwig Silva

Este projeto é um site de portfólio desenvolvido com Django, criado para apresentar minha trajetória como artista, educador e músico. Ele conta com seções para divulgação de aulas presenciais e online, eventos e informações de contato.

## 🌐 Demonstração

O site está disponível em: [https://portifolio-lud.onrender.com](https://portifolio-vyct.onrender.com)  
*(Domínio personalizado em breve!)*

---

## 📁 Estrutura do Projeto

```bash
portifolio/
├── meu_site/            # Projeto Django
│   ├── meu_site/        # Configurações (settings.py, urls.py, wsgi.py)
│   ├── core/            # App principal com as views, urls e templates
│   ├── static/          # Arquivos estáticos (CSS, imagens, JS)
│   ├── templates/       # Templates HTML
│   ├── media/           # Uploads (utilizado inicialmente, agora substituído por static/)
│   ├── manage.py        # Gerenciador do projeto Django
├── requirements.txt     # Dependências do projeto
├── render.yaml          # Configuração de deploy no Render
├── README.md            # Documentação do projeto
```

---

## ⚙️ Funcionalidades

- ✅ Página inicial com imagem de destaque e introdução
- ✅ Aulas presenciais e online com agendamento
- ✅ Página de eventos (workshops, apresentações, etc.)
- ✅ Página de contato
- ✅ Layout responsivo com Bootstrap
- ✅ Servindo arquivos estáticos corretamente em produção (via `collectstatic`)
- ✅ Hospedagem no Render

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11+**
- **Django 5**
- **Bootstrap 5**
- **HTML5, CSS3, JS**
- **Render.com** (deploy e hospedagem)
- **Git + GitHub**

---

## 🛠️ Configuração Local

### 1. Clone o projeto
```bash
git clone https://github.com/silvaludwig/portifolio.git
cd portifolio
```

### 2. Crie o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações
```bash
python manage.py migrate
```

### 5. Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```

Acesse o site em: [http://localhost:8000](http://localhost:8000)

---

## 🧾 Deploy no Render

### Estrutura básica usada no `render.yaml`:
```yaml
services:
  - type: web
    name: portifolio
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn meu_site.wsgi:application"
    staticPublishPath: staticfiles
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: meu_site.settings
      - key: PYTHON_VERSION
        value: 3.11
```

### Coleta dos arquivos estáticos para produção:
```bash
python manage.py collectstatic
```

---

## 🌍 Como configurar um domínio personalizado

1. Compre um domínio em um provedor (como Registro.br, GoDaddy, Namecheap, etc.)
2. Acesse o painel do Render: `https://dashboard.render.com`
3. Vá em *Settings* do seu serviço
4. Adicione o domínio personalizado em **Custom Domains**
5. Aponte os registros DNS do seu domínio para o Render (eles fornecem instruções específicas com os registros A e CNAME)
6. Aguarde a propagação (pode levar algumas horas)

---

## ✨ Autor

Feito com dedicação por **[Ludwig Silva](https://github.com/silvaludwig)**  
📧 ludwigsilva.contato@gmail.com  
🎸 Artista, educador e programador iniciante com paixão por música e tecnologia.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
