const bisection_method_button = document.getElementById("show_bisection_method_form");
const bisection_method_form = document.getElementById("bisection_method_form");
const graph_function_form = document.getElementById("graph_function_form");
const newton_method_form = document.getElementById("newton_method_form")
const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
let tolerance;
let variable;
let func;

// Function that hides all the forms
function hide_all_forms() {
    bisection_method_form.style.display = "none";
    newton_method_form.style.display = "none";
    graph_function_form.style.display = "none";
}

// Display the bisection method form
bisection_method_button.addEventListener("click", function(e){
   e.preventDefault();
   hide_all_forms();
   bisection_method_form.style.display = "block";

});

// Display the show graph form 
document.getElementById("graph_function").addEventListener("click", function(e) {
    e.preventDefault();
    hide_all_forms();
    graph_function_form.style.display = "block";
});

// Display the Newton method form
document.getElementById("show_newton_method_form").addEventListener("click", function(e) {
    e.preventDefault();
    hide_all_forms();
    newton_method_form.style.display = "block";
});

//Bisection method
document.getElementById("bisection_method_form").addEventListener("submit", function(e){
   e.preventDefault();

   let a = document.getElementById("a_bisection_method").value;
   let b = document.getElementById("b_bisection_method").value;
   tolerance = document.getElementById("tolerance_bisection_method").value;
   func = document.getElementById("function_bisection_method").value;
   variable = document.getElementById("variable_bisection_method").value;

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
        let result_container = document.getElementById("result");
        result_container.innerHTML = "";
        if (data.type == 1) {
            let result = document.createElement("p");
            result.innerHTML = data.result;
            result_container.appendChild(result);
        }
        else {
            let root_result = document.createElement("p");
            let iter_result = document.createElement("p");
            let error_result = document.createElement("p");

            root_result.innerHTML = `Root: ${data.result.root_result}`;
            iter_result.innerHTML = `Iterations: ${data.result.iter}`;
            error_result.innerHTML = `Error: ${data.result.error}`;
            result_container.appendChild(root_result);
            result_container.appendChild(iter_result);
            result_container.appendChild(error_result);
            const existing_table = document.getElementById("iterations_table");
            if (existing_table) {
                existing_table.remove();
            }
            create_table(data.result.table, "bisection");
        }
        document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
   })
   .catch(error => console.log("Error: ", error));

   bisection_method_form.style.display = "none";

});

//Show graph
graph_function_form.addEventListener("submit", function(e){
    e.preventDefault();

    let func = document.getElementById("function_graph_function").value;
    variable =document.getElementById("variable_bisection_method").value

    fetch("/Calculator/graph_function/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            function: func,
            variable: variable
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.image}" />`;
    })
    .catch(error => console.log("Error: ", error))
    graph_function_form.style.display = "none";
});

//Newton method
document.getElementById("newton_method_form").addEventListener("submit", function(e){
    e.preventDefault();
 
    let x0 = document.getElementById("x0_newton_method").value;
    tolerance = document.getElementById("tolerance_newton_method").value;
    func = document.getElementById("function_newton_method").value;
    variable = document.getElementById("variable_newton_method").value;
 
    fetch("/Calculator/newton_method/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            x0: x0,
            tolerance: tolerance,
            function: func,
            variable: variable
        })
    })
    .then(response => response.json())
    .then(data => {
         let result_container = document.getElementById("result");
         result_container.innerHTML = "";
         if (data.type == 1 || data.type == 3) {
             let result = document.createElement("p");
             result.innerHTML = data.result;
             result_container.appendChild(result);
         }
         else {
             let root_result = document.createElement("p");
             let iter_result = document.createElement("p");
             let error_result = document.createElement("p");
 
             root_result.innerHTML = `Root: ${data.result.root_result}`;
             iter_result.innerHTML = `Iterations: ${data.result.iter}`;
             error_result.innerHTML = `Error: ${data.result.error}`;
             result_container.appendChild(root_result);
             result_container.appendChild(iter_result);
             result_container.appendChild(error_result);
             const existing_table = document.getElementById("iterations_table");
             if (existing_table) {
                 existing_table.remove();
             }
             create_table(data.result.table, "newton");
         }
         document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
    })
    .catch(error => console.log("Error: ", error));
 
    newton_method_form.style.display = "none";
 
 });

// Function that creates tables
function create_table(data, method) {
    const table = document.createElement('table');
    table.classList.add('table', 'table-bordered', 'table-striped', 'table-hover');
    table.id = 'iterations_table'; 

    const thead = document.createElement('thead');
    const headers_row = document.createElement('tr');
    if(method == "bisection"){
            const headers = ["i", "a", "b", "c", "f(a)", "f(c)", "Error absoluto"] 
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
    }
    else if (method == "newton") {
        const headers = ["i", "xi", "f(xi)", "f'(xi)", "Error absoluto"] 
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


