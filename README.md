# Currículo em Docker
O objetivo deste projeto é criar um container que engloba todo o conteúdo essencial necessário para a execução de um aplicativo web que exibe uma página HTML do meu currículo como estudante. A minha aplicação está na pasta corinthians.

# Método de Desenvolvimento da Aplicação
O aplicativo web foi criado usando o Python em conjunto com o framework "Flask". Para a implementação do contêiner, a Docker Engine foi empregada, seguindo uma abordagem de organização de recursos e criação de imagem.
- Inicialmente, uma lista de requisitos necessários para executar o sistema foi compilada e listada no arquivo "requirements.txt".
- Subsequentemente, um "Dockerfile" foi criado para definir as instruções a serem seguidas durante a construção da imagem. O Dockerfile inclui a linguagem de programação utilizada, sua versão, o diretório de armazenamento dos arquivos, a instalação das dependências e o comando para executar o aplicativo web.

# Geração do Container

Para a criação da imagem é necesário rodar o seguinte commando com o Docker Engine ativado:
 
docker build.

