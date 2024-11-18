import React, { useState, useEffect } from 'react';
import { getTasks, addTask, deleteTask } from './api';


function App() {
    const [tasks, setTasks] = useState([]);
    const [description, setDescription] = useState('');

    // Fetch tasks from the API on component load
    useEffect(() => {
        loadTasks();
    }, []);

    const loadTasks = async () => {
        try {
            const data = await getTasks();
            setTasks(data);
        } catch (error) {
            console.error('Error loading tasks:', error);
        }
    };

    const handleAddTask = async (e) => {
        e.preventDefault();
        if (!description.trim()) return;

        try {
            await addTask(description);
            setDescription('');
            loadTasks();
        } catch (error) {
            console.error('Error adding task:', error);
        }
    };

    const handleDeleteTask = async (id) => {
        try {
            await deleteTask(id);
            loadTasks();
        } catch (error) {
            console.error('Error deleting task:', error);
        }
    };

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Task Manager</h1>

            <form onSubmit={handleAddTask} className="flex gap-2 mb-4">
                <input
                    type="text"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="New task"
                    className="border p-2 flex-grow"
                />
                <button type="submit" className="bg-blue-500 text-white px-4 py-2">Add Task</button>
            </form>

            <ul className="space-y-2">
                {tasks.map((task) => (
                    <li key={task.id} className="flex justify-between items-center border p-2">
                        <span>{task.description}</span>
                        <button
                            onClick={() => handleDeleteTask(task.id)}
                            className="text-red-500"
                        >
                            Delete
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
