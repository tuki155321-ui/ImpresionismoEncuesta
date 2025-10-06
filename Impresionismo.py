import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Evaluación Impresionismo",
    page_icon="🎨",
    layout="centered"
)

# Datos de las preguntas
preguntas = [
    {
        "pregunta": "¿Cuál de estas características es la MÁS definitoria de la pintura impresionista?",
        "opciones": [
            "El uso de colores puros y sombras coloreadas",
            "La representación de temas mitológicos e históricos", 
            "La búsqueda del realismo fotográfico y el detalle minucioso"
        ],
        "respuesta_correcta": 0,
        "explicacion": {
            "correcta": "Los impresionistas se caracterizaron por aplicar pinceladas sueltas de colores puros, evitando el negro para las sombras y sustituyéndolo por colores complementarios, captando así la luz y la atmósfera del momento.",
            "incorrecta": "La representación de temas mitológicos era característica del arte académico previo, y la búsqueda del realismo fotográfico es lo opuesto al enfoque impresionista."
        }
    },
    {
        "pregunta": "¿Qué compositor es ampliamente reconocido como una figura central en la música impresionista?",
        "opciones": [
            "Ludwig van Beethoven",
            "Claude Debussy", 
            "Richard Wagner"
        ],
        "respuesta_correcta": 1,
        "explicacion": {
            "correcta": "Claude Debussy es considerado el padre del impresionismo musical. Obras como 'Claro de Luna' y 'El Mar' buscan crear atmósferas y coloridos sonoros, paralelos a lo que hacían los pintores impresionistas.",
            "incorrecta": "Beethoven fue del período clásico-romántico, y Wagner, aunque influyente, pertenece al romanticismo tardío."
        }
    },
    {
        "pregunta": "La obra 'Impresión, sol naciente' de Claude Monet es fundamental porque:",
        "opciones": [
            "Fue la pintura más cara de su época",
            "Dio nombre al movimiento impresionista", 
            "Representa la perfección del realismo académico"
        ],
        "respuesta_correcta": 1,
        "explicacion": {
            "correcta": "El crítico Louis Leroy usó el título de esta obra de manera despectiva para burlarse de ella, acuñando el término 'impresionistas' para el grupo. El nombre fue adoptado por los propios artistas.",
            "incorrecta": "No fue particularmente cara en su tiempo y fue ridiculizada inicialmente. Además, es el antítesis del realismo académico."
        }
    },
    {
        "pregunta": "¿Qué técnica pictórica, utilizada frecuentemente por los impresionistas, consiste en aplicar pinceladas cortas y gruesas de color para capturar la vibración de la luz?",
        "opciones": [
            "Esfumado",
            "Claroscuro", 
            "Pincelada gestáltica o 'touche'"
        ],
        "respuesta_correcta": 2,
        "explicacion": {
            "correcta": "La 'touche' o pincelada visible y fragmentada es una seña de identidad del impresionismo. Permitía que los colores se mezclaran ópticamente en el ojo del espectador.",
            "incorrecta": "El esfumado es renacentista y el claroscuro pertenece al barroco."
        }
    },
    {
        "pregunta": "Además de la pintura, el impresionismo también se manifestó en la literatura. ¿Qué caracterizaba principalmente al impresionismo literario?",
        "opciones": [
            "La descripción detallada de los hechos y la trama lineal",
            "La priorización de la sensación subjetiva y la atmósfera sobre la narración", 
            "La escritura en verso rimado y métrica estricta"
        ],
        "respuesta_correcta": 1,
        "explicacion": {
            "correcta": "Los escritores impresionistas buscaban transmitir la impresión sensorial inmediata de un momento, fragmentando la realidad y privilegiando la descripción de sensaciones.",
            "incorrecta": "La descripción detallada corresponde al realismo tradicional, y el impresionismo literario se dio principalmente en prosa."
        }
    },
    {
        "pregunta": "¿Qué artista impresionista se especializó en capturar los efectos de la luz en la arquitectura, especialmente en la fachada de la Catedral de Ruan en distintas horas del día?",
        "opciones": [
            "Edgar Degas",
            "Pierre-Auguste Renoir", 
            "Claude Monet"
        ],
        "respuesta_correcta": 2,
        "explicacion": {
            "correcta": "Claude Monet pintó más de 30 versiones de la fachada de la Catedral de Ruan en diferentes condiciones de luz, demostrando su obsesión por cómo la luz modifica la percepción.",
            "incorrecta": "Degas se centró en bailarinas y escenas urbanas, mientras Renoir en figuras humanas y escenas sociales."
        }
    },
    {
        "pregunta": "La primera exposición impresionista en 1874 se caracterizó por:",
        "opciones": [
            "Ser un éxito rotundo de crítica y público desde el primer día",
            "Ser organizada por los artistas al margen del Salón oficial de París", 
            "Contar con el pleno apoyo del gobierno francés y la Academia de Bellas Artes"
        ],
        "respuesta_correcta": 1,
        "explicacion": {
            "correcta": "Al ser rechazados por el Salón oficial, un grupo de artistas organizó su propia exposición independiente, un acto revolucionario para la época.",
            "incorrecta": "Fue recibida con burlas e incomprensión, y fue un acto de rebeldía contra la Academia."
        }
    },
    {
        "pregunta": "En la música impresionista, ¿qué elemento tradicional de la armonía se vio más desdibujado?",
        "opciones": [
            "El tempo (la velocidad de la pieza)",
            "La tonalidad y el uso de acordes estables", 
            "El uso de instrumentos de percusión"
        ],
        "respuesta_correcta": 1,
        "explicacion": {
            "correcta": "Compositores como Debussy utilizaron escalas modales y acordes con funciones ambiguas para crear un sentido de flotación, rompiendo con la claridad tonal del romanticismo.",
            "incorrecta": "El tempo y la percusión no fueron los elementos más revolucionariamente alterados."
        }
    },
    {
        "pregunta": "¿Qué artista impresionista es famoso por sus representaciones de bailarinas de ballet, ensayos y el mundo del espectáculo, a menudo desde ángulos inusuales?",
        "opciones": [
            "Camille Pissarro",
            "Édouard Manet", 
            "Edgar Degas"
        ],
        "respuesta_correcta": 2,
        "explicacion": {
            "correcta": "Edgar Degas dedicó una gran parte de su obra al ballet, capturando no solo las actuaciones sino también los momentos detrás del escenario con composiciones novedosas.",
            "incorrecta": "Pissarro se centró en paisajes, y Manet en retratos y escenas de café."
        }
    },
    {
        "pregunta": "El postimpresionismo, movimiento que siguió al impresionismo, se caracterizó por:",
        "opciones": [
            "Abandonar por completo el uso del color y la luz",
            "Volver a los estilos y temas del Renacimiento", 
            "Rechazar la mera impresión sensorial para buscar mayor estructura, emoción y simbología"
        ],
        "respuesta_correcta": 2,
        "explicacion": {
            "correcta": "Artistas como Cézanne, Van Gogh y Gauguin tomaron las lecciones del impresionismo pero las llevaron más allá, buscando un arte con más solidez formal y expresión emocional.",
            "incorrecta": "Por el contrario, el color se volvió más expresivo, y fueron artistas modernos que buscaban nuevos caminos, no un retorno al pasado."
        }
    }
]

def main():
    # Inicializar el estado de la sesión
    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = 0
        st.session_state.respuestas_correctas = 0
        st.session_state.respondida = False
        st.session_state.respuesta_usuario = None
        st.session_state.quiz_completado = False

    # Título principal
    st.title("🎨 Evaluación: Movimiento Impresionista")
    st.markdown("---")

    # Verificar si el quiz está completado
    if st.session_state.quiz_completado:
        mostrar_resultados_finales()
        return

    # Mostrar progreso
    progreso = st.session_state.pregunta_actual / len(preguntas)
    st.progress(progreso)
    st.write(f"Pregunta {st.session_state.pregunta_actual + 1} de {len(preguntas)}")

    # Obtener pregunta actual
    pregunta = preguntas[st.session_state.pregunta_actual]

    # Mostrar pregunta
    st.subheader(f"Pregunta {st.session_state.pregunta_actual + 1}")
    st.write(pregunta["pregunta"])

    # Mostrar opciones de respuesta
    if not st.session_state.respondida:
        respuesta = st.radio(
            "Selecciona tu respuesta:",
            pregunta["opciones"],
            key=f"pregunta_{st.session_state.pregunta_actual}"
        )
        
        if st.button("Enviar respuesta"):
            st.session_state.respondida = True
            st.session_state.respuesta_usuario = pregunta["opciones"].index(respuesta)
            if st.session_state.respuesta_usuario == pregunta["respuesta_correcta"]:
                st.session_state.respuestas_correctas += 1
            st.rerun()

    # Mostrar retroalimentación si ya se respondió
    if st.session_state.respondida:
        mostrar_retroalimentacion(pregunta)
        
        # Botón para siguiente pregunta
        if st.session_state.pregunta_actual < len(preguntas) - 1:
            if st.button("Siguiente pregunta →"):
                st.session_state.pregunta_actual += 1
                st.session_state.respondida = False
                st.session_state.respuesta_usuario = None
                st.rerun()
        else:
            if st.button("Ver resultados finales"):
                st.session_state.quiz_completado = True
                st.rerun()

def mostrar_retroalimentacion(pregunta):
    st.markdown("---")
    st.subheader("📝 Retroalimentación")
    
    respuesta_usuario = st.session_state.respuesta_usuario
    respuesta_correcta = pregunta["respuesta_correcta"]
    
    # Mostrar si la respuesta fue correcta o incorrecta
    if respuesta_usuario == respuesta_correcta:
        st.success("✅ ¡Respuesta correcta!")
        st.write(pregunta["explicacion"]["correcta"])
    else:
        st.error("❌ Respuesta incorrecta")
        st.write(f"**Tu respuesta:** {pregunta['opciones'][respuesta_usuario]}")
        st.write(f"**Respuesta correcta:** {pregunta['opciones'][respuesta_correcta]}")
        st.write(pregunta["explicacion"]["correcta"])
        st.write(pregunta["explicacion"]["incorrecta"])

def mostrar_resultados_finales():
    st.title("🎯 Resultados Finales")
    st.markdown("---")
    
    total_preguntas = len(preguntas)
    correctas = st.session_state.respuestas_correctas
    porcentaje = (correctas / total_preguntas) * 100
    
    # Mostrar puntuación
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Preguntas correctas", f"{correctas}/{total_preguntas}")
    with col2:
        st.metric("Porcentaje", f"{porcentaje:.1f}%")
    with col3:
        st.metric("Calificación", obtener_calificacion(porcentaje))
    
    # Mensaje según el desempeño
    st.markdown("---")
    if porcentaje >= 90:
        st.balloons()
        st.success("""
        🎉 **¡Excelente!** Eres un verdadero experto en impresionismo. 
        Tu conocimiento abarca perfectamente todas las áreas del movimiento.
        """)
    elif porcentaje >= 70:
        st.success("""
        👍 **¡Muy bien!** Tienes un buen conocimiento del impresionismo. 
        Continúa explorando este fascinante movimiento artístico.
        """)
    elif porcentaje >= 50:
        st.warning("""
        📚 **Buen intento.** Tienes conocimientos básicos del impresionismo. 
        Te recomendamos repasar algunos conceptos clave.
        """)
    else:
        st.info("""
        💡 **No te rindas.** El impresionismo es un movimiento complejo. 
        Esta es una oportunidad para aprender más sobre él.
        """)
    
    # Botón para reiniciar
    if st.button("🔄 Intentar de nuevo"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

def obtener_calificacion(porcentaje):
    if porcentaje >= 90:
        return "Sobresaliente"
    elif porcentaje >= 80:
        return "Notable"
    elif porcentaje >= 70:
        return "Bien"
    elif porcentaje >= 60:
        return "Suficiente"
    else:
        return "Insuficiente"

if __name__ == "__main__":
    main()
