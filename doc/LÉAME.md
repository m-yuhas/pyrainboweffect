# pyrainboweffect
## Introducción
Tome imagen como esta:

![Cargando...](../images/demo0_in.png)

Y la transforme:

![Cargando...](../images/demo0_out.gif)

## Comienzo Rápido
* Instale el paquete:

```
pip install pyrainboweffect
```

### Python IPA
En una consola Python, importe el paquete:

```python
>>> import pyrainboweffect
```

Aplique el efecto a un archivo de imagen y guarde el resultado como un GIF:

```python
>>> pyrainboweffect.psychedelic_gif('input.png', 'output.gif')
```

Aplique el efecto a un archivo de imagen y guarde el resultado como un mp4:

```python
>>> pyrainboweffect.psychedelic_mp4('input.png', 'output.gif')
```

### CLI
Para usar la interfaz de línea de órdenes:

```bash
$ python -m pyrainboweffect input.png output.gif
```

## Documentación de IPA
Para la documentación de IPA completa, [clica aquí](api_documentation.md).
Actualmente la documentación es solamente disponible en inglés.

## Teoría de Operación
Parace que este efecto puede ser generado utilizando los pasos siguientes:
1. Convertir la imagen a la escala de grises.
2. Dividir el espacio de intensidad en el mismo número de particiones como
  colores en la esquema de colores.
3. Colocar las regiones de intensidad a sus colores correspondientes.
4. Incrementar la intensidad de todos los pixeles en la imagen original
  (empezar de nuevo a 0 si sucede el desbordamiento aritmético).
5. Regresar al paso 2 y repetir hasta hay cuadros secuenciales suficientes para
  formar una animación.

## Dependencias
Solamente las versiones del Python 3.6 y arriba son compatibles.  Este paquete
debe poder ejecutado en alguno sistema POSIX así como Windows 7 y arriba.

Los paquetes Pypi siguientes son requeridos:
* moviepy
* numpy
* opencv-python

## Cómo Contribuir
Las sugerencias y «pull requests» son bienvenidos. Si encuentra un bug y no
tiene el tiempo para arreglarlo su mismo, por favor abre un problema.

## Tarea Futura
- Aplicar el efecto psicodélico a una imagen animada o video.
