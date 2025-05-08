import pandas as pd

file_path = "employes.csv"
data = pd.read_csv(file_path)

print("Les cinq premières lignes du fichier CSV:")
print(data.head())

average_age = data['âge'].mean()
print(f"La moyenne d'âge des employés est: {average_age:.2f} ans")
