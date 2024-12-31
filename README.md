# Preparando seu ambiente

Ambiente rodando de forma segura e encapsulada.

## Instalação:

### Rodando tudo dentro de contêiner

Isso para quando não quer ou não pode ter o python instalado na sua máquina.

Instalações necessárias:
- https://www.docker.com
- https://code.visualstudio.com

Extensões necessárias no seu [VSCode](https://vscode.dev/):
- https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker
- https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

```bash
docker pull python:3.13.1-slim
docker rm study-python
docker run --name study-python -it python:3.13.1-slim bash
```

Isso vai abrir no seu terminal uma central com o contêiner criado, já com python pronto para uso.

o `Dev Containers` vai te permitir abrir a pasta de dentro do seu contêiner, a partir do VSCode, e com isso, pode programar diretamente de dentro do seu contêiner!


### Rodando na sua máquina

Se você quer mais comodidade, então instale o python no seu Sistema Operacional.

Instalações necessárias:
- https://code.visualstudio.com
- https://www.python.org

Extensões necessárias no seu [VSCode](https://vscode.dev/):
- https://marketplace.visualstudio.com/items?itemName=ms-python.python


## Criação do ambiente virtual

https://docs.python.org/3/library/venv.html

> Obs.: Comandos considerando a raiz do projeto

> Não se esquece de adicionar `**/.venv/*` no seu `.gitignore`

```bash
python -m pip install --upgrade pip
python -m venv .\.venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
```

> Ativação Linux
```bash
source .venv\bin\activate
```

> A partir de agora, está com ambiente virtual criado e ativo!


> Instalação das dependências necessárias até o momento:
```
pip install -r ./requeriments.txt

pip install boto3
pip install qrcode img2pdf
pip install streamlit streamlit_modal streamlit_option_menu streamlit_navigation_bar
pip install lxml pyQt5
pip install opencv-python numpy matplotlib  
```

# Tutoriais:

## Use Python no contêiner:

Aqui é uma forma para quando não pode ou não quer instalar o python no seu host.

```bash
docker pull python:3.13.1-alpine
docker run --name study-python:3.13.1 -it python:3.13.1-alpine bash

docker pull python:3.13.1-slim
docker rm study-python
docker run --name study-python -it python:3.13.1-slim bash

docker build -t study-python:get_youtube -f ./Dockerfile .
docker run -p 8501:8501 --name get_youtube study-python:get_youtube
```




## Streamlit:

* https://fonts.google.com/icons
* https://docs.streamlit.io/develop/api-reference/caching-and-state
* https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation
* https://docs.streamlit.io/develop/api-reference/data/st.column_config
* 
* https://discuss.streamlit.io/t/new-component-streamlit-navigation-bar/66032


## Tutorial How to Install LabelImg on WINDOWS 10
* https://www.youtube.com/watch?v=3d_EffmnAQc

```
pip install lxml pyQt5
cd .\.venv
git clone git@github.com:HumanSignal/labelImg.git
cd .\labelImg\
pyrcc5 -o libs/resources.py resources.qrc
python .\labelImg.py
```

### Sample

* [imagem](labelImg_sample/1050x1485_20241120134236446284_1a90.png)
* [CreateML](labelImg_sample/1050x1485_20241120134236446284_1a90.json)
* [PascalVOC](labelImg_sample/1050x1485_20241120134236446284_1a90.xml)
* [YOLO](labelImg_sample/1050x1485_20241120134236446284_1a90.txt)

<br><br>

## Tutorial: Como usar esses arquivos?


# References

* https://medium.com/thedeephub/adjusting-image-orientation-with-perspective-transformations-using-opencv-e32d16e017fd
* https://www.galirows.com.br/meublog/opencv-python/opencv2-python27/capitulo1-basico/desenhar-formas-geometricas/
* https://learnopencv.com/cropping-an-image-using-opencv/

* https://holypython.com/python-pil-tutorial/how-to-create-a-new-image-with-pil/
* https://www.geeksforgeeks.org/image-resizing-using-opencv-python/
* 

## LIBS:

* https://pypi.org/project/img2pdf/


## AWS Lambda
- https://www.youtube.com/watch?v=fEZE3rm8Ma8
- https://www.youtube.com/watch?v=S0rlj67cTHw
- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lambda.html

- https://docs.localstack.cloud/user-guide/aws/lambda/
