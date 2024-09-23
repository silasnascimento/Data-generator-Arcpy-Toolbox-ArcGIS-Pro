# Data Generator Tool for ArcGIS Pro

Este script é parte de uma ferramenta `.atbx` desenvolvida para ArcGIS Pro, destinada a gerar camadas de dados a partir de um polígono delimitador fornecido pelo usuário. Ele automatiza a criação de várias camadas vetoriais, incluindo subdivisões de polígonos em partes menores, conversões para pontos e linhas, e outras operações relacionadas.

## Funcionalidades

- **Divisão de Polígonos:** Divide o polígono de entrada em várias partes iguais, criando múltiplas camadas de tarefas, parcelas e geometrias.
- **Criação de Camadas Vetoriais:** Gera camadas de ponto, linha e polígono a partir das subdivisões.
- **Manipulação de Campos:** Adiciona e calcula campos nas camadas geradas para atribuição de nomes e outras informações relevantes.
- **Apêndice de Dados:** Os resultados são adicionados a camadas existentes no geodatabase especificado.

## Parâmetros de Entrada

1. **Enclosing Polygon (Polígono Delimitador):** Polígono de entrada que será subdividido para criar as camadas.
2. **Number of Assignments (Número de Atribuições):** Define o número de subdivisões para a camada de atribuições.
3. **Assignment Name (Nome da Atribuição):** Nome atribuído aos registros gerados.
4. **Min Tasks (Tarefas Mínimas):** Número mínimo de subdivisões para a camada de tarefas.
5. **Max Tasks (Tarefas Máximas):** Número máximo de subdivisões para a camada de tarefas.
6. **Min Geometries (Geometrias Mínimas):** Número mínimo de subdivisões para a camada de geometrias.
7. **Max Geometries (Geometrias Máximas):** Número máximo de subdivisões para a camada de geometrias.
8. **Min Parcels (Parcelas Mínimas):** Número mínimo de subdivisões para a camada de parcelas.
9. **Max Parcels (Parcelas Máximas):** Número máximo de subdivisões para a camada de parcelas.

## Como Funciona

1. **Divisão e Criação de Camadas:** O script subdivide o polígono de entrada com base nos parâmetros fornecidos, gerando as camadas necessárias.
2. **Manipulação de Dados:** Novos campos são adicionados e preenchidos conforme a lógica do script, como atribuições de nomes.
3. **Armazenamento em Geodatabase:** As camadas geradas são salvas dentro do Feature Dataset `Process_DataGen` no geodatabase especificado.
4. **Apêndice de Resultados:** Os dados gerados são adicionados às camadas existentes no geodatabase.

## Requisitos

- ArcGIS Pro com a extensão de Spatial Analyst.
- Geodatabase configurado conforme o caminho especificado no script.
- Permissões de leitura e escrita no local do geodatabase.

## Mensagens e Logs

- O script exibe uma mensagem de conclusão ao término do processo para confirmar o sucesso da operação.

## Observações

- Certifique-se de ajustar o caminho do geodatabase (`geodatabase_path`) conforme necessário.
- Verifique as permissões no ArcGIS Pro para garantir que o script possa manipular as camadas corretamente.

---

Este README serve como guia de uso e referência para a correta execução do script embutido na ferramenta `.atbx` dentro do ArcGIS Pro.
