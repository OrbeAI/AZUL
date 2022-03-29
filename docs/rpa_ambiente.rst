Preparando o ambiente
****

01.Instalar o Jupyter
====

Como a biblioteca de RPA que iremos utilizar (Pyautogui) acessa alguns comandos físicos do computador, como mouse, teclado, tela, etc, não é possível utilizar o Google Colaboratory, pois ele roda em um servidor.

Para isso veremos como instalar o Jupyter Notebook para que os códigos rodem em nossa máquina, só seguir o passo a passo:

1.Acesse o site https://www.anaconda.com/

2.Posicione o mouse em *Products* e depois clique em *Individual Edition*.

.. image:: images/RPA/anaconda_1.png
   :align: center
   :width: 450

3.Clique em *Download*

.. image:: images/RPA/anaconda_2.png
   :align: center
   :width: 450

4.Aguarde a instalação, depois clique em *Next* até finalizar, na última etapa basta desmarcar as opções e clicar em *Finish*

.. image:: images/RPA/anaconda_3.png
   :align: center
   :width: 550


02.Acessar o Jupyter
=====

02.a.Verificando a instalação
-----

Agora que o Anaconda já está instalada, podemos acessar o Jupyter Notebook, para isso basta:

1.Verificar se o prompt de comando anaconda está instalado.

.. image:: images/RPA/anaconda_4.png
   :align: center
   :width: 450

2.Verificar se o Jupyter Notebook está instalado.

.. image:: images/RPA/anaconda_5.png
   :align: center
   :width: 450

3.Clicar no programa Jupyter Notebook.


02.b.Instalando a pyautogui
----

Para instalar a biblioteca que iremos utilizar para criar nossos RPA:

1.Abra o Anaconda Prompt

.. image:: images/RPA/anaconda_prompt.png
   :align: center
   :width: 450

2.Com o prompt aberto digite **pip install pyautogui** e clique enter

.. image:: images/RPA/pyautogui.png
   :align: center
   :width: 550

Ele irá instalar uma série de dependências e depois irá aparecer *Successfully installed pyauogui-* e o numero da versão instalada.


02.c.Programa Jupyter Notebook
----

Ao clicar no programa Jupyter Notebook irá abrir duas telas, uma tela preta e outra do navegador com o Jupyter Notebook, se fechar alguma delas, fecha as duas.

.. image:: images/RPA/anaconda_6.png
   :align: center
   :width: 350

02.c.I.Criando um repositório
++++

O Jupyter Notebook acessa o sistema de arquivos do seu computador, portanto ao abrir o Jupyter, é recomendado criar uma pasta para salvar seus projetos. 

Para isso, clique na pasta *Downloads* depois clique em *New* e então clique em *Folder*

.. image:: images/RPA/new_folder.png
   :align: center
   :width: 450

02.c.II.Renomeando o repositório
++++

Depois uma nova pasta chamada *Untitled Folder* irá surgir dentro da pasta *Downloads*, para renomea-la basta selecionas essa pasta e clicar em *Rename*

.. image:: images/RPA/rename.png
   :align: center
   :width: 550

Então só selecionar o nome desejado e clicar em *Rename*

.. image:: images/RPA/rename_2.png
   :align: center
   :width: 550

02.c.III.Acessando o Jupyter
++++

Agora que já temos um repositório nomeado corretamente podemos criar um Jupyter Notebook para começar a trabalhar, para isso, dentro da pasta criada clique em *New* e então em *Python 3*

.. image:: images/RPA/new_jupyter.png
   :align: center
   :width: 550

Apesar da interface ser um pouco diferente do Google Colaboratory, seu funcionamento é praticamente igual. 

.. image:: images/RPA/jupyter.png
   :align: center
   :width: 450

Neste bloco podemos escrever códigos em linguagem Python e ao clicar *Run* iremos rodar o código da célula selecionada.

.. image:: images/RPA/run_python.png
   :align: center
   :width: 450
