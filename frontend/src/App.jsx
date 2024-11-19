import React, { useState } from 'react';
import { useTasksHelper } from './useTasksHelper';
import { ADD_ITEMS, DELETE_ITEMS } from './constants.js';

/**
 * Main component for the Task Manager application.
 * Handles task addition, deletion, and displays the task list.
 */
function App() {
    const { tasks, error, addTaskHandler, deleteTaskHandler } = useTasksHelper();
    const [description, setDescription] = useState('');

    /**
     * Handles the submission of the add task form.
     * Prevents default form submission behavior, calls the addTaskHandler, and clears the input.
     * @param {Event} e - Form submission event
     */
    const handleSubmit = (e) => {
        e.preventDefault();
        addTaskHandler(description);
        setDescription('');
    };

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Task Manager</h1>

            {/* Display error message if an error occurs */}
            {error && <p className="text-red-500">{error}</p>}

            {/* Add Task Form */}
            <form onSubmit={handleSubmit} className="flex gap-2 mb-4">
                <input
                    type="text"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="New task"
                    className="border p-2 flex-grow"
                />
                <button type="submit" className="bg-blue-500 text-white px-4 py-2">
                    {ADD_ITEMS}
                </button>
            </form>

            {/* Task List */}
            <ul className="space-y-2">
                {tasks.map((task) => (
                    <li key={task.id} className="flex justify-between items-center border p-2">
                        <span>{task.description}</span>
                        <button
                            onClick={() => deleteTaskHandler(task.id)}
                            className="text-red-500"
                        >
                            {DELETE_ITEMS}
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;