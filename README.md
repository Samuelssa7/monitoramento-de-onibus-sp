# 🚌 Monitoramento de Ônibus SP

Script em Python que consulta a API pública **Olho Vivo**, da SPTrans, para localizar em tempo real um ônibus de uma linha específica e as paradas do seu trajeto, exibindo tudo em um mapa interativo.

## Funcionalidades

- Autenticação na API Olho Vivo usando token pessoal
- Consulta da posição atual (latitude/longitude) de um ônibus de uma linha
- Consulta das paradas cadastradas para essa linha
- Geração de um mapa interativo (via [Folium](https://python-visualization.github.io/folium/)) com marcadores para o ônibus e cada parada

## Tecnologias

- Python
- [Requests](https://docs.python-requests.org/) para consumo da API REST
- [Folium](https://python-visualization.github.io/folium/) para geração do mapa interativo
- [python-dotenv](https://pypi.org/project/python-dotenv/) para gerenciar o token de acesso
- API Olho Vivo (SPTrans)

## Como rodar

Pré-requisitos: Python 3.8+ e um token de acesso à API Olho Vivo (gratuito, solicitado em [olhovivo.sptrans.com.br](http://www.sptrans.com.br/desenvolvedores/api-do-olho-vivo/como-acessar/)).

```bash
git clone https://github.com/Samuelssa7/monitoramento-de-onibus-sp.git
cd monitoramento-de-onibus-sp
pip install requests folium python-dotenv
```

Crie um arquivo `.env` na raiz do projeto com o seu token:

```
SPTRANS_TOKEN=seu_token_aqui
```

Depois, execute:

```bash
python main.py
```

Isso abre no navegador um mapa com a posição do ônibus e as paradas da linha configurada (por padrão, o código da linha `2304` — pode ser alterado diretamente em `main.py`).

## Estrutura do projeto

O projeto está em evolução: a lógica principal está hoje em `main.py`, e a ideia é reorganizá-la nos módulos já esboçados na estrutura de pastas:

```
main.py                     # Script principal (autenticação, consultas e geração do mapa)
services/
└── sptrans_service.py      # Em construção: isolar as chamadas à API Olho Vivo
models/
├── onibus.py                # Em construção: representação do ônibus como objeto
└── parada.py                 # Em construção: representação da parada como objeto
maps/
└── mapa_service.py           # Em construção: isolar a geração do mapa com Folium
```

## Aprendizados

Este projeto foi minha primeira experiência integrando uma API REST externa com autenticação, tratando o retorno em JSON e usando essas informações para gerar uma visualização geográfica em tempo real.

## Próximos passos

- Migrar a lógica de `main.py` para os módulos em `services/`, `models/` e `maps/`
- Aplicar POO na representação de ônibus e paradas
- Permitir escolher a linha de ônibus via input, em vez de valor fixo no código
- Tratar erros de autenticação e de linha inexistente
