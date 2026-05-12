
import pandas as pd
import pandas as pd
import xml.etree.ElementTree as ET
import os

# parse the XML file
tree = ET.parse('./input files/EFwrittenTasks.xml')
root = tree.getroot()

# extract data into a list of dicts
rows = []
for item in root.findall('Item'):
    rows.append({
        'levelNumber': item.findtext('levelNumber'),
        'level': item.findtext('level'),
        'unit': item.findtext('unit'),
        'title': item.findtext('title'),
        'topic': item.findtext('topic'),
        'writtenTask': item.findtext('writtenTask').strip() if item.findtext('writtenTask') else None
    })

# create the df
tasks_df = pd.DataFrame(rows)

tasks_df['levelNumber'] = pd.to_numeric(tasks_df['levelNumber'])
tasks_df['unit'] = pd.to_numeric(tasks_df['unit'])

tasks_df.to_csv("./Python output files/EF_written_tasks.csv", sep=";", index=False)


all_ef = pd.read_csv("./input files/ef_POStagged_original_corrected.csv", index_col=0)

cond_topic_ids ={59, 104, 97, 109, 119, 82, 120, 100, 46, 88, 75, 108, 67, 106, 77, 68, 73, 107, 110, 74}
cond_ef = all_ef[all_ef["topicID"].isin(cond_topic_ids)]


# maps ef levels to CEFR
cefr_map = {
    1: 'A1', 2: 'A1', 3: 'A1',
    4: 'A2', 5: 'A2', 6: 'A2',
    7: 'B1', 8: 'B1', 9: 'B1',
    10: 'B2', 11: 'B2', 12: 'B2',
    13: 'C1', 14: 'C1', 15: 'C1',
    16: 'C2'
}

# maps CEFR levels to groupings for this study
group_map = {
    "A2": "lower",
    "B1": "lower",
    "B2": "upper",
    "C1": "upper",
}

# apply mapping to a CEFR column
cond_ef['CEFR'] = cond_ef['level'].map(cefr_map)
cond_ef["group"] = cond_ef['CEFR'].map(group_map)

cond_ef = cond_ef.replace(to_replace=r'<br\s*/?>', value='\n', regex=True)



cond_ef.to_csv("./Python output files/ef_cond.csv", sep=";", index=False)


pd.unique(cond_ef["topic"])


