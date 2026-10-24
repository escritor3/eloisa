import os
import json
import unicodedata
import re
import urllib.parse

def limpar_nome(texto):
    nfkd = unicodedata.normalize('NFKD', texto)
    palavra_sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
    limpo = re.sub(r'[^a-zA-Z0-9\s\-_]', '', palavra_sem_acento)
    limpo = re.sub(r'\s+', ' ', limpo).strip()
    return limpo

def arrumar_pasta_e_json(pasta_musicas="."):
    json_path = os.path.join(pasta_musicas, "playlist.json")
    
    if not os.path.exists(json_path):
        print("Arquivo playlist.json não encontrado nesta pasta!")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            playlist = json.load(f)
        except Exception as e:
            print(f"Erro ao ler o JSON: {e}. Verifique se o playlist.json está preenchido corretamente.")
            return

    print("Renomeando arquivos físicos para corresponder ao JSON...")
    for item in playlist:
        # Pega o nome esperado pelo JSON limpo
        url_limpa = item["url"].replace("./", "")
        nome_desejado = urllib.parse.unquote(url_limpa)
        caminho_destino = os.path.join(pasta_musicas, nome_desejado)

        # Procura na pasta por arquivos MP3 parecidos ou tenta achar o arquivo original antigo
        # Como alteramos o JSON, vamos procurar arquivos físicos soltos na pasta para renomear
        encontrado = False
        for arquivo in os.listdir(pasta_musicas):
            if arquivo.endswith(".mp3") and arquivo != nome_desejado:
                # Compara sem acentos/espaços para achar o correspondente antigo
                if limpar_nome(os.path.splitext(arquivo)[0]).lower() == limpar_nome(os.path.splitext(nome_desejado)[0]).lower():
                    caminho_antigo = os.path.join(pasta_musicas, arquivo)
                    try:
                        os.rename(caminho_antigo, caminho_destino)
                        print(f"Renomeado: {arquivo} -> {nome_desejado}")
                        encontrado = True
                        break
                    except Exception as e:
                        print(f"Erro ao renomear {arquivo}: {e}")
        
        if not encontrado and os.path.exists(caminho_destino):
            print(f"Arquivo já está com o nome correto: {nome_desejado}")

    print("\nProcesso concluído com sucesso!")

if __name__ == "__main__":
    arrumar_pasta_e_json()