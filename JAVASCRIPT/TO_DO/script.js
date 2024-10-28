const taskInput = document.getElementById('taskInput');
const addTaskButton = document.getElementById('addTaskButton');
const activeTasksList = document.getElementById('activeTasks');
const completedTasksList = document.getElementById('completedTasks');
const toggleModeButton = document.getElementById('toggleMode');

addTaskButton.addEventListener('click', addTask);
toggleModeButton.addEventListener('click', toggleMode);

function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText) {
        const listItem = document.createElement('li');
        listItem.className = 'list-group-item d-flex justify-content-between align-items-center';
        listItem.innerHTML = `
            ${taskText}
            <button class="btn btn-success btn-sm complete-btn">Concluir</button>
        `;
        activeTasksList.appendChild(listItem);
        taskInput.value = '';
    }
}

activeTasksList.addEventListener('click', function(event) {
    if (event.target.classList.contains('complete-btn')) {
        const taskItem = event.target.parentElement;
        completedTasksList.appendChild(taskItem);
        event.target.remove();
    }
});

function toggleMode() {
    document.body.classList.toggle('bg-dark');
    const isDarkMode = document.body.classList.contains('bg-dark');
    toggleModeButton.textContent = isDarkMode ? 'Modo Claro' : 'Modo Escuro';
}
