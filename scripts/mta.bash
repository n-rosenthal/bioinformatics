#!/scripts/mta.bash
#   Invoca o fastqc para todos os arquivos .fastq de um diretorio
#   Depois, invoca o multiqc para todos os relatórios .html do diretório de output
#
#   Uso: mta.bash <diretorio> <diretorio de output>
#   Uso: mta.bash <diretorio>
#
#   Exemplo: mta.bash /home/usr/sequences /home/usr/output
#   Exemplo: mta.bash /home/usr/sequences


DIR=$1
OUT_DIR=$2

# Verifica se o diretório de output foi informado
# Se não foi informado, usa o diretório de input e informa o usuário
if [ -z "$OUT_DIR" ]; then
    OUT_DIR=$DIR
    echo "O diretório de output será $OUT_DIR"
fi

# Verifica se o diretório de output existe
# Se nao existir, cria
if [ ! -d "$OUT_DIR" ]; then
    mkdir $OUT_DIR
    echo "O diretório de output $OUT_DIR foi criado"
fi

# Chama o fastqc para todos os arquivos .fastq do diretório de input
echo "Analisando os arquivos .fastq do diretório $DIR"
for f in $DIR/*.fastq; do
    echo "Analisando $f ($((i++))/$#)"
    fastqc $f -o $OUT_DIR
done

# Chama o multiqc para todos os relatórios .html do diretório de output
echo "Gerando o multi-relatório do diretório $OUT_DIR"
multiqc $OUT_DIR

exit 0