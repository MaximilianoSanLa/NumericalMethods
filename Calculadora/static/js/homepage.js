document.addEventListener("DOMContentLoaded", function() {
    const incremental_search_method_form = document.getElementById("incremental_search_method_form");
    const bisection_method_button = document.getElementById("show_bisection_method_form");
    const bisection_method_form = document.getElementById("bisection_method_form");
    const regla_falsa_method_form = document.getElementById("regla_falsa_method_form");
    const graph_function_form = document.getElementById("graph_function_form");
    const newton_method_form = document.getElementById("newton_method_form")
    const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    let tolerance;
    let func;

    // Function that hides all the forms
    function hide_all_forms() {
        bisection_method_form.style.display = "none";
        newton_method_form.style.display = "none";
        graph_function_form.style.display = "none";
        incremental_search_method_form.style.display = "none";
        regla_falsa_method_form.style.display = "none";

    }

    // Display the incremental search method form
    document.getElementById("show_incremental_search_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        incremental_search_method_form.style.display = "block";
    
    });

    // Display the bisection method form
    bisection_method_button.addEventListener("click", function(e){
    e.preventDefault();
    hide_all_forms();
    bisection_method_form.style.display = "block";

    });

    // Display the regla falsa method form
    document.getElementById("show_regla_falsa_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        regla_falsa_method_form.style.display = "block";
    
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

    //Incremental search method
    document.getElementById("incremental_search_method_form").addEventListener("submit", function(e){
        e.preventDefault();
    
        func = document.getElementById("function_incremental_search_method").value;
        let x0 = parseFloat(document.getElementById("x0_incremental_search_method").value);
        let delta = parseFloat(document.getElementById("delta_incremental_search_method").value);
        N = parseInt(document.getElementById("N_incremental_search_method").value);
    
        if (N < 0) {
        alert("N can not be less than 0")
        }
    
    
        fetch("/Calculator/incremental_search_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                function: func,
                x0: x0,
                delta: delta,
                N: N
            })
        })
        .then(response => response.json())
        .then(data => {
            let result_container = document.getElementById("result");
            result_container.innerHTML = "";
            if (data.result == "empty table") {
            let message = document.createElement("h2");
            message.innerHTML = "There is no root in any of the intervals";
            result_container.appendChild(message);
            }
            else {
                const existing_table = document.getElementById("iterations_table");
                if (existing_table) {
                    existing_table.remove();
                }
                create_table(data.result, "incremental_search");
            }
            document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
            incremental_search_method_form.style.display = "none";
            
        })
        .catch(error => console.log("Error: ", error));
    });

    //Bisection method
    document.getElementById("bisection_method_form").addEventListener("submit", function(e){
    e.preventDefault();

    let a = parseFloat(document.getElementById("a_bisection_method").value);
    let b = parseFloat(document.getElementById("b_bisection_method").value);
    tolerance = parseFloat(document.getElementById
    ("tolerance_bisection_method").value);
    func = document.getElementById("function_bisection_method").value;
    N = parseInt(document.getElementById("N_bisection_method").value);

    if (tolerance < 0 || N < 0) {
        alert("Tolerance or N can not be less than 0")
        return;
    }


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
            N: N
        })
    })
    .then(response => response.json())
    .then(data => {
            let result_container = document.getElementById("result");
            result_container.innerHTML = "";
            if (data.type == "no root in the interval") {
                alert("Error: No root in the given interval. Please choose a different interval.");
                document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
            }
            else if (data.type == "invalid function") {
                alert("Error: Invalid function. Please verify.");
            }
            else if (data.type == "no convernge") {
                let message = document.createElement("h2");
                message.innerHTML = "No convergence. Maximun iterations were reached. Plese insert a new interval, adjust tolerance or verify function."
                result_container.appendChild(message);
                const existing_table = document.getElementById("iterations_table");
                if (existing_table) {
                    existing_table.remove();
                }
                create_table(data.result, "bisection");
                document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
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
                document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                bisection_method_form.style.display = "none";
            }
    })
    .catch(error => console.log("Error: ", error));
    });

    //Regla falsa method
    document.getElementById("regla_falsa_method_form").addEventListener("submit", function(e){
        e.preventDefault();
    
        func = document.getElementById("function_regla_falsa_form").value;
        let a = parseFloat(document.getElementById("a_regla_falsa_form_method").value);
        let b = parseFloat(document.getElementById("b_regla_falsa_form_method").value);
        tolerance = parseFloat(document.getElementById
        ("tolerance_regla_falsa_method").value);
        N = parseInt(document.getElementById("N_regla_falsa_method").value);
    
        if (tolerance < 0 || N < 0) {
            alert("Tolerance or N can not be less than 0")
            return;
        }
    
    
        fetch("/Calculator/regla_falsa_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                function: func,
                a: a,
                b: b,
                tolerance: tolerance,
                N: N
            })
        })
        .then(response => response.json())
        .then(data => {
                let result_container = document.getElementById("result");
                result_container.innerHTML = "";
                if (data.type == "no root in the interval") {
                    alert("Error: No root in the given interval. Please choose a different interval.");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                }
                else if (data.type == "invalid function") {
                    alert("Error: Invalid function. Please verify.");
                }
                else if (data.type == "no convernge") {
                    let message = document.createElement("h2");
                    message.innerHTML = "No convergence. Maximun iterations were reached. Plese insert a new interval, adjust tolerance or verify function."
                    result_container.appendChild(message);
                    const existing_table = document.getElementById("iterations_table");
                    if (existing_table) {
                        existing_table.remove();
                    }
                    create_table(data.result, "regla_falsa");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
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
                    create_table(data.result.table, "regla_falsa");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                    regla_falsa_method_form.style.display = "none";
                }
        })
        .catch(error => console.log("Error: ", error));
        });

    //Show graph
    graph_function_form.addEventListener("submit", function(e){
        e.preventDefault();

        let func = document.getElementById("function_graph_function").value;

        fetch("/Calculator/graph_function/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                function: func
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
    
        fetch("/Calculator/newton_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                x0: x0,
                tolerance: tolerance,
                function: func
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
    
        // Cambios aquí
        if (method === "bisection") {
            const headers = ["i", "a", "b", "c", "f(a)", "f(c)", "Error absoluto"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        
        } 
        else if (method === "regla_falsa") {
            const headers = ["i", "a", "xm", "b", "f(xm)", "Error absoluto"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        }
        else if (method === "newton") {
            const headers = ["i", "xi", "f(xi)", "f'(xi)", "Error absoluto"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } else if (method === "incremental_search") {
            // Para "incremental_search", no agregamos encabezados
            // Se omite la creación de la fila de encabezados
            // Solo se añade un tbody para la tabla de una sola columna
            const tbody = document.createElement('tbody');
            
            data.forEach(item => {
                const new_row = document.createElement('tr');
                const new_cel = document.createElement('td');
                new_cel.textContent = item; // Mostrar solo el valor de item
                new_row.appendChild(new_cel);
                tbody.appendChild(new_row);
            });
            
            table.appendChild(tbody);
            const result_container = document.getElementById("table");
            result_container.appendChild(table);
            return; // Salir de la función después de manejar este caso
        }
    
        // Añadir los encabezados al thead si no es incremental_search
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
    
});

