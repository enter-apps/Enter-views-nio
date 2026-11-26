# Subsídios Nio

App para operadores da Nio montarem subsídios: questionário guiado por subobjeto (começando por Interrupção), upload de telas com checagem de qualidade da imagem, nota 0–10 orientativa e exportação em PDF, PPTX e DOCX.

## Estrutura
- `src/src.html`: código-fonte (HTML único, JS puro) com os marcadores `__DATA__` e `__ASSETS__`.
- `src/data.json`, `src/assets.json`: dados de causas e imagens (logo e ondas) embutidos no build.
- `dist/app.html`: app pronto, publicado como artefato.
- `build.py`: `python3 build.py` regenera `dist/app.html`.
- `docs/requisitos-subsidios-nio.md`: requisitos e decisões.
- `data/`: de-para do checklist de Interrupção e lista de causas reais (MECE).

## Identidade visual (v16)
Fundo areia, verdes da Nio como protagonistas, cores secundárias só como ponto pequeno, gradientes suaves, cartão da nota em verde-claro, menu lateral com linha do tempo e ondas, PDF em destaque no download. Fonte Plus Jakarta Sans (fallback da BW Gradual).

## Pendências
Logo em SVG, ícones oficiais e fonte BW Gradual; OCR não roda no visualizador do artefato (confirmação humana de legibilidade); validar nomes de tela inferidos e causa real de alguns casos de Interrupção.
