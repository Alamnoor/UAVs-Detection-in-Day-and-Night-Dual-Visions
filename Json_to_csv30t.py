import pandas as pd
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_200320_1_2/IR_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR30/Label/IR30.csv', index = None, header=True)
