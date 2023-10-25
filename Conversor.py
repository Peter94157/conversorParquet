
import pandas as pd
from tkinter import messagebox
import easygui

nome=easygui.enterbox ('Qual o nome do arquivo ?? ')
df = pd.read_parquet(nome+'.parquet')
df.to_csv(nome+".csv", index=False)
