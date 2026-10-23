import os
import json
import unicodedata
import re

def limpar_nome(texto):
    # Remove acentos
    nfkd = unicodedata.normalize('NFKD', texto)
    palavra_sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
    # Mantém apenas letras, números, espaços, hífens e underscores
    limpo = re.sub(r'[^a-zA-Z0-9\s\-_]', '', palavra_sem_acento)
    # Substitui múltiplos espaços por apenas um e remove espaços nas pontas
    limpo = re.sub(r'\s+', ' ', limpo).strip()
    return limpo

def arrumar_pasta_e_json(pasta_musicas="."):
    json_path = os.path.join(pasta_musicas, "playlist.json")
    
    if not os.path.exists(json_path):
        print("Arquivo playlist.json não encontrado nesta pasta!")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        playlist = json.load(f)

    nova_playlist = []

    print("Limpando e renomeando arquivos...")
    for item in playlist:
        url_antiga = item["url"].replace("./", "")
        # Decodifica caracteres de URL caso estejam codificados
        import urllib.parse
        nome_arquivo_atual = urllib.parse.unquote(url_antiga)
        
        caminho_antigo = os.path.join(pasta_musicas, nome_arquivo_atual)
        
        # Pega o nome base sem extensão (.mp3)
        base_nome = os.path.splitext(os.path.basename(nome_arquivo_atual))[0]
        novo_nome_base = limpar_nome(base_nome)
        novo_nome_arquivo = f"{novo_nome_base}.mp3"
        caminho_novo = os.path.join(pasta_musicas, novo_nome_arquivo)

        # Renomeia o arquivo físico se ele existir
        if os.path.exists(caminho_antigo):
            if caminho_antigo != caminho_novo:
                try:
                    os.rename(caminho_antigo, caminho_novo)
                    print(f"Renomeado: {nome_arquivo_atual} -> {novo_nome_arquivo}")
                except Exception as e:
                    print(f"Erro ao renomear {nome_arquivo_atual}: {e}")
        else:
            print(f"Aviso: Arquivo físico não encontrado: {nome_arquivo_atual}")

        # Atualiza os dados no JSON
        item["url"] = f"./{urllib.parse.quote(novo_nome_arquivo)}"
        nova_playlist.append(item)

    # Salva o novo JSON limpo
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(nova_playlist, f, ensure_ascii=False, indent=4)

    print("\nProcesso concluído! O 'playlist.json' foi atualizado com URLs limpas.")

if __name__ == "__main__":
    arrumar_pasta_e_json()