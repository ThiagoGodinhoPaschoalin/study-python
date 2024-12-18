# HELLO WORLD

Ambiente rodando de forma segura e encapsulada.

## Ter o python globalmente

Observação: A versão do python 3.13.0 está com um bug no `venv`, como descrito nessa discussão:<br>
https://discuss.python.org/t/3-13-0-tkinter-versus-venv-in-windows-10/67151<br>
E por esse movito sugiro a instalação da versão 3.12.7!
* [download python 3.12.7](https://www.python.org/downloads/release/python-3127/)

## Criação do ambiente virtual

https://docs.python.org/3/library/venv.html

> Obs.: Comandos considerando a raiz do projeto

> Não se esquece de adicionar `**/.venv/*` no seu `.gitignore`

```
python.exe -m pip install --upgrade pip

python -m venv .\.venv

.\.venv\Scripts\activate

python -m pip install --upgrade pip

pip install boto3
pip install qrcode img2pdf
pip install streamlit streamlit_modal streamlit_option_menu streamlit_navigation_bar
pip install lxml pyQt5
pip install opencv-python numpy matplotlib  
```

# Tutoriais:

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
