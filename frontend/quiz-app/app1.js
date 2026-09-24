
// --- VARIABLES DE ESTADO ---
let score = 0;             // Aciertos
let totalQuestions = 0;     // Total de intentos
let gameActive = true;     // "Interruptor" del juego
let currentQuestion;

// Elementos del DOM
const questionDiv = document.querySelector('.question');
const buttons = document.querySelectorAll('.answer-button');
const resultDiv = document.querySelector('.result');
const mainContainer = document.querySelector('main');

// Funciones de ayuda
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getOperator() {
    const signs = ['+', '-', 'x', '/'];
    return signs[randomInt(0, 3)];
}

// --- CLASE QUESTION ---
class Question {
    constructor() {
        let numberOne = randomInt(1, 30);
        let numberTwo = randomInt(1, 30);
        let operator = getOperator();

        this.questionName = `${numberOne} ${operator} ${numberTwo}`;

        // Lógica para establecere la respuesta correcta
        if (operator === '+') { this.correctAnswer = numberOne + numberTwo; }
        else if (operator === '-') { this.correctAnswer = numberOne - numberTwo; }
        else if (operator === 'x') { this.correctAnswer = numberOne * numberTwo; }
        else if (operator === '/') { this.correctAnswer = Math.round(numberOne / numberTwo); }

        // Opciones con respuestas diferentes
        const choices = [this.correctAnswer];
        while (choices.length < 5) {
            let wrongAnswer = randomInt(this.correctAnswer - 10, this.correctAnswer + 10);

            if (!choices.includes(wrongAnswer)){
                choices.push(wrongAnswer);
            }
        }

        this.answersArray = choices;
        this.shuffleArray(this.answersArray);
    }

    // Establecer la pregunta
    displayQuestion() {
        questionDiv.textContent = this.questionName;
        for (let i = 0; i < this.answersArray.length; i++) {
            buttons[i].textContent = this.answersArray[i];
            // Reiniciamos el color del botón
            buttons[i].style.backgroundColor = '#ffca28';
        }
    }

    // Mezclar el array
    shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = randomInt(0, i);
            [array[i], array[j]] = [array[j], array[i]];
        }
    }
}


// --- LOGICA DEL JUEGO ---

// 1. Iniciar primera pregunta
currentQuestion = new Question();
currentQuestion.displayQuestion();

// 2. Temporizador: Se activa a los 15 segundos
setTimeout(() => {
    gameActive = false; // Desactivamos el juego
    showResults();     // Mostramos resultados
}, 15000);

// 3. Evento de clic en botones
buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        if (!gameActive) return; // Si el juego no está activo, ignorar clics
        
        totalQuestions++; // Si el juego esta activo inicia el conteo
        
        const correct = (Number(btn.textContent) === currentQuestion.correctAnswer);
        
        if (correct) {
            console.log('✅ Correcto!');
            score++;
            // TODO: ANIMACION - Implementar feedback visual de acierto.
            // Ejemplo de guía: Cambiar de forma directa el color del botón presionado ('btn') a verde.
            
        } else {
            console.log('❌ Incorrecto!');
            // TODO: ANIMACION - Implementar feedback visual de error.
            // Ejemplo de guía: Cambiar de forma directa el color del botón presionado ('btn') a rojo.
        }

        // Generamos una nueva pregunta si el juego sigue activo
        setTimeout(() => {
            // Validamos que la pantalla no se haya ocultado por el temporizador general durante la espera
            const isGameOver = (mainContainer.style.display === 'none');
            
            if (!isGameOver) {
                currentQuestion = new Question();
                currentQuestion.displayQuestion();
            }
        }, 300);
    });
});

// 4. Mostrar Resultados Finales
function showResults() {
    mainContainer.style.display = 'none';

    // TODO: ESTADISTICAS - Calcular el porcentaje de precisión del alumno.
    // Fórmula recomendada: (Aciertos / Intentos) * 100. Recuerda redondear usando Math.round() 
    // y validar con un condicional que 'questionCount' sea mayor a 0 para evitar divisiones por cero.
    let accuracy;

    // TODO: RESULTS - Estructurar el nuevo contenido dinámico usando Template Literals (``).
    // Debes renderizar dentro del HTML las variables de estado finales ('score', 'questionCount' y tu variable 'accuracy').
    resultDiv.innerHTML = `
        <div class="final-results">
        </div>
    `;
}
