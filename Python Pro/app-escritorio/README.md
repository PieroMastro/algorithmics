# 🫀 Ruffier Test - Aplicación de Evaluación Cardíaca

**Ruffier Test** es una aplicación de escritorio desarrollada en **Python** y **PyQt5** que guía al usuario a través de la Prueba de Ruffier: un test médico-deportivo utilizado para evaluar la capacidad de recuperación cardíaca y el estado de forma física tras el esfuerzo.

---

## 📋 Tabla de Contenidos
- [Características](#características)
- [¿Qué es la Prueba de Ruffier?](#qué-es-la-prueba-de-ruffier)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Notas Importantes](#notas-importantes)

---

## ✨ Características

* **Interfaz Gráfica Multi-ventana:** Navegación fluida entre la pantalla de bienvenida, toma de datos y reporte de resultados.
* **Diseño Adaptativo (Layouts):** Organización de componentes mediante `QVBoxLayout` y `QHBoxLayout` para garantizar una correcta escala en distintas pantallas.
* **Diagnóstico Personalizado:** Cálculo autoevaluativo considerando la edad del usuario y la variación de sus pulsaciones en tres momentos clave.
* **Código Modular:** Separación limpia de responsabilidades en diferentes archivos `.py` (mantenimiento simple y escalable).

---

## 🩺 ¿Qué es la Prueba de Ruffier?

La prueba evalúa el rendimiento cardíaco midiendo la frecuencia cardíaca en tres etapas de 15 segundos:

1. **$P_1$ (Pulso 1):** Pulsaciones en reposo completo (durante 15 segundos).
2. **$P_2$ (Pulso 2):** Pulsaciones inmediatamente después de realizar **30 sentadillas en 45 segundos** (durante 15 segundos).
3. **$P_3$ (Pulso 3):** Pulsaciones tras 1 minuto de descanso, tomadas en los últimos 15 segundos del minuto.

### Fórmula del Índice de Ruffier:

$$I = \frac{4 \times (P_1 + P_2 + P_3) - 200}{10}$$

El valor obtenido se evalúa junto con la edad del sujeto para determinar su nivel de rendimiento cardíaco (Excelente, Bueno, Satisfactorio, Complejo o Deficiente).

---

## 📁 Estructura del Proyecto

El repositorio sigue una arquitectura modular donde cada pantalla e información global se aísla en su propio archivo:

```text
ruffier-test/
│
├── instr.py        # Módulo de constantes, dimensiones de ventana y textos informativos
├── main.py         # Módulo principal (Ventana de Bienvenida: MainWindow)
├── test.py         # Módulo de captura de datos y ejercicios (TestWin)
└── result.py       # Módulo de procesamiento y diagnóstico final (ResultWin)
```

---

## ⚠️ Notas Importantes
* Esta aplicación tiene fines educativos y de autoevaluación orientativa.

* No sustituye un diagnóstico médico profesional.

* Si experimentas mareos, dolor de pecho o falta de aire durante la prueba, detén el ejercicio inmediatamente.
