
// referencia al elemento de la consola
const consolaEnPagina = document.getElementById('consola-js');

// referencia a la funcion original de console.log
const logOriginal = console.log;

// sobrescribir console.log con la funcion
console.log = function (...args) {
    // 1. llamado a la función original para que siga imprimiendo en la consola del navegador
    logOriginal.apply(console, args);

    // 2. mensaje para nuestra consola en el body
    // JSON.stringify para manejar objetos y arrays de forma legible
    const mensaje = args.map(arg =>
        typeof arg === 'object' ? JSON.stringify(arg, null, 2) : arg
    ).join(' ');

    // 3. agrega el nuevo mensaje al contenido del div
    consolaEnPagina.innerHTML += mensaje + '\n';
};

// --- USO DE CONSOLA ---
// el contenido de muestra en ambas consolas
