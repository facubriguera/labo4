// Función para verificar si existe el token JWT en las cookies
function getToken() {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        const [name, value] = cookie.trim().split('=');
        if (name === 'token') {
            return value;
        }
    }
    return '';
}

// Función para cargar y mostrar eventos
function loadEventos() {
    fetch('http://127.0.0.1:8000/eventos', {
        headers: {
            'Authorization': `Bearer ${getToken()}` // Obtener token JWT y añadirlo a la cabecera
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        renderEventos(data);
    })
    .catch(error => {
        console.error('Error al cargar eventos:', error);
    });

    // Cargar opciones del select de categorías al mismo tiempo
    loadCategorias();
}

// Función para renderizar eventos en la tabla
function renderEventos(eventos) {
    const tableBody = document.getElementById('eventoTableBody');
    tableBody.innerHTML = '';

    eventos.forEach(evento => {
        //const categoriaNombre = evento.categoria ? evento.categoria.nombre : 'Sin categoría'; // Verificar si evento.categoria está definido

        const row = `
            <tr>
                <td>${evento.id}</td>
                <td>${evento.nombre}</td>
                <td>${evento.fecha_inicio}</td>
                <td>${evento.fecha_fin}</td>
                <td>${evento.lugar}</td>
                <td>${evento.cupos}</td>
                <td>${evento.categoria_id}</td> <!-- Mostrar nombre de la categoría -->
                <td>
                    <button type="button" class="btn btn-info btn-sm" onclick="editEvento(${evento.id})">Editar</button>
                    <button type="button" class="btn btn-danger btn-sm" onclick="deleteEvento(${evento.id})">Eliminar</button>
                </td>
            </tr>
        `;
        tableBody.innerHTML += row;
    });
}

// Función para cargar opciones del select de categorías
function loadCategorias() {
    fetch('http://127.0.0.1:8000/categorias', {
        headers: {
            'Authorization': `Bearer ${getToken()}` // Obtener token JWT y añadirlo a la cabecera
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        const selectCategoriaFilter = document.getElementById('categoriaFilter');
        const selectCategoriaEvento = document.getElementById('eventoCategoria');

        selectCategoriaFilter.innerHTML = ''; // Limpiar opciones actuales
        selectCategoriaEvento.innerHTML = ''; // Limpiar opciones actuales

        // Añadir opción por defecto al filtro
        const defaultOptionFilter = document.createElement('option');
        defaultOptionFilter.value = '';
        defaultOptionFilter.textContent = 'Todas las categorías';
        selectCategoriaFilter.appendChild(defaultOptionFilter);

        // Añadir opciones al select de categoría en el formulario de evento
        data.forEach(categoria => {
            const optionFilter = document.createElement('option');
            optionFilter.value = categoria.id;
            optionFilter.textContent = categoria.nombre;
            selectCategoriaFilter.appendChild(optionFilter);

            const optionEvento = document.createElement('option');
            optionEvento.value = categoria.id;
            optionEvento.textContent = categoria.nombre;
            selectCategoriaEvento.appendChild(optionEvento);
        });
    })
    .catch(error => {
        console.error('Error al cargar categorías:', error);
    });
}

// Función para filtrar eventos por categoría
function filterByCategoria() {
    const categoriaId = document.getElementById('categoriaFilter').value;
    const url = categoriaId ? `http://127.0.0.1:8000/eventos/categoria/${categoriaId}` : 'http://127.0.0.1:8000/eventos';

    fetch(url, {
        headers: {
            'Authorization': `Bearer ${getToken()}` // Obtener token JWT y añadirlo a la cabecera
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        renderEventos(data);
    })
    .catch(error => {
        console.error('Error al filtrar eventos:', error);
    });
}

// Función para guardar un evento (crear o actualizar)
function guardarEvento(event) {
    event.preventDefault();
    
    const id = document.getElementById('eventoId').value;
    const nombre = document.getElementById('eventoNombre').value;
    const descripcion = document.getElementById('eventoDescripcion').value;
    const fecha_inicio = document.getElementById('eventoFechaInicio').value;
    const fecha_fin = document.getElementById('eventoFechaFin').value;
    const lugar = document.getElementById('eventoLugar').value;
    const cupos = document.getElementById('eventoCupos').value;
    const categoria_id = document.getElementById('eventoCategoria').value;

    const evento = { id, nombre, descripcion, fecha_inicio, fecha_fin, lugar, cupos, categoria_id };

    const method = id ? 'PUT' : 'POST';
    const url = id ? `http://127.0.0.1:8000/eventos/${id}` : 'http://127.0.0.1:8000/eventos';

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}` // Obtener token JWT y añadirlo a la cabecera
        },
        body: JSON.stringify(evento)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(data => {
        loadEventos(); // Recargar eventos después de guardar
        $('#eventoModal').modal('hide');
        resetForm();
    })
    .catch(error => {
        console.error('Error al guardar evento:', error);
    });
}

// Función para eliminar un evento
function deleteEvento(id) {
    if (!confirm('¿Estás seguro de que quieres eliminar este evento?')) {
        return;
    }

    fetch(`http://127.0.0.1:8000/eventos/${id}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${getToken()}` // Obtener token JWT y añadirlo a la cabecera
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error HTTP ${response.status}: ${response.statusText}`);
        }
        loadEventos(); // Recargar eventos después de eliminar
    })
    .catch(error => {
        console.error('Error al eliminar evento:', error);
    });
}

// Función para editar un evento (cargar datos en el formulario)
function editEvento(id) {
    fetch(`http://127.0.0.1:8000/eventos/${id}`, {
        headers: {
            'Authorization': `Bearer ${getToken()}` // Obtener token JWT y añadirlo a la cabecera
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(evento => {
        document.getElementById('eventoId').value = evento.id;
        document.getElementById('eventoNombre').value = evento.nombre;
        document.getElementById('eventoDescripcion').value = evento.descripcion;
        document.getElementById('eventoFechaInicio').value = evento.fecha_inicio;
        document.getElementById('eventoFechaFin').value = evento.fecha_fin;
        document.getElementById('eventoLugar').value = evento.lugar;
        document.getElementById('eventoCupos').value = evento.cupos;
        document.getElementById('eventoCategoria').value = evento.categoria_id;

        $('#eventoModal').modal('show');
    })
    .catch(error => {
        console.error('Error al cargar evento:', error);
    });
}

// Función para resetear el formulario
function resetForm() {
    document.getElementById('eventoForm').reset();
    document.getElementById('eventoId').value = '';
}

// Inicializar carga de eventos y categorías al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    loadEventos();
});
