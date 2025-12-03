#!/bin/bash

set -e

# ==========================
# CONFIGURAÇÃO
# ==========================
REPEAT_COUNT=${1:-1}   # Número de repetições passado por parâmetro
DEPLOY_SCRIPT="./deploy.sh"
TERRAFORM_DIR="terraform"

# ==========================
# VALIDAÇÕES
# ==========================
if [ ! -f "$DEPLOY_SCRIPT" ]; then
    echo "ERRO: deploy.sh não encontrado no diretório atual."
    exit 1
fi

if [ ! -d "$TERRAFORM_DIR" ]; then
    echo "ERRO: pasta 'terraform' não encontrada."
    exit 1
fi

echo "O processo será executado $REPEAT_COUNT vez(es)"
echo ""

# ==========================
# LOOP PRINCIPAL
# ==========================
for ((i=1; i<=REPEAT_COUNT; i++)); do
    echo "=============================================="
    echo "INÍCIO DO CICLO $i"
    echo "=============================================="

    # --- Executar deploy ---
    echo "Executando deploy.sh..."
    bash "$DEPLOY_SCRIPT"

    # --- Destruir Terraform ---
    echo "Destruindo recursos Terraform..."
    cd "$TERRAFORM_DIR"
    terraform destroy -auto-approve

    # --- Voltar pasta ---
    cd ..

    echo "Ciclo $i concluído!"
    echo ""
done

echo "=============================================="
echo "Processo finalizado após $REPEAT_COUNT execução(ões)."
echo "=============================================="

