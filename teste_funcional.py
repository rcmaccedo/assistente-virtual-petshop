# Simulação de funcionamento do Assistente Virtual
def responder_cliente(pergunta):
    conhecimento = {
        "horario": "Segunda a Sexta, das 08h às 20h. Sábados das 08h às 12h.",
        "local": "Rua dos Pets, nº 123, Bairro Central.",
        "vacinas": "Aplicamos V10 e Antirrábica."
    }
    
    pergunta = pergunta.lower()
    
    if "horário" in pergunta or "hora" in pergunta:
        return f"PetBot: Nosso horário é {conhecimento['horario']}"
    elif "onde" in pergunta or "endereço" in pergunta:
        return f"PetBot: Estamos na {conhecimento['local']}"
    elif "vacina" in pergunta:
        return f"PetBot: {conhecimento['vacinas']}"
    else:
        return "PetBot: Desculpe, não encontrei essa informação. Pode ligar para (11) 9999-9999?"

# Teste rápido
print(responder_cliente("Qual o horário de vocês?"))
print(responder_cliente("Onde fica a clínica?"))
