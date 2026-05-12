import os
import stanza
import pandas as pd

# Load Stanza pipeline
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse')

ef_csv = "./Python output files/ef_cond.csv"
base_dir = "./parsed_documents"

# Load CSV file
essays_data = pd.read_csv(ef_csv, sep=";")

cor_dir = os.path.join(base_dir, "corrected")
os.makedirs(cor_dir, exist_ok=True)

# Extract columns
cor_texts = essays_data["corrected"].tolist()
file_names = essays_data.apply(
    lambda row: f"{row['group']}_{row['topicID']}_{row['writingID']}_{row['learnerID']}.conll",
    axis=1
).tolist()

print(f"Created {len(file_names)} file names:")

cor_docs_out = []
i = 1
for t, f_name in zip(cor_texts, file_names):
    print(f"{i}/{len(file_names)} ({i/len(file_names) * 100:.3f} %)")
    
    i += 1
    
    out_path = os.path.join(cor_dir, f_name)
    
    # Skip if already done
    if os.path.exists(out_path):
        # print(f"Skipping (already exists): {f_name}")
        continue

    doc = nlp(t)

    with open(out_path, 'w', encoding='utf-8') as out_file:
        stanza.utils.conll.CoNLL.write_doc2conll(doc, out_file)

