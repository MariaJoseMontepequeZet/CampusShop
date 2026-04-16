# CampusShop: E-commerce Universitario
Sistema integral de compras en línea diseñado para la comunidad universitaria, enfocado en la venta de artículos promocionales y suministros académicos.

> Hecho por **María José Montepeque Zet**

### Tabla de contenido
* [Introducción](#introducción)
* [¿Qué hace este proyecto exactamente?](#qué-hace-este-proyecto-exactamente)
* [Antes de empezar](#antes-de-empezar)
* [Cómo ponerlo a andar (Paso a paso)](#cómo-ponerlo-a-andar-paso-a-paso)
* [Estructura del Proyecto](#estructura-del-proyecto)

---

### Introducción
CampusShop es una plataforma web moderna que permite a los estudiantes gestionar sus compras institucionales de manera eficiente. El proyecto destaca por una interfaz limpia, un flujo de usuario intuitivo y un diseño **responsive** que se adapta a dispositivos móviles y de escritorio.

> [!NOTA]
> Esto es una nota especial: El diseño visual utiliza una paleta de colores profesional (#2d4343) y tipografía **Quicksand** para garantizar una experiencia de usuario amigable y académica.

---

### ¿Qué hace este proyecto exactamente?
El sistema cubre el ciclo completo de una tienda virtual, desde la selección del producto hasta la confirmación del pago:
* **Gestión de Perfil**: Panel centralizado donde el usuario puede ver su nivel de cliente, crédito disponible y accesos directos.
* **Carrito y Checkout**: Flujo de compra completo con validación visual de productos, cálculo de totales y formularios de pago con tarjeta.
* **Historial de Pedidos**: Registro detallado de compras anteriores con estados dinámicos (Entregado, En camino, Procesando) y visualización de productos.
* **Gestión de Direcciones**: Almacenamiento de múltiples ubicaciones dentro y fuera del campus universitario.
* **Soporte y Contacto**: Canal directo de comunicación con la administración para resolución de dudas o reclamos.

---

### Antes de empezar
Para visualizar y trabajar en este proyecto, necesitas lo siguiente:
* **Navegador Web**: (Chrome, Firefox o Edge actualizado para soporte completo de CSS Grid y Flexbox).
* **Editor de Código**: Visual Studio Code (recomendado para manejar la estructura de carpetas).
* **Recursos Gráficos**: Carpeta `/imagenes` con los archivos `logo.png`, `camiseta-polo.png`, `mochila.png`, `gorra.png` y `taza.png`.

---

### Cómo ponerlo a andar (Paso a paso)

1. **Descarga el código:**
   Descarga el archivo ZIP o clona el repositorio que contiene todos los archivos HTML y la carpeta de estilos CSS.

2. **Organización de archivos:**
   Asegúrate de mantener la jerarquía de carpetas para que los enlaces y estilos funcionen:
   * **Raíz**: Archivos `.html` (index, perfil, vacio, historial, contacto, direcciones, pago).
   * **/css**: Archivos `.css` individuales para cada sección.
   * **/imagenes**: Recursos visuales y logotipos.

3. **Ejecución:**
   Abre el archivo `index.html` en tu navegador preferido para iniciar la experiencia de la tienda.

---

### Estructura del Proyecto
El código se ha organizado de forma modular para facilitar su edición:

| Archivo HTML | Función Principal | CSS Asociado |
| :--- | :--- | :--- |
| `index.html` | Catálogo principal de productos | `layout.css` |
| `perfil.html` | Panel de control del usuario | `perfil.css` |
| `checkout.html` | Pasarela de pago y resumen de orden | `checkout.css` |
| `historial.html` | Registro histórico de compras | `historial.css` |
| `contacto.html` | Formulario de ayuda al cliente | `contacto.css` |
| `vacio.html`| Estado de error/vacío del carrito | `carrito.css` |

---

### Especificaciones Técnicas
* **Precisión Numérica**: Todos los cálculos internos y visualizaciones de moneda se manejan con un formato estricto de **4.0000 decimales** en lógica y **2.00 decimales** en la interfaz de usuario.
* **Diseño Visual**: Basado en bordes redondeados de **15.00px** para una estética moderna y profesional.
* **Tipografía**: Implementación de Google Fonts (Quicksand) para mejorar la legibilidad académica.