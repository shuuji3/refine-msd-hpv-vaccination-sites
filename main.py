from glob import glob

import pandas as pd
import zenhan

header = ['city', 'name','postal_code', 'address', 'phone', 'departments', 'has_female_doctor',
          'conduct_cervical_cancer_screening', 'website']

df_all = pd.DataFrame()
for csv_path in glob('data/raw/*.csv'):
    df = pd.read_csv(csv_path, names=header, index_col=1, usecols=header)

    df['address'] = df.address.apply(lambda a: zenhan.z2h(str(a), mode=zenhan.DIGIT).replace('－', '-'))
    df['departments'] = df.departments.apply(lambda s: s.split('、') if not pd.isna(s) else [])
    df['has_female_doctor'] = df.has_female_doctor.apply(lambda c: c == '○')
    df['conduct_cervical_cancer_screening'] = df.conduct_cervical_cancer_screening.apply(lambda c: c == '○')
    df_all = pd.concat([df_all, df])

df_all.to_csv('data/all.csv', index_label='name')
df_all.to_json('data/all.json', orient='records', force_ascii=False, indent=4)
