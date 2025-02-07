# Calculadora-de-reas-con-Tkinter

El propósito de este programa es crear una calculadora de áreas de figuras geométricas básicas (cuadrado, rectángulo, triángulo y círculo) utilizando una interfaz gráfica desarrollada con la librería tkinter de Python. El programa permite al usuario seleccionar una figura, ingresar los valores necesarios (como el lado, base, altura o radio) y calcular el área correspondiente, mostrando el resultado en una ventana emergente. Además, el programa incluye validaciones para asegurar que los valores ingresados sean positivos y maneja errores de manera visual.

El análisis programático del código se divide en los siguientes aspectos:

Interfaz gráfica: El programa utiliza tkinter para crear una ventana principal con un menú desplegable que permite al usuario seleccionar la figura geométrica. Dependiendo de la figura seleccionada, se muestran los campos de entrada correspondientes (lado, base, altura o radio). La interfaz también incluye imágenes de las figuras para mejorar la experiencia del usuario.

Cálculo de áreas: El programa implementa funciones para calcular el área de cada figura. Para el cuadrado, se eleva al cuadrado el valor del lado; para el rectángulo, se multiplica la base por la altura; para el triángulo, se multiplica la base por la altura y se divide entre dos; y para el círculo, se utiliza la fórmula del área de un círculo (π * radio²).

Validación de datos: Antes de realizar los cálculos, el programa verifica que los valores ingresados sean positivos. Si el usuario introduce valores no válidos (como números negativos o cero), se muestra un mensaje de error en una ventana emergente.

Manejo de errores: El programa utiliza bloques try-except para capturar errores, como la entrada de valores no numéricos o valores negativos. En caso de error, se muestra una ventana emergente con un mensaje de error y una imagen indicativa.

Ventanas emergentes: El programa utiliza ventanas emergentes (Toplevel) para mostrar los resultados de los cálculos o los mensajes de error. Estas ventanas incluyen imágenes y botones para cerrarlas, lo que mejora la interacción con el usuario.

Interacción con el usuario: El programa permite al usuario calcular el área presionando un botón o la tecla "Enter". Además, los campos de entrada se ajustan dinámicamente según la figura seleccionada, lo que facilita la introducción de datos.

Diseño visual: El programa utiliza colores, fuentes pixeladas e imágenes para crear una interfaz atractiva y coherente. Los botones y campos de entrada tienen un diseño personalizado que mejora la experiencia visual.
