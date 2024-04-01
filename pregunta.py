"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
from datetime import datetime
import pandas as pd
import re


def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    
    #Eliminar datos duplicados y faltantes
    df.dropna(inplace=True)

    df.sexo = df.sexo.str.lower()

    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    df.idea_negocio = [str.lower(idea.replace("_", " ").replace("-", " ")) for idea in df.idea_negocio]

    df.barrio = [str.lower(barrio).replace("_", " ").replace("-", " ") for barrio in df.barrio]

    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)

    df.estrato = df.estrato.astype(int)

    df["línea_credito"] = [str.lower(linea.strip().replace("-", " ").replace("_", " ").replace(". ", ".")) for linea in
                           df["línea_credito"]]

    df.fecha_de_beneficio = [datetime.strptime(date, "%d/%m/%Y") if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
                             else datetime.strptime(date, "%Y/%m/%d")
                             for date in df.fecha_de_beneficio]

    df.monto_del_credito = [int(monto.replace("$ ", "").replace(".00", "").replace(",", "")) for monto in
                            df.monto_del_credito]

    df.drop_duplicates(inplace=True)

    return df

