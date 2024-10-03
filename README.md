
# Proyecto de Análisis de Datos: VANGUARD A/B TEST

Este proyecto se centra en el análisis de datos de un experimento digital, utilizando Python y bibliotecas como Pandas, Seaborn y Matplotlib. Se incluyen funciones para cargar, limpiar, analizar y visualizar datos de diferentes fuentes, así como para realizar pruebas estadísticas.

## Tabla de Contenidos

- [Características](#Características)
- [Requisitos](#Requisitos)
- [Instalación](#Instalación)
- [Uso](#Uso)
- [Funciones](#Funciones)
- [Contribuciones](#Contribuciones)
- [Links](#Links)
- [Autoras](#Autoras)

## Características

- Carga y fusión de datos desde múltiples archivos CSV.
- Limpieza de datos y conversión de tipos.
- Cálculo de métricas estadísticas (media, mediana, varianza, etc.).
- Análisis de tasas de finalización y tiempo de permanencia.
- Realización de pruebas de Chi-cuadrado para asociación entre variables.
- Análisis de correlación y categorización de datos demográficos.

## Requisitos

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

## Instalación

Para instalar las dependencias necesarias, puedes utilizar `pip`:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

## Uso

1. **Carga y fusión de datos:**

   Llama a la función `load_and_merge_data` pasando las rutas de tus archivos CSV.

   ```python
   df_final = load_and_merge_data('demo.csv', 'experiment_clients.csv', 'web_data_part1.csv', 'web_data_part2.csv')
   ```

2. **Limpieza de datos:**

   Utiliza la función `clean_data` para limpiar el DataFrame.

   ```python
   df_cleaned = clean_data(df_final)
   ```

3. **Cálculo de métricas estadísticas:**

   Puedes calcular métricas para cualquier columna del DataFrame.

   ```python
   stats = calculate_stat_metrics(df_cleaned, 'column_name')
   ```

4. **Análisis de tasas de finalización:**

   Calcula la tasa de finalización para un paso específico.

   ```python
   completion_rate = calculate_completion_rate(df_cleaned, 'step_name')
   ```

5. **Prueba de Chi-cuadrado:**

   Realiza una prueba de Chi-cuadrado para determinar la asociación entre dos variables.

   ```python
   chi2, p, dof, cramer_v = perform_chi2_test(df_cleaned, 'column1', 'column2')
   ```

6. **Análisis de tiempo de permanencia:**

   Calcula el tiempo que cada visitante pasó en el sitio.

   ```python
   df_with_time = calculate_time_spent(df_cleaned)
   ```

## Funciones

A continuación se detallan las funciones disponibles en `functions.py`:

- **load_and_merge_data**: Carga y fusiona datos de múltiples archivos CSV.
- **clean_data**: Limpia y prepara los datos para el análisis.
- **calculate_stat_metrics**: Calcula métricas estadísticas para una columna específica.
- **calculate_completion_rate**: Calcula la tasa de finalización para un paso dado.
- **perform_chi2_test**: Realiza una prueba de Chi-cuadrado para analizar la independencia de variables.
- **calculate_time_spent**: Calcula el tiempo que los visitantes pasan en el sitio.
- **age_category**: Categorización de clientes por grupos de edad.
- **bal_category**: Categorización de clientes por saldo.
- **tenure_category**: Categorización de clientes por tiempo de permanencia.
- **average_time_spent_by_step**: Calcula el tiempo promedio dedicado a cada paso.
- **time_correlation**: Analiza la correlación del tiempo entre pasos consecutivos.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un "issue" o envía un "pull request".

## Links 

[Enlace a presentación](https://prezi.com/view/mSvrwbefWRkJcKrg1KCv/)
[Enlace a Tableau](https://public.tableau.com/views/Libro1_17277803145900/Historia1?:language=es-ES&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Autoras 

Cristina Ramírez | Beatriz Tranche
