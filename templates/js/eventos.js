// Función para cargar y mostrar eventos
function loadEventos() {
    fetch('http://127.0.0.1:8000/eventos', {
        headers: {
            'Authorization': `Bearer ${getToken()}` // Obtener token JWT y añadirlo a la cabecera
        }
    })
    .then(response => response.json())
    .then(data => {
        // Limpiar tabla antes de agregar datos nuevos
        const tableBody = document.getElementById('eventoTableBody');
        tableBody.innerHTML = '';
        // Agregar cada evento a la tabla
        data.forEach(evento => {
            const row = `
                <tr>
                    <td>${evento.id}</td>
                    <td>${evento.nombre}</td>
                    <td>${evento.fecha_inicio}</td>
                    <td>
                        <button type="button" class="btn btn-info btn-sm" onclick="editEvento(${evento.id})">Editar</button>
                        <button type="button" class="btn btn-danger btn-sm" onclick="deleteEvento(${evento.id})">Eliminar</button>
                    </td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });
    })
    .catch(error => {
        console.error('Error al cargar eventos:', error);
    });
}

// Función para crear un nuevo evento
function guardarEvento(event) {
    event.preventDefault();
    const nombre = document.getElementById('eventoNombre').value;
    const fecha = document.getElementById('eventoFecha').value;
    
    fetch('http://127.0.0.1:8000/eventos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}` // Añadir token JWT a la cabecera
        },
        body: JSON.stringify({ nombre: nombre, fecha: fecha })
    })
    .then(response => {
        if (response.ok) {
            $('#eventoModal').modal('hide'); // Ocultar modal después de guardar
            loadEventos(); // Volver a cargar eventos después de guardar
        } else {
            alert('Error al guardar el evento');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al guardar el evento');
    });
}

// Función para eliminar un evento
function deleteEvento(id) {
    if (confirm('¿Estás seguro de que quieres eliminar este evento?')) {
        fetch(`http://127.0.0.1:8000/eventos/${id}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${getToken()}` // Añadir token JWT a la cabecera
            }
        })
        .then(response => {
            if (response.ok) {
                loadEventos(); // Volver a cargar eventos después de eliminar
            } else {
                alert('Error al eliminar el evento');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error al eliminar el evento');
        });
    }
}


// Función para editar un evento
function editEvento(id) {
    fetch(`http://127.0.0.1:8000/eventos/${id}`, {
        headers: {
            'Authorization': `Bearer ${getToken()}`
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error HTTP ${response.status}: ${response.statusText}`);
        }
        return response.json();
    })
    .then(evento => {
        // Asegurar que los elementos existan antes de asignarles valores
        const eventoIdInput = document.getElementById('eventoId');
        const eventoNombreInput = document.getElementById('eventoNombre');
        const eventoFechaInput = document.getElementById('eventoFecha');

        if (eventoIdInput && eventoNombreInput && eventoFechaInput) {
            // Llenar el formulario con los datos del evento
            eventoIdInput.value = evento.id;
            eventoNombreInput.value = evento.nombre;

            // Formatear la fecha para mostrarla correctamente en el input type="date"
            const fecha = new Date(evento.fecha_inicio);
            const fechaFormateada = fecha.toISOString().substring(0, 10); // YYYY-MM-DD
            eventoFechaInput.value = fechaFormateada;

            // Cambiar título del modal y atributo 'data-action'
            const modalTitle = document.getElementById('eventoModalLabel');
            modalTitle.textContent = 'Editar Evento';
            document.getElementById('eventoForm').setAttribute('data-action', 'editar');

            // Mostrar el modal de evento
            $('#eventoModal').modal('show');
        } else {
            console.error('No se encontraron los elementos del formulario de evento.');
            alert('Error al cargar el evento para editar. Consulta la consola para más detalles.');
        }
    })
    .catch(error => {
        console.error('Error al cargar el evento para editar:', error);
        alert('Error al cargar el evento para editar. Consulta la consola para más detalles.');
    });
}









// Función para obtener el token JWT almacenado en las cookies
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

// Cargar eventos al cargar la página
document.addEventListener('DOMContentLoaded', function() {
    loadEventos();
});
