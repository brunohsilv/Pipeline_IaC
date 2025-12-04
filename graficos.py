import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Criar pasta para imagens
os.makedirs("benchmark_images", exist_ok=True)

# Ler CSV consolidado
df = pd.read_csv("benchmarks/all_benchmarks.csv")

# Gráfico 1: Tempo Total por execução (barplot) - AJUSTADO
plt.figure(figsize=(14, 6))
ax = sns.barplot(x='run_id', y='total_seconds', data=df, palette="Blues")
plt.title("Tempo Total por Execução do Pipeline", fontsize=14)
plt.xlabel("Execução", fontsize=12)
plt.ylabel("Tempo Total (s)", fontsize=12)

# Mostrar labels intercalados (1 sim, 2 não, 3 sim, 4 não...)
labels = [df['run_id'].iloc[i] if i % 2 == 0 else '' for i in range(len(df))]
ax.set_xticklabels(labels, rotation=0, fontsize=11)

plt.tight_layout()
plt.savefig("benchmark_images/tempo_total_por_execucao.png", dpi=150)
plt.close()

# Gráfico 2: Boxplot do tempo total
plt.figure(figsize=(8,5))
sns.boxplot(y='total_seconds', data=df, palette="Pastel1")
plt.title("Distribuição do Tempo Total do Pipeline")
plt.ylabel("Tempo Total (s)")
plt.savefig("benchmark_images/boxplot_tempo_total.png")
plt.close()

# Gráfico 3: Linha do tempo total por execução
plt.figure(figsize=(10,5))
sns.lineplot(x='run_id', y='total_seconds', data=df, marker='o', color='green')
plt.title("Evolução do Tempo Total do Pipeline")
plt.xlabel("Execução")
plt.ylabel("Tempo Total (s)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("benchmark_images/linha_evolucao_tempo_total.png")
plt.close()

print("Gráficos gerados em: benchmark_images/")