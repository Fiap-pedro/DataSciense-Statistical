import pandas as pd
import numpy as np

dados = pd.read_csv("https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/update/ds_salaries_statistics")

# print(dados.shape)
# print(dados)

print(np.mean(dados["salary_in_usd"]))
