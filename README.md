 Proyecto Xignus - Análisis Financiero

 Descripción
Sistema de análisis financiero que procesa datos de facturas, pagos, productos y clientes para generar reportes ejecutivos mensuales, análisis de flujo de caja y métricas financieras clave.
 Requisitos Previos
- Python 3.8 o superior
- pip 
 Instalación

1. Crear Entorno Virtual
Es altamente recomendable usar un entorno virtual para aislar las dependencias del proyecto.

Windows
```bash
python -m venv venv
venv\Scripts\activate
```



2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

Librerías Utilizadas

Core
- **pandas**: Manipulación y análisis de datos
- **numpy**: Computación numérica
- **pyarrow**: Lectura/escritura de archivos Parquet

 Jupyter
- **jupyter**: Entorno interactivo de notebooks
- **ipython**: Shell interactivo mejorado
- **ipykernel**: Kernel de Python para Jupyter

Estructura del Proyecto
```
proyecto_xignus/
├── analisis_financiero.ipynb    # Notebook principal con análisis
├── dataset_creados/              # Carpeta con archivos Parquet
│   ├── invoice.parquet
│   ├── invoiceLine.parquet
│   ├── partner.parquet
│   ├── product.parquet
│   ├── payment.parquet
│   └── paymentApplication.parquet
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Este archivo
```

Uso

1. Activar el entorno virtual
2. Abrir Jupyter Notebook:
```bash
jupyter notebook
```
3. Navegar a `analisis_financiero.ipynb` y ejecutar las celdas

Análisis Incluidos

- ✅ **Cuentas por Cobrar (AR)**: Análisis de antigüedad de saldos
- ✅ **Flujo de Caja**: Proyección semanal de entradas y salidas
- ✅ **Márgenes**: Análisis de rentabilidad por producto y cliente
- ✅ **Métricas Financieras**: DSO, DPO, DIO, CCC
- ✅ **Panel Ejecutivo Mensual**: Resumen consolidado mensual

Notas
- Los archivos de datos deben estar en formato Parquet en la carpeta `dataset_creados/`
- El análisis utiliza la fecha actual para cálculos de vencimientos

Autor
Francisco Luis Delgado Santana
