from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

# Carregar o tokenizer e o modelo PEGASUS pré-treinado
model_name = "google/pegasus-xsum"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)


def paraphrase(text):
    # Tokenizar o texto de entrada
    inputs = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    # Gerar o parafraseamento
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=60,
            num_beams=5,
            num_return_sequences=1,
            temperature=1.5,
        )
    # Decodificar o texto parafraseado
    paraphrased_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return paraphrased_text


if __name__ == "__main__":
    while True:
        # Solicitar ao usuário que insira uma frase
        user_input = input("\nDigite uma frase em inglês (ou 'exit' para sair): ")
        if user_input.lower() == "exit":
            print("Encerrando o programa. Até mais!")
            break
        # Exibir a frase parafraseada
        print(f"↪ Frase parafraseada: {paraphrase(user_input)}")
