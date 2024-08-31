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
        let a_result = document.createElement("p");
        let b_result = document.createElement("p");
        let iter_result = document.createElement("p");
        let error_result = document.createElement("p");
        a_result.innerHTML = `a: ${data.result.a}`;
        b_result.innerHTML = `b: ${data.result.b}`;
        iter_result.innerHTML = `Iterations: ${data.result.iter}`;
        error_result.innerHTML = `Error: ${data.result.error}`;

        let resultContainer = document.getElementById("result");
        resultContainer.innerHTML = "";
        resultContainer.appendChild(a_result);
        resultContainer.appendChild(b_result);
        resultContainer.appendChild(iter_result);
        resultContainer.appendChild(error_result);

        // Muestra la gráfica
        document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
    })
    .catch(error => console.log("Error: ", error));

    bisection_method_form.style.display = "none";

 });