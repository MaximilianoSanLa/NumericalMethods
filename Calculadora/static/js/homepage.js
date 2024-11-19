document.addEventListener("DOMContentLoaded", function() {
    const incremental_search_method_form = document.getElementById("incremental_search_method_form");
    const bisection_method_button = document.getElementById("show_bisection_method_form");
    const bisection_method_form = document.getElementById("bisection_method_form");
    const regla_falsa_method_form = document.getElementById("regla_falsa_method_form");
    const punto_fijo_method_form = document.getElementById("punto_fijo_method_form")
    const graph_function_form = document.getElementById("graph_function_form");
    const newton_method_form = document.getElementById("newton_method_form")
    const secant_method_form = document.getElementById("secant_method_form")
    const multiple_roots_method_form = document.getElementById("multiple_roots_method_form")
    const gaussian_simple_elimination_method_form = document.getElementById("gaussian_simple_elimination_method_form");
    const GE_partial_pivoting_method_form = document.getElementById("GE_partial_pivoting_method_form");
    const GE_total_pivoting_method_form = document.getElementById("GE_total_pivoting_method_form");
    const LU_simple_method_form = document.getElementById("LU_simple_method_form");
    const LU_partial_method_form = document.getElementById("LU_partial_method_form");
    const crout_method_form = document.getElementById("crout_method_form");
    const doolittle_method_form = document.getElementById("doolittle_method_form");
    const cholesky_method_form = document.getElementById("cholesky_method_form");
    const jacobi_method_form = document.getElementById("jacobi_method_form");
    const seidel_method_form = document.getElementById("seidel_method_form");
    const SOR_method_form = document.getElementById("SOR_method_form");
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
        punto_fijo_method_form.style.display = "none";
        secant_method_form.style.display = "none";
        multiple_roots_method_form.style.display = "none";
        gaussian_simple_elimination_method_form.style.display = "none";
        GE_partial_pivoting_method_form.style.display = "none";
        GE_total_pivoting_method_form.style.display = "none";
        LU_simple_method_form.style.display = "none";
        LU_partial_method_form.style.display = "none";
        crout_method_form.style.display = "none";
        doolittle_method_form.style.display = "none";
        cholesky_method_form.style.display = "none";
        jacobi_method_form.style.display = "none";
        seidel_method_form.style.display = "none";
        SOR_method_form.style.display = "none";
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

    // Display the punto fijo method form
    document.getElementById("show_punto_fijo_method_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        punto_fijo_method_form.style.display = "block";
    
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

    // Display secant method form
    document.getElementById("show_secant_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        secant_method_form.style.display = "block";
    
    });

    // Display multiple roots method form
    document.getElementById("show_multiple_roots_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        multiple_roots_method_form.style.display = "block";
    
    });

    // Display gaussian simple elimination method form
    document.getElementById("show_gaussian_simple_elimination_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        gaussian_simple_elimination_method_form.style.display = "block";
    
    });

    // Display GE partial pivoting method form
    document.getElementById("show_GE_partial_pivoting_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        GE_partial_pivoting_method_form.style.display = "block";
    
    });

    // Display GE total pivoting method form
    document.getElementById("show_GE_total_pivoting_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        GE_total_pivoting_method_form.style.display = "block";
    
    });

    // Display LU simple method form
    document.getElementById("show_LU_simple_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        LU_simple_method_form.style.display = "block";
    });

    // Display LU partial method form
    document.getElementById("show_LU_partial_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        LU_partial_method_form.style.display = "block";
    });

    // Display crout method form
    document.getElementById("show_crout_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        crout_method_form.style.display = "block";
    });

    // Display doolittle method form
    document.getElementById("show_doolittle_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        doolittle_method_form.style.display = "block";
    });

    // Display cholesky method form
    document.getElementById("show_cholesky_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        cholesky_method_form.style.display = "block";
    });

    // Display jacobi method form
    document.getElementById("show_jacobi_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        jacobi_method_form.style.display = "block";
    });

    // Display Gauss-Seidel method form
    document.getElementById("show_seidel_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        seidel_method_form.style.display = "block";
    });

    // Display SOR method form
    document.getElementById("show_SOR_method_form").addEventListener("click", function(e){
        e.preventDefault();
        hide_all_forms();
        SOR_method_form.style.display = "block";
    });

    //Incremental search method
    document.getElementById("incremental_search_method_form").addEventListener("submit", function(e){
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        e.preventDefault();
        updateMethodTitle("Incremental Search Method");
        func = document.getElementById("function_incremental_search_method").value;
        let x0 = parseFloat(document.getElementById("x0_incremental_search_method").value);
        let delta = parseFloat(document.getElementById("delta_incremental_search_method").value);
        N = parseInt(document.getElementById("N_incremental_search_method").value);
    
        if (N < 0) {
            alert("N can not be less than 0")
            return 
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
            else if (data.type == 2) {
                alert("Error: Invalid function. Please verify.");
            }
            else {
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
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
    const existing_graph = document.getElementById("graph");
    if (existing_graph) {
        existing_graph.innerHTML="";
    }
    updateMethodTitle("Bisection Method");
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
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
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
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
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
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Regla Falsa Method");
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
                    const existing_table = document.getElementById("table");
                    if (existing_table) {
                        existing_table.innerHTML="";
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
                    const existing_table = document.getElementById("table");
                    if (existing_table) {
                        existing_table.innerHTML="";
                    }
                    create_table(data.result.table, "regla_falsa");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                    regla_falsa_method_form.style.display = "none";
                }
        })
        .catch(error => console.log("Error: ", error));
        });
    
    // Punto fijo method
    document.getElementById("punto_fijo_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Punto Fijo Method");
        let f = document.getElementById("f_punto_fijo_method").value;
        let g = document.getElementById("g_punto_fijo_method").value;
        let x0 = parseFloat(document.getElementById("x0_punto_fijo_method").value);
        tolerance = parseFloat(document.getElementById
        ("tolerance_punto_fijo_method").value);
        N = parseInt(document.getElementById("N_punto_fijo_method").value);
    
        if (tolerance < 0 || N < 0) {
            alert("Tolerance or N can not be less than 0")
            return;
        }
        fetch("/Calculator/punto_fijo_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                f: f,
                g: g,
                x0: x0,
                tolerance: tolerance,
                N: N
            })
        })
        .then(response => response.json())
        .then(data => {
                let result_container = document.getElementById("result");
                result_container.innerHTML = "";
                if (data.type == 1) {
                    alert("Error: Invalid function. Please verify.");
                }
                else if (data.type == 2) {
                    let message = document.createElement("h2");
                    message.innerHTML = "No convergence. Maximun iterations were reached. Plese insert a new interval, adjust tolerance or verify function."
                    result_container.appendChild(message);
                    const existing_table = document.getElementById("table");
                    if (existing_table) {
                        existing_table.innerHTML="";
                    }
                    create_table(data.table, "punto_fijo");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                }
                else {
                    let iter_result = document.createElement("p");
                    let root_result = document.createElement("p");
                    let g_result = document.createElement("p");
                    let f_result = document.createElement("p");
                    let error_result = document.createElement("p");
    
                    iter_result.innerHTML = `Iterations: ${data.result.iterations}`;
                    root_result.innerHTML = `xi: ${data.result.xi}`;
                    g_result.innerHTML = `g(xi): ${data.result.gxi}`;
                    f_result.innerHTML = `g(xi): ${data.result.fxi}`;
                    error_result.innerHTML = `Error: ${data.result.error}`;
                    result_container.appendChild(iter_result);
                    result_container.appendChild(root_result);
                    result_container.appendChild(g_result);
                    result_container.appendChild(f_result);
                    result_container.appendChild(error_result);
                    const existing_table = document.getElementById("table");
                    if (existing_table) {
                        existing_table.innerHTML="";
                    }
                    create_table(data.result.table, "punto_fijo");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                    punto_fijo_method_form.style.display = "none";
                }
        })
        .catch(error => console.log("Error: ", error));
    });

    //Show graph
    graph_function_form.addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        let func = document.getElementById("function_graph_function").value;
        const existing_table = document.getElementById("table");
        if (existing_table) {
            existing_table.innerHTML="";
        }

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
    
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
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
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.result.table, "newton");
            }
            document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
        })
        .catch(error => console.log("Error: ", error));
    
        newton_method_form.style.display = "none";
    
    });

    // Secant method
    document.getElementById("secant_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Secant Method");
        func = document.getElementById("function_secant_method").value;
        let x0 = parseFloat(document.getElementById("x0_secant_method").value);
        let x1 = parseFloat(document.getElementById("x1_secant_method").value);
        tolerance = parseFloat(document.getElementById
        ("tolerance_secant_method").value);
        N = parseInt(document.getElementById("N_secant_method").value);
    
        if (tolerance < 0 || N < 0) {
            alert("Tolerance or N can not be less than 0")
            return;
        }
        fetch("/Calculator/secant_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                function: func,
                x0: x0,
                x1: x1,
                tolerance: tolerance,
                N: N
            })
        })
        .then(response => response.json())
        .then(data => {
                let result_container = document.getElementById("result");
                result_container.innerHTML = "";
                if (data.type == 1) {
                    alert("Error: Dividing by 0. Please verify the function.");
                }
                else if (data.type == 2) {
                    let message = document.createElement("h2");
                    message.innerHTML = "No convergence. Maximun iterations were reached. Plese insert a new interval, adjust tolerance or verify function."
                    result_container.appendChild(message);
                    const existing_table = document.getElementById("table");
                    if (existing_table) {
                        existing_table.innerHTML="";
                    }
                    create_table(data.table, "secant");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                }
                else if (data.type == 3) {
                    alert("Error: Invalid function. Please verify.");
                }
                else {
                    let iter_result = document.createElement("p");
                    let root_result = document.createElement("p");
                    let function_result = document.createElement("p");
                    let error_result = document.createElement("p");
    
                    iter_result.innerHTML = `Iterations: ${data.result.iterations}`;
                    root_result.innerHTML = `xi: ${data.result.xi}`;
                    function_result.innerHTML = `f(xi): ${data.result.fxi}`;
                    error_result.innerHTML = `Error: ${data.result.error}`;
                    result_container.appendChild(iter_result);
                    result_container.appendChild(root_result);
                    result_container.appendChild(function_result);
                    result_container.appendChild(error_result);
                    const existing_table = document.getElementById("table");
                    if (existing_table) {
                        existing_table.innerHTML="";
                    }
                    create_table(data.result.table, "secant");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                    secant_method_form.style.display = "none";
                }
        })
        .catch(error => console.log("Error: ", error));
    });

    // Multiple roots method
    document.getElementById("multiple_roots_method_form").addEventListener("submit", function(e){
        e.preventDefault();
    
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Multiple Roots Method");
        func = document.getElementById("function_mulitple_roots_method").value;
        let x0 = parseFloat(document.getElementById("x0_multiple_roots_method").value);
        tolerance = parseFloat(document.getElementById
        ("tolerance_multiple_roots_method").value);
        N = parseInt(document.getElementById("N_multiple_roots_method").value);
    
        if (tolerance < 0 || N < 0) {
            alert("Tolerance or N can not be less than 0")
            return;
        }
        fetch("/Calculator/multiple_roots_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                function: func,
                x0: x0,
                tolerance: tolerance,
                N: N
            })
        })
        .then(response => response.json())
        .then(data => {
                let result_container = document.getElementById("result");
                result_container.innerHTML = "";
                if (data.type == 1) {
                    let message = document.createElement("h2");
                    message.innerHTML = "No convergence. Maximun iterations were reached. Plese insert a new interval, adjust tolerance or verify function."
                    result_container.appendChild(message);
                    const existing_table = document.getElementById("table");
                    if (existing_table) {
                        existing_table.innerHTML="";
                    }
                    create_table(data.table, "multiple_roots");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                }
                else if (data.type == 2) {
                    alert("Error: Invalid function. Please verify.");
                }
                else {
                    let iter_result = document.createElement("p");
                    let root_result = document.createElement("p");
                    let function_result = document.createElement("p");
                    let error_result = document.createElement("p");
    
                    iter_result.innerHTML = `Iterations: ${data.result.iterations}`;
                    root_result.innerHTML = `xi: ${data.result.xi}`;
                    function_result.innerHTML = `h(xi): ${data.result.fxi}`;
                    error_result.innerHTML = `Error: ${data.result.error}`;
                    result_container.appendChild(iter_result);
                    result_container.appendChild(root_result);
                    result_container.appendChild(function_result);
                    result_container.appendChild(error_result);
                    const existing_table = document.getElementById("table");
                    if (existing_table) {
                        existing_table.innerHTML="";
                    }
                    create_table(data.result.table, "multiple_roots");
                    document.getElementById("graph").innerHTML = `<img src="data:image/png;base64, ${data.buffer}" />`;
                    multiple_roots_method_form.style.display = "none";
                }
        })
        .catch(error => console.log("Error: ", error));
    });

    // Gaussian simple elimination method
    document.getElementById("gaussian_simple_elimination_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Gaussian Simple Elimination Method");
    
        A = validateMatrix(document.getElementById("A_gaussian_simple_elimination_method").value);
        b = validateVectorB(A, document.getElementById("b_gaussian_simple_elimination_method").value);
        if (!A)
        {
            return;
        }
        if (!b)
        {
            return;
        }
        
        fetch("/Calculator/gausspl_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                A: A, 
                b: b
            })
        })
        .then(response => response.json())
        .then(data => {
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.result, "gaussian_simple_elimination");
                gaussian_simple_elimination_method_form.style.display = "none";
        })
        .catch(error => console.log("Error: ", error));
    });

    // LU_simple method
    document.getElementById("LU_simple_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("LU Simple Method");
        
        A = validateMatrix(document.getElementById("A_LU_simple_method").value);
        b = validateVectorB(A, document.getElementById("b_LU_simple_method").value);
        if (!A)
        {
            return;
        }
        if (!b)
        {
            return;
        }
        
        fetch("/Calculator/LU_simple_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                A: A, 
                b: b
            })
        })
        .then(response => response.json())
        .then(data => {
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.x, "LU_simple");
                create_table(data.L, "Matrix L");
                create_table(data.U, "Matrix U");
                
                LU_simple_method_form.style.display = "none"
        })
        .catch(error => console.log("Error: ", error));
    });


    document.getElementById("LU_partial_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("LU Partial Method");
        
        A = validateMatrix(document.getElementById("A_LU_partial_method").value);
        b = validateVectorB(A, document.getElementById("b_LU_partial_method").value);
        if (!A)
        {
            return;
        }
        if (!b)
        {
            return;
        }
        
        fetch("/Calculator/LU_partial_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                A: A, 
                b: b
            })
        })
        .then(response => response.json())
        .then(data => {
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.x, "LU_partial");
                create_table(data.L, "Matrix L");
                create_table(data.U, "Matrix U");
                create_table(data.P, "Matrix P");
                
                LU_partial_method_form.style.display = "none"
        })
        .catch(error => console.log("Error: ", error));
    });

    // Crout method
    document.getElementById("crout_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Crout Method");
        
        A = validateMatrix(document.getElementById("A_crout_method").value);
        b = validateVectorB(A, document.getElementById("b_crout_method").value);
        if (!A)
        {
            return;
        }
        if (!b)
        {
            return;
        }
        
        fetch("/Calculator/Crout_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                A: A, 
                b: b
            })
        })
        .then(response => response.json())
        .then(data => {
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.x, "LU_partial");
                create_table(data.L, "Matrix L");
                create_table(data.U, "Matrix U");
                
                crout_method_form.style.display = "none"
        })
        .catch(error => console.log("Error: ", error));
    });

    // Doolittle method
    document.getElementById("doolittle_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Doolittle Method");
        
        A = validateMatrix(document.getElementById("A_doolittle_method").value);
        b = validateVectorB(A, document.getElementById("b_doolittle_method").value);
        if (!A)
        {
            return;
        }
        if (!b)
        {
            return;
        }
        
        fetch("/Calculator/Doolittle_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                A: A, 
                b: b
            })
        })
        .then(response => response.json())
        .then(data => {
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.x, "LU_partial");
                create_table(data.L, "Matrix L");
                create_table(data.U, "Matrix U");
                
                doolittle_method_form.style.display = "none"
        })
        .catch(error => console.log("Error: ", error));
    });

    // Cholesky method
    document.getElementById("cholesky_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Cholesky Method");
        
        A = validateMatrix(document.getElementById("A_cholesky_method").value);
        b = validateVectorB(A, document.getElementById("b_cholesky_method").value);
        console.log(A,b);
        if (!A)
        {
            return;
        }
        if (!b)
        {
            return;
        }
        
        fetch("/Calculator/Cholesky_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                A: A, 
                b: b
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.x, "LU_partial");
                create_table(data.L, "Matrix L");
                create_table(data.U, "Matrix U");
                
                cholesky_method_form.style.display = "none"
        })
        .catch(error => console.log("Error: ", error));
    });

    // Jacobi method
    document.getElementById("jacobi_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Jacobi Method");
        
        A = validateMatrix(document.getElementById("A_jacobi_method").value);
        b = validateVectorB(A, document.getElementById("b_jacobi_method").value);
        x0 = validateVectorB(A, document.getElementById("x0_jacobi_method").value);
        console.log(A,b);
        if (!A)
        {
            return;
        }
        if (!b)
        {
            return;
        }
        if (!x0)
        {
            return;
        }
        tolerance = parseFloat(document.getElementById
        ("tolerance_jacobi_method").value);
        N = parseInt(document.getElementById("N_jacobi_method").value);

        if (tolerance < 0 || N < 0) {
            alert("Tolerance or N can not be less than 0")
            return;
        }
        
        fetch("/Calculator/Jacobi_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                A: A, 
                b: b,
                x0: x0,
                tolerance: tolerance,
                N: N
            })
        })
        .then(response => response.json())
        .then(data => {
                let result_container = document.getElementById("result");
                result_container.innerHTML = "";
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.T, "Matrix T");
                create_table(data.C, "C");
                let SR_result = document.createElement("p");
    
                SR_result.innerHTML = `Spectral Radius: ${data.spectral_radius}`;
                result_container.appendChild(SR_result);
                create_table(data.table, "jacobi");
                
                jacobi_method_form.style.display = "none"
        })
        .catch(error => console.log("Error: ", error));
    });

    // Gauss-Seidel method
    document.getElementById("seidel_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("Seidel Method");
        
        A = validateMatrix(document.getElementById("A_seidel_method").value);
        b = validateVectorB(A, document.getElementById("b_seidel_method").value);
        x0 = validateVectorB(A, document.getElementById("x0_seidel_method").value);
        console.log(A,b);
        if (!A)
        {
            return;
        }
        if (!b)
        {
            return;
        }
        if (!x0)
        {
            return;
        }
        tolerance = parseFloat(document.getElementById
        ("tolerance_seidel_method").value);
        N = parseInt(document.getElementById("N_seidel_method").value);

        if (tolerance < 0 || N < 0) {
            alert("Tolerance or N can not be less than 0")
            return;
        }
        
        fetch("/Calculator/Gauss_Seidel_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                A: A, 
                b: b,
                x0: x0,
                tolerance: tolerance,
                N: N
            })
        })
        .then(response => response.json())
        .then(data => {
                let result_container = document.getElementById("result");
                result_container.innerHTML = "";
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.T, "Matrix T");
                create_table(data.C, "C");
                let SR_result = document.createElement("p");
    
                SR_result.innerHTML = `Spectral Radius: ${data.spectral_radius}`;
                result_container.appendChild(SR_result);
                create_table(data.table, "seidel");
                
                seidel_method_form.style.display = "none"
        })
        .catch(error => console.log("Error: ", error));
    });

    // SOR method
    document.getElementById("SOR_method_form").addEventListener("submit", function(e){
        e.preventDefault();
        const existing_graph = document.getElementById("graph");
        if (existing_graph) {
            existing_graph.innerHTML="";
        }
        updateMethodTitle("SOR Method");
        
        A = validateMatrix(document.getElementById("A_SOR_method").value);
        b = validateVectorB(A, document.getElementById("b_SOR_method").value);
        x0 = validateVectorB(A, document.getElementById("x0_SOR_method").value);
        if (!A)
        {
            return;
        }
        if (!b)
        {
            return;
        }
        if (!x0)
        {
            return;
        }
        tolerance = parseFloat(document.getElementById
        ("tolerance_SOR_method").value);
        let w = parseFloat(document.getElementById
            ("w_SOR_method").value);
        N = parseInt(document.getElementById("N_SOR_method").value);

        if (tolerance < 0 || N < 0) {
            alert("Tolerance or N can not be less than 0")
            return;
        }
        
        fetch("/Calculator/SOR_method/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                A: A, 
                b: b,
                x0: x0,
                tolerance: tolerance,
                w: w,
                N: N
            })
        })
        .then(response => response.json())
        .then(data => {
                console.log(data);
                let result_container = document.getElementById("result");
                result_container.innerHTML = "";
                const existing_table = document.getElementById("table");
                if (existing_table) {
                    existing_table.innerHTML="";
                }
                create_table(data.T, "Matrix T");
                create_table(data.C, "C");
                let SR_result = document.createElement("p");
    
                SR_result.innerHTML = `Spectral Radius: ${data.spectral_radius}`;
                result_container.appendChild(SR_result);
                create_table(data.table, "SOR");
                
                SOR_method_form.style.display = "none"
        })
        .catch(error => console.log("Error: ", error));
    });

    // Function that creates tables
    function create_table(data, method) {
        const table = document.createElement('table');
        table.classList.add('table', 'table-bordered', 'table-striped', 'table-hover');
        table.id = 'iterations_table'; 

        const caption = document.createElement('caption');
        caption.style.textAlign = "center";
        caption.style.captionSide = "top";
        caption.style.fontWeight = "bold";
        caption.style.marginBottom = "10px";
        caption.style.fontSize = "18px";
    
        const thead = document.createElement('thead');
        const headers_row = document.createElement('tr');
    
        if (method === "bisection") {
            caption.textContent = "Bisection table"; 
            table.appendChild(caption);
            const headers = ["i", "a", "b", "c", "f(a)", "f(c)", "Error absoluto"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } 
        else if (method === "regla_falsa") {
            caption.textContent = "Regla Falsa table"; 
            table.appendChild(caption);
            const headers = ["i", "a", "xm", "b", "f(xm)", "Error absoluto"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } 
        else if (method === "newton") {
            caption.textContent = "Newton table"; 
            table.appendChild(caption);
            const headers = ["i", "xi", "f(xi)", "f'(xi)", "Error absoluto"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } 
        else if (method === "incremental_search") {
            caption.textContent = "Incremental Search table"; 
            table.appendChild(caption);
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
        else if (method === "punto_fijo") {
            caption.textContent = "Punto Fijo table"; 
            table.appendChild(caption);
            const headers = ["i", "xi", "g(xi)", "f(xi)", "Error absoluto"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } 
        else if (method === "secant") {
            caption.textContent = "Secant table"; 
            table.appendChild(caption);
            const headers = ["i", "xi", "f(xi)", "Error absoluto"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } 
        else if (method === "multiple_roots") {
            caption.textContent = "Multiple Roots table"; 
            table.appendChild(caption);
            const headers = ["i", "xi", "h(xi)", "Error absoluto"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } 
        else if (method === "jacobi") {
            caption.textContent = "Jacobi table"; 
            table.appendChild(caption);
            const headers = ["iter", "E", "x"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } 
        else if (method === "seidel") {
            caption.textContent = "Gauss-Seidel table"; 
            table.appendChild(caption);
            const headers = ["iter", "E", "x"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } 
        else if (method === "SOR") {
            caption.textContent = "SOR table"; 
            table.appendChild(caption);
            const headers = ["iter", "E", "x"];
            headers.forEach(header => {
                const header_cel = document.createElement('th');
                header_cel.textContent = header;
                headers_row.appendChild(header_cel);
            });
        } 
        else if (method === "gaussian_simple_elimination" || method === "LU_simple" || method === "LU_partial") {
            caption.textContent = "Coefficients"; 
            table.appendChild(caption);
            const tbody = document.createElement('tbody');
            
            data.forEach(item => {
                const new_row = document.createElement('tr');
                const new_cel = document.createElement('td');
                new_cel.textContent = item; 
                new_row.appendChild(new_cel);
                tbody.appendChild(new_row);
            });
            
            table.appendChild(tbody);
            const result_container = document.getElementById("table");
            result_container.appendChild(table);
            return; // Salir de la función después de manejar este caso
            
        } 
        else if (method === "C") {
            caption.textContent = "C"; 
            table.appendChild(caption);
            const tbody = document.createElement('tbody');
            
            data.forEach(item => {
                const new_row = document.createElement('tr');
                const new_cel = document.createElement('td');
                new_cel.textContent = item; 
                new_row.appendChild(new_cel);
                tbody.appendChild(new_row);
            });
            
            table.appendChild(tbody);
            const result_container = document.getElementById("table");
            result_container.appendChild(table);
            return; // Salir de la función después de manejar este caso
            
        } 
        else if (method === "Matrix L" || method === "Matrix U" || method === "Matrix P" || method === "Matrix T") {
            caption.textContent = method; 
            table.appendChild(caption); // Nuevo manejo para matrices
            data.forEach(row => {
                const tr = document.createElement('tr');
                row.forEach(value => {
                    const td = document.createElement('td');
                    td.textContent = value;
                    tr.appendChild(td);
                });
                table.appendChild(tr);
            });
            
            const result_container = document.getElementById("table");
            result_container.appendChild(table);
            return; // Salir después de manejar matrices.
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
    

    function validateMatrix(A) {
        try {
            let matrix = JSON.parse(A);
    
            if (!Array.isArray(matrix)) {
                throw new Error("La entrada no es una matriz válida. Asegúrate de que esté en formato JSON.");
            }
    
            const size = matrix.length;
            for (let i = 0; i < size; i++) {
                if (!Array.isArray(matrix[i]) || matrix[i].length !== size) {
                    throw new Error("La matriz no es cuadrada. Asegúrate de que todas las filas tengan la misma longitud que el número de filas.");
                }
    
                for (let j = 0; j < size; j++) {
                    if (typeof matrix[i][j] !== 'number') {
                        throw new Error("Todos los elementos deben ser números. Verifica la entrada.");
                    }
                }
            }
            return matrix;
        } catch (error) {
            // Personalizar el mensaje de error si la entrada es incorrecta
            if (error.message.includes("Unexpected token")) {
                alert("Formato incorrecto. Asegúrate de que la matriz esté correctamente formada, como: [[1, 2], [3, 4]].");
            } else {
                alert(error.message);  // Muestra el mensaje de error correspondiente
            }
            return false;
        }
    }
    
    function validateVectorB(A, b) {
        try {
            // Verificar la longitud del vector b
            let vectorB = JSON.parse(b);
            
            if (!Array.isArray(vectorB)) {
                throw new Error("La entrada b no es un vector válido.");
            }
    
            if (A.length !== vectorB.length) {
                throw new Error("El vector b debe tener la misma longitud que la cantidad de filas de la matriz A.");
            }
    
            return vectorB;
        } catch (error) {
            alert(error.message);
            return false;
        }
    }

    function updateMethodTitle(titleText) {
        let titleElement = document.getElementById("method-title");
    
        if (!titleElement) {
            // Crear el título si no existe
            titleElement = document.createElement("h2");
            titleElement.id = "method-title";
            titleElement.style.textAlign = "center";
            titleElement.style.marginTop = "20px";
            titleElement.style.color = "#007bff"; // Color azul bonito
            titleElement.style.fontFamily = "'Arial', sans-serif"; // Fuente más estilizada
            document.getElementById("table").parentElement.insertBefore(titleElement, document.getElementById("table"));
        }
    
        // Actualizar el texto del título
        titleElement.textContent = titleText;
    }
});