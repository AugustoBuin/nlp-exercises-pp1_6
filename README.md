# 📂 Paraphrase Generator - Comparando spaCy e Transformers

## 🔍 Visão Geral
Este repositório apresenta dois métodos para **parafrasear** frases em inglês utilizando **Processamento de Linguagem Natural (PLN)**:

1. **Usando spaCy + WordNet**: Substitui palavras por sinônimos extraídos do WordNet, com base na classificação gramatical (POS tagging).
2. **Usando Transformers (PEGASUS)**: Um modelo de deep learning treinado para parafraseamento, que gera frases reescritas de forma mais natural.

Ambos os métodos têm vantagens e limitações, que serão discutidas abaixo.

---

## ⚙️ Configuração e Instalação
Para rodar os scripts, instale as dependências, nas duas pastas, e depois rode cada uma delas, com os seguintes comandos:

```sh
cd pasta
pip install -r requirements.txt
python index.py
```

---

## 📚 Método 1: Usando spaCy + WordNet
**Código:** [`paraphrase_spacy.py`](paraphrase_spacy.py)

### ✅ Como funciona?
- Usa **spaCy** para dividir a frase e identificar classes gramaticais (POS tagging).
- Consulta **WordNet (NLTK)** para encontrar sinônimos das palavras relevantes.
- Substitui palavras por sinônimos e reconstrói a frase.

### ⚠ Problemas:
- **Pouca precisão**: Muitas palavras substituídas perdem o significado original.
- **Sinônimos inadequados**: Pode escolher nomes próprios ou termos fora de contexto.
- **Erro em substantivos**: Por exemplo, "fox" pode ser substituído por "Charles James Fox".

### 🌟 Exemplo de Saída:
#### **Entrada:**
```text
The quick brown fox jumps over the lazy dog.
```
#### **Saída:**
```text
The nimble brownish Charles James Fox jump out over the slothful pawl.
```
**💥 Problema:** Termos aleatórios sem sentido!

---

## 🧠 Método 2: Usando Transformers (PEGASUS)
**Código:** [`paraphrase_transformers.py`](paraphrase_transformers.py)

### ✅ Como funciona?
- Utiliza o modelo **PEGASUS**, treinado para sumarização e parafraseamento.
- Gera uma nova frase sem substituir palavras isoladamente.
- Usa redes neurais para capturar contexto e estrutura da frase.

### 💚 Vantagens:
- **Maior coerência**: A frase mantém o sentido original.
- **Evita sinônimos errados**: O modelo reformula a frase em vez de apenas trocar palavras.

### ⚠ Limitações:
- **Nem sempre parafraseia de forma expressiva**: Pode gerar uma frase muito parecida com a original.
- **Requer mais recursos computacionais**: Pode ser mais lento e consumir mais memória.

### 🌟 Exemplo de Saída:
#### **Entrada:**
```text
The quick brown fox jumps over the lazy dog.
```
#### **Saída:**
```text
A fast brown fox leaps over a sluggish dog.
```
**👌 Muito melhor!**

---

## 📊 Comparando os Métodos
| Critério              | spaCy + WordNet     | Transformers (PEGASUS)      |
| --------------------- | ------------------- | --------------------------- |
| **Precisão**          | ❌ Baixa             | ✅ Alta                      |
| **Contexto**          | ❌ Ignora            | ✅ Considera                 |
| **Qualidade**         | ❌ Sinônimos errados | ✅ Frases naturais           |
| **Velocidade**        | ✅ Rápido            | ❌ Pode ser mais lento       |
| **Facilidade de uso** | ✅ Simples           | ❌ Requer mais processamento |

---

## 🔍 Conclusão

- O **spaCy + WordNet** é **mais rápido**, mas tem baixa precisão e gera frases com erros grotescos.
- O **PEGASUS (Transformers)** é **mais preciso**, considerando o contexto, mas pode ser mais lento.
- Para parafraseamento **realista e natural**, o método baseado em **Transformers** é a melhor opção!

---

Digite uma frase e veja o resultado!

📄 Criado por [AugustoBuin](https://github.com/AugustoBuin) | 2025

