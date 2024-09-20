const bisection_method_button = document.getElementById("show_bisection_method_form");
const bisection_method_form = document.getElementById("bisection_method_form");

bisection_method_button.addEventListener("click", function(e){
   e.preventDefault();
   bisection_method_form.style.display = "block";
});

//Bisection method
document.getElementById("bisection_method_form").addEventListener("submit", function(e){
   e.preventDefault();

   let a = document.getElementById("a").value;
   let b = document.getElementById("b").value;
   let tolerance = document.getElementById("tolerance").value;
   let func = document.getElementById("function").value;
   let variable = document.getElementById("variable").value;
   const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

   fetch("/Calculator/fun_bisection/", {
       method: "POST",
       headers: {
           "Content-Type": "application/json",
           'X-CSRFToken': csrftoken
       },
       body: JSON.stringify({
           a: a,
           b: b,
           tolerance: tolerance,
           function: func,
           variable: variable
       })
   })
   .then(response => response.json())
   .then(data => {
       console.log(data)
       let root_result = document.createElement("p");
       let iter_result = document.createElement("p");
       let error_result = document.createElement("p");
       root_result.innerHTML = `Root: ${data.result.root_result}`;
       iter_result.innerHTML = `Iterations: ${data.result.iter}`;
       error_result.innerHTML = `Error: ${data.result.error}`;

       let resultContainer = document.getElementById("result");
       resultContainer.innerHTML = "";
       resultContainer.appendChild(root_result);
       resultContainer.appendChild(iter_result);
       resultContainer.appendChild(error_result);

       // Muestra la gráfica
       document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;

       const table = data.result.table
       table.forEach(fila =>{
        agregar_fila(fila)
       })
       document.getElementById("tabla-resultados").style.display = "block";
   })
   .catch(error => console.log("Error: ", error));

   bisection_method_form.style.display = "none";

});

function agregar_fila(fila) {
    const tabla = document.getElementById('tabla-resultados').getElementsByTagName('tbody')[0];
    const nuevaFila = tabla.insertRow();

    // Añadir celdas
    for (const key in fila) {
        const nuevaCelda = nuevaFila.insertCell();
        nuevaCelda.textContent = fila[key];
    }
}