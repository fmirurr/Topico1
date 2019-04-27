import pandas as pd
from Datos_Faltantes import *
from Funcion_1D import *

#cargar archivos csv
aisles = pd.read_csv('BD/aisles.csv', sep=',')
departments = pd.read_csv('BD/departments.csv', sep=',')
order_products_prior = pd.read_csv('BD/order_products__prior.csv', sep=',')
order_products_train = pd.read_csv('BD/order_products__train.csv', sep=',')
orders = pd.read_csv('BD/orders.csv', sep=',')
products = pd.read_csv('BD/products.csv', sep=',')

#datos faltantes = -1
aisles_1 = aisles
departments_1 = departments
order_products_prior_1 = order_products_prior
order_products_train_1 = order_products_train
orders_1 = orders
products_1 = products

#llena con -1 cuando faltan datos
Llenar(aisles_1)
Llenar(departments_1)
Llenar(order_products_prior_1)
Llenar(order_products_train_1)
Llenar(orders_1)
Llenar(products_1)

#datos faltantes = eliminados
aisles_eli = aisles
departments_eli = departments
order_products_prior_eli = order_products_prior
order_products_train_eli = order_products_train
orders_eli = orders
products_eli = products

#elimina las filas que falten datos
Eliminar(aisles_eli)
Eliminar(departments_eli)
Eliminar(order_products_prior_eli)
Eliminar(order_products_train_eli)
Eliminar(orders_eli)
Eliminar(products_eli)


#identificar tablas que le faltan datos (se guarda archivo en carpeta Archivos[tiene que estar creada])
Arch_Dat_Falt = open('Archivos/Datos_Faltantes', 'a')
Arch_Dat_Falt.write("aisles: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(aisles, Arch_Dat_Falt)))
Arch_Dat_Falt.write("departments: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(departments, Arch_Dat_Falt)))
Arch_Dat_Falt.write("order_products_prior: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(order_products_prior, Arch_Dat_Falt)))
Arch_Dat_Falt.write("order_products_train: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(order_products_train, Arch_Dat_Falt)))
Arch_Dat_Falt.write("orders: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(orders, Arch_Dat_Falt)))
Arch_Dat_Falt.write("products: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(products, Arch_Dat_Falt)))
Arch_Dat_Falt.close()

#se hacen los procesos de 1D con los datos originales
Arch_1D_Original = open('Archivos/Archivo_1D', 'a')
Arch_1D_Original.write("aisles: \n")
Arch_1D_Original.write(str(TipoDatos(aisles, Arch_1D_Original)))
Arch_1D_Original.write("departments: \n")
Arch_1D_Original.write(str(TipoDatos(departments, Arch_1D_Original)))
Arch_1D_Original.write("order_products_prior: \n")
Arch_1D_Original.write(str(TipoDatos(order_products_prior, Arch_1D_Original)))
Arch_1D_Original.write("order_products_train: \n")
Arch_1D_Original.write(str(TipoDatos(order_products_train, Arch_1D_Original)))
Arch_1D_Original.write("oreders: \n")
Arch_1D_Original.write(str(TipoDatos(orders, Arch_1D_Original)))
Arch_1D_Original.write("products: \n")
Arch_1D_Original.write(str(TipoDatos(products, Arch_1D_Original)))
Arch_1D_Original.close()

#se hacen los procesos de 1D con los datos NaN = -1
Arch_1D_1 = open('Archivos/Archivo_1D_1', 'a')
Arch_1D_1.write("aisles: \n")
Arch_1D_1.write(str(TipoDatos(aisles, Arch_1D_1)))
Arch_1D_1.write("departments: \n")
Arch_1D_1.write(str(TipoDatos(departments, Arch_1D_1)))
Arch_1D_1.write("order_products_prior: \n")
Arch_1D_1.write(str(TipoDatos(order_products_prior, Arch_1D_1)))
Arch_1D_1.write("order_products_train: \n")
Arch_1D_1.write(str(TipoDatos(order_products_train, Arch_1D_1)))
Arch_1D_1.write("oreders: \n")
Arch_1D_1.write(str(TipoDatos(orders, Arch_1D_1)))
Arch_1D_1.write("products: \n")
Arch_1D_1.write(str(TipoDatos(products, Arch_1D_1)))
Arch_1D_1.close()

#se hacen los procesos de 1D con los datos NaN eliminados
Arch_1D_Eliminados = open('Archivos/Archivo_1D_eliminados', 'a')
Arch_1D_Eliminados.write("aisles: \n")
Arch_1D_Eliminados.write(str(TipoDatos(aisles, Arch_1D_Eliminados)))
Arch_1D_Eliminados.write("departments: \n")
Arch_1D_Eliminados.write(str(TipoDatos(departments, Arch_1D_Eliminados)))
Arch_1D_Eliminados.write("order_products_prior: \n")
Arch_1D_Eliminados.write(str(TipoDatos(order_products_prior, Arch_1D_Eliminados)))
Arch_1D_Eliminados.write("order_products_train: \n")
Arch_1D_Eliminados.write(str(TipoDatos(order_products_train, Arch_1D_Eliminados)))
Arch_1D_Eliminados.write("oreders: \n")
Arch_1D_Eliminados.write(str(TipoDatos(orders, Arch_1D_Eliminados)))
Arch_1D_Eliminados.write("products: \n")
Arch_1D_Eliminados.write(str(TipoDatos(products, Arch_1D_Eliminados)))
Arch_1D_Eliminados.close()
