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

        document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
        const existing_table = document.getElementById("iterations_table");
        if (existing_table) {
            existing_table.remove();
        }
        create_table(data.result.table, "bisection");
   })
   .catch(error => console.log("Error: ", error));

   bisection_method_form.style.display = "none";

});

document.getElementById("graph_function").addEventListener("click", function(e){
    e.preventDefault();
    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;

})
function create_table(data, method) {
    const table = document.createElement('table');
    table.classList.add('table', 'table-bordered', 'table-striped', 'table-hover');
    table.id = 'iterations_table'; 

    const thead = document.createElement('thead');
    const headers_row = document.createElement('tr');
    if(method == "bisection"){
            const headers = ["a", "b", "c", "f(a)", "f(c)", "Error absoluto"] 
            headers.forEach(header => {
            const header_cel = document.createElement('th');
            header_cel.textContent = header;
            headers_row.appendChild(header_cel);
        });
    }
    thead.appendChild(headers_row);
    table.appendChild(thead);

    const tbody = document.createElement('tbody');
    
    data.forEach(row => {
        const new_row = document.createElement('tr');
        for (const key in row) {
            const new_cel = document.createElement('td');
            new_cel.textContent = row[key];
            new_row.appendChild(new_cel);
        }
        tbody.appendChild(new_row);
    });

    table.appendChild(tbody);
    const result_container = document.getElementById("table");
    result_container.appendChild(table);
}


