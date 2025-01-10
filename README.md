# Juego del Ahorcado en Python

## ✨ Acerca de
**Juego del Ahorcado** Este es un simple juego del ahorcado implementado en Python. El objetivo del juego es adivinar una palabra oculta, letra por letra, antes de que se agoten los intentos. El jugador tiene un número limitado de intentos para acertar las letras de la palabra secreta.

---

## 🛠 Tecnologías utilizadas
- Python 3
- Terminal/Consola

---

## 📝 Requisitos
Asegúrate de tener instalado:
- Python 3.x o superior

---

## 🚀 Instalación
1. Clona este repositorio:  
   ```bash
   git clone https://github.com/usuario/repositorio.git
   
2. Navega a la carpeta del proyecto:
   ```bash
   cd nombre-del-repositorio

3. Ejecuta el juego:
   ```
   py hangman.py

## 
# Juego del Ahorcado en Python

Este es un simple juego del ahorcado implementado en Python. El objetivo del juego es adivinar una palabra oculta, letra por letra, antes de que se agoten los intentos. El jugador tiene un número limitado de intentos para acertar las letras de la palabra secreta.

## Requisitos

Para ejecutar este proyecto, necesitas tener Python instalado en tu sistema. Puedes descargar la última versión de Python desde su sitio web oficial: [python.org](https://www.python.org/).

Este juego no requiere librerías externas, por lo que no es necesario instalar dependencias adicionales.

## Instalación

1. Clona este repositorio en tu máquina local usando el siguiente comando:
    ```bash
    git clone https://github.com/tu_usuario/nombre-del-repositorio.git
    ```
2. Navega a la carpeta del proyecto:
    ```bash
    cd nombre-del-repositorio
    ```
3. El juego se puede ejecutar directamente desde el archivo `hangman.py` (o el archivo que uses para ejecutar el juego).

## Cómo Jugar

1. Ejecuta el archivo `hangman.py`:
    ```bash
    python hangman.py
    ```
2. El juego seleccionará aleatoriamente una palabra de una lista predefinida y la mostrará con guiones bajos (`_`) representando cada letra. El jugador debe adivinar las letras de la palabra.
3. En cada turno, ingresa una letra. Si la letra está en la palabra, se revelará en su lugar. Si la letra no está en la palabra, perderás un intento.
4. Tienes un total de 6 intentos para adivinar la palabra. Si adivinas la palabra antes de que se acaben los intentos, ¡ganas! Si no, el juego terminará y perderás.
5. Después de cada juego, se te preguntará si deseas jugar de nuevo.

## Características

- El juego tiene una representación gráfica del ahorcado que se va actualizando con cada intento fallido.
- El número de intentos es limitado a 6, representados por el ahorcado.
- Puedes agregar nuevas palabras fácilmente a la lista de palabras del juego.


## Funcionalidad del Código

- **`make_guess()`**: Solicita al usuario una letra para adivinar.
- **`_get_stickman_stages()`**: Devuelve las diferentes etapas del ahorcado que se van mostrando a medida que se pierden intentos.
- **`ask_to_play_again()`**: Pregunta al usuario si desea jugar otra vez.
- **Clase `Hangman`**: Contiene la lógica principal del juego. Permite gestionar el estado del juego, la palabra secreta, los intentos y la interacción con el jugador.

## Contribuciones

Si deseas contribuir a este proyecto, por favor realiza un **fork** y envía un **pull request** con tus cambios. Asegúrate de que el código esté bien documentado y siga las mejores prácticas.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

