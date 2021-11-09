import re
import pandas as pd
import numpy as np
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

#ask for file path and return the dataframe
def load_file():
    print('----------------------------------------------------------------------------------------------------------------------')
    print('Por favor seleccione el archivo que desea limpiar')
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.destroy()
    print('----------------------------------------------------------------------------------------------------------------------')
    return check_file(file_path)

#check if the file is a csv or a xlsx file and return the dataframe
def check_file(file):
    print('Realizando carga del archivo')
    if file.endswith('.csv'):
        return pd.read_csv(file)
    elif file.endswith('.xlsx'):
        return pd.read_excel(file)

if __name__ == '__main__':
    
    print('Bienvenido al aplicativo de limpieza de datos')
    print('----------------------------------------------------------------------------------------------------------------------')
    
    df_ori = pd.DataFrame()
    df_ori = load_file()
    print('----------------------------------------------------------------------------------------------------------------------')
    
    print('Seleccionando columnas objetivo')
    df = df_ori.loc[:, ['Numero Activo','Numero Etiqueta', 'Descripcion', 'ATT8', 'Modelo', 'UAC', 'UR', 'ATT2', 'ATT4', 'ATT5', 'ATT6', 'ATT9', 'ATT11', 'ATT19', 'ATT20', 'ATT24']]
    df = df.drop_duplicates()
    df.reset_index(drop=True, inplace=True)
    print('----------------------------------------------------------------------------------------------------------------------')
    
    print('Removiendo caracteres extra desde la columna Numero Etiqueta')
    chars_to_remove = ['*', ' ']
    regular_expression = '[' + re.escape (''. join (chars_to_remove)) + ']'

    df['Numero Etiqueta'] = df['Numero Etiqueta'].str.replace(regular_expression,'', regex=True)
    df['Numero Etiqueta'] = df['Numero Etiqueta'].str.replace('.','-', regex=True)
    df['Numero Etiqueta'] = df['Numero Etiqueta'].str.replace('REP.','', regex=True)
    df['Numero Etiqueta'] = df['Numero Etiqueta'].str.replace('XW6996','XW-6996', regex=True)
    df['Numero Etiqueta'] = df['Numero Etiqueta'].str.replace('SINMATRICULA','', regex=True)
    df['Numero Etiqueta'] = df['Numero Etiqueta'].str.replace('S/M','', regex=True)

    b=0
    for i, n in enumerate(df['Numero Etiqueta']):
        try:
            a = n.split('-')
            if len(a) > 2:
                if (re.match(r'[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{0}$', n)):
                    df.loc[i, 'Numero Etiqueta'] = n[:-1]
                    b=b+1
                if (re.match(r'[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{1}$', n)):
                    df.loc[i, 'Numero Etiqueta'] = n[:-2]    
                    b=b+1
                if (re.match(r'[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{2}$', n)):
                    df.loc[i, 'Numero Etiqueta'] = n[:-3]
                    b=b+1
                if (re.match(r'[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{3}$', n)):
                    df.loc[i, 'Numero Etiqueta'] = n[:-4]
                    b=b+1
                if (re.match(r'[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{1, 4}-[a-zA-Z0-9]{1, 4}$', n)):
                    df.loc[i, 'Numero Etiqueta'] = n[:-3]
                    b=b+1
        except:
            b=b+0

    df.drop_duplicates(subset='Numero Etiqueta', ignore_index=True, inplace=True)
    print('----------------------------------------------------------------------------------------------------------------------')
    
    print('Corriguiendo errores de ingreso en columna Descripcion')
    df['Descripcion'] = df['Descripcion'].str.replace('ALJIBE PARA AGUA','REMOLQUE ALJIBE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('MINI CARGADOR','MINICARGADOR', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('MONTACARGA CON HORQUILLA','MONTACARGA', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('MOTO PARA NIEVE','MOTO DE NIEVE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('STATION WAGON','SUV', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('SEMIREMOLQUE CAMA BAJA','SEMIREMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('SEMIREMOLQUE EQUIPO LOGISTICO','SEMIREMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('SEMIREMOLQUE DE CARGA','SEMIREMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE DE CARGA','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE ESTANQUE','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE PARA USO EN NIEVE','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE EQUIPO LOGISTICO','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE ALJIBE','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE LIVIANO','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE TRIPLE (MOTOCICLETA)','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE TRIPLE','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE DE ARRASTRE ANIMAL (USO AGRICOLA)','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE MB 2300W','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE PESADO','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE CARGA (CUADRIMOTO)','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('TRINEO DE ARRASTRE PARA MOTO DE NIEVE','TRINEO DE ARRASTRE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('TRINEO DE ARRASTRE ORION PARA MOTO DE NIEVE','TRINEO DE ARRASTRE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('TRACTOR AGRICOLA','TRACTOR', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('CAMIONETA DE TRASNPORTE PERSONAL','CAMIONETA', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('CAMIONETA TRASNPORTE PERSONAL','CAMIONETA', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('CAMIONETA TRASNPORTE SHELTER','CAMIONETA', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('CAMIÓN','CAMION', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('CAMION TRASNPORTE SHELTER','CAMION', regex=False)
    # df['Descripcion'] = df['Descripcion'].str.replace('CAMIÓN TRASNPORTE SHELTER','CAMION', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('CAMION TRANSPORTE SHELTER','CAMION', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('JEEP DE TRASNPORTE','JEEP', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('CAMIONETA PARA ESTACION REPETIDORA','CAMIONETA', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('REMOLQUE ALGIBE','REMOLQUE', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace(' CAMA BAJA ','CAMA BAJA', regex=False)
    df['Descripcion'] = df['Descripcion'].str.replace('CAMION DE TRANSPORTE','CAMION', regex=False)
    print('----------------------------------------------------------------------------------------------------------------------')

    print('Corrigiendo errores de ingreso en columna Marca (ATT8)')
    df['ATT8'] = df['ATT8'].str.replace('ALTO AMERICAN- LINCOLN','AMERICAN LINCOLN', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('AM GENERAL','AM GEN', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('AM GEN','AM GENERAL', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('ASIA MOTORS','ASIA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('ASIA','ASIA MOTORS', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BARRETT','BARRET', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BARRET','BARRETT', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BEIT ALFA TRAILER CO','BEIT ALFA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BEIT-ALFA TRAILER CO.','BEIT ALFA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BLUMHART','BLUMHARDT', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BOBCAT INGERSOLL RAND','BOBCAT', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BOBCAT MODELO S630 FULLJ','BOBCAT', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BOMBARDIER BRP SKI DOO','BOMBARDIER', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BOX/CB2.SANCHEZ/Balatas,Neumaticos,Correa distribucion y turbo con eje gastados','', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('BROCK HOUSE','BROCKHOUSE', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('CARDOEN','CARDOEN-MOWAG', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('CATARPILLAR','CATERPILLAR', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('CATERPILAR','CATERPILLAR', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('CATERPILLAR 130-G','CATERPILLAR', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('CATERPILLAR D6D','CATERPILLAR', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('COMAND CAR','COMMANDCAR', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('COMANDCAR','COMMANDCAR', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('COMMANCAR','COMMANDCAR', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('COMMAND CAR','COMMANDCAR', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('CUSTROM','CUSTOM', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('DAHIATSU','DAIHATSU', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('FDERAL MOTOR COMPANY','FEDERAL MOTOR COMPANY', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('FEDERAL MOTOR COMPANY','FEDERAL', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('FEDERAL','FEDERAL MOTOR COMPANY', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('FMC CORPORATION','FEDERAL MOTOR COMPANY', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('FORD RANGER','FORD', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('HYNDAI','HYUNDAI', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('HYUNDAY','HYUNDAI', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('HYUYNDAI','HYUNDAI', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('ELANTRA','HYUNDAI', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('INCA FREUHAUF','INCA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('INCA FRUEHAUF','INCA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('ISUSU','ISUZU', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('IZUSU','ISUZU', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('JOHNSON','TEST', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('JHON DEERE','JOHN', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('JOHN DEERE','JOHN', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('JHON DEER','JOHN', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('JOHN','JOHN DEERE', regex=False)
    # df['ATT8'] = df['ATT8'].str.replace('JOHN','JOHN DEEREE', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('TEST','JOHNSON', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('KIA MOTORS','KIA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('KIA SORENTO','KIA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('KOMATSU PC 130-8','KOMATSU', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('M/BENZ','MERCEDES BENZ', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('MERC. BENZ','MERCEDES BENZ', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('MERCEDEZ BENZ','MERCEDES BENZ', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('MERCEDEZ-BENZ','MERCEDES BENZ', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('MERCEDES BENZ   ','MERCEDES BENZ', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('MAK','MACK', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('nissan','NISSAN', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('NETZER SERENI','NETZER', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('N.A','', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('N.A.','', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('SIM MARCA','', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('SIN INFORMACION','', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('SIN MARCA','', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('NO APLICA','', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('S/M','', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('POLARIS DEFENSE','POLARIS', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('POLARIS','DEFENSE', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('RANDOM','RANDON', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('TECNOVE SEGURITY','TECNOVE SECURITY', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('TOYOTA CAMRI','TOYOTA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('TOYOTA LAND CRUISER II','TOYOTA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('TOYOTA LAND CRUISER','TOYOTA', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('WILLYS BANTAM','WILLYS', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('SUZUKY','SUZUKI', regex=False)
    df['ATT8'] = df['ATT8'].str.replace('ZUZUKI DR 350','SUZUKI', regex=False)
    print('----------------------------------------------------------------------------------------------------------------------')

    print('Limpiar columna de Tipo de Combustible')
    df['ATT19']=np.where(df['ATT19'].str.contains('DIESEL'), 'DIESEL', df['ATT19'])
    df['ATT19']=np.where(df['ATT19'].str.contains('BENCI'), 'BENCINERO', df['ATT19'])
    df['ATT19']=np.where(df['ATT19'].str.contains('NO APLICA'), 'NO APLICA', df['ATT19'])
    df['ATT19']=np.where((df['ATT19'].str.contains('NO APLICA')) | (df['ATT19'].str.contains('DIESEL')) | (df['ATT19'].str.contains('BENCI')), df['ATT19'], 'NO APLICA')
    print('----------------------------------------------------------------------------------------------------------------------')

    df_test = df.copy()
    print('Seleccionar solo Tipos de vehiculos especificos')
    df_test = df_test[df_test.Descripcion != 'CARRO BLINDADO']
    df_test = df_test[df_test.Descripcion != 'EXCAVADORA']
    df_test = df_test[df_test.Descripcion != 'BARREDORA']
    df_test = df_test[df_test.Descripcion != 'CARGADOR FRONTAL']
    df_test = df_test[df_test.Descripcion != 'GRUA']
    df_test = df_test[df_test.Descripcion != 'TANQUE']
    df_test = df_test[df_test.Descripcion != 'TRACTOR']
    df_test = df_test[df_test.Descripcion != 'ARTILLERIA AUTOPROPULSADA']
    df_test = df_test[df_test.Descripcion != 'CHASIS PARA OBUS']
    df_test = df_test[df_test.Descripcion != 'CHASIS DE TANQUE']
    df_test = df_test[df_test.Descripcion != 'ESTANQUE PARA COMBUSTIBLE']
    df_test = df_test[df_test.Descripcion != 'RETROEXCAVADORA']
    df_test = df_test[df_test.Descripcion != 'MINICARGADOR']
    df_test = df_test[df_test.Descripcion != 'RETROCARGADOR']
    df_test = df_test[df_test.Descripcion != 'MOTONIVELADORA']
    df_test = df_test[df_test.Descripcion != 'BULLDOZER']
    df_test = df_test[df_test.Descripcion != 'RODILLO COMPACTADOR']
    df_test = df_test[df_test.Descripcion != 'VEHICULO CORTA PASTO']
    df_test = df_test[df_test.Descripcion != 'CARRO']
    print('----------------------------------------------------------------------------------------------------------------------')

    print('Seleccionar solo material activo')
    df_test = df_test[df_test.ATT5 == 'ACTIVO']
    print('----------------------------------------------------------------------------------------------------------------------')
    
    print('Limpiar columna de tamaño de estanque de combustible (ATT20)')
    df_test['ATT20'] = df_test['ATT20'].str.extract('(\d+)', expand=False)
    df_test['ATT20'] = pd.to_numeric(df_test['ATT20'])
    print('----------------------------------------------------------------------------------------------------------------------')

    df_test.to_excel('Clean_Bd_Vehic.xlsx', encoding='latin-1')
    
    print('Archivo Clean_Bd_Vehic.xlsx creado')
    print('Proceso finalizado')
    print('----------------------------------------------------------------------------------------------------------------------')