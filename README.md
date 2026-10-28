# Treinamento para Machine Learning 🧠

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white&style=for-the-badge)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white&style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white&style=for-the-badge)

Repositório com meus primeiros estudos de **Machine Learning** e **redes neurais** em Python.

---

## 🔢 Rede neural para reconhecer dígitos — [`Rede-neural-do-zero.ipynb`](Rede-neural-do-zero.ipynb)

Rede neural treinada com **PyTorch** para reconhecer dígitos escritos à mão do dataset **MNIST** (imagens 28×28 em tons de cinza).

**Arquitetura**

| Camada | Neurônios | Ativação |
|---|---|---|
| Entrada | 784 (28×28 pixels) → 128 | ReLU |
| Oculta | 128 → 64 | ReLU |
| Saída | 64 → 10 (dígitos 0 a 9) | Log-Softmax |

**Treino:** otimizador SGD (taxa de aprendizado 0,01, momentum 0,5), função de perda NLL e 10 épocas. Roda em GPU (CUDA) quando disponível.

**Resultado:** **95,69% de acerto** em 10.000 imagens de teste, com cerca de 1 minuto de treino.

## 📈 Primeiro modelo — [`primeiro_ML.ipynb`](primeiro_ML.ipynb)

Geração de dados sintéticos para regressão com `make_regression` do **scikit-learn** e visualização com **Matplotlib**.

## 🐍 Fundamentos de Python — [`treinamento_python.py`](treinamento_python.py)

Exercícios de estruturas de controle (`if`, `for`, `while`) usados como revisão antes dos notebooks.

## 🚀 Como rodar

```bash
pip install torch torchvision numpy matplotlib scikit-learn jupyter
jupyter notebook
```

O dataset MNIST é baixado automaticamente pelo `torchvision` na primeira execução.
