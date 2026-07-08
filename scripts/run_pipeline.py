from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parents[1]
df = pd.read_csv(root / "outputs/extracted_abstracts.csv")
print(df[["pmid", "year", "compound_or_topic", "mechanism_keyword"]].head(10))
