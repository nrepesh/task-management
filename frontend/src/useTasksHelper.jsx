import { useState, useEffect } from 'react';
import { getTasks, addTask, deleteTask } from './api';

/**
 * Custom hook to manage task-related operations (fetch, add, delete).
 * It provides state management and API interaction for tasks.
 * @returns {object} Object containing tasks, error, and handlers for adding and deleting tasks
 */
export const useTasksHelper = () => {
    const [tasks, setTasks] = useState([]);
    const [error, setError] = useState(null);

    // Fetch tasks on mount
    useEffect(() => {
        /**
         * Fetch tasks from the backend and update the tasks state.
         * If an error occurs, set the error state.
         */
        const fetchTasks = async () => {
            try {
                const data = await getTasks();
                setTasks(data);
            } catch (err) {
                setError('Failed to load tasks');
            }
        };
        fetchTasks();
    }, []);

    /**
     * Add a new task to the list.
     * @param {string} description - The description of the new task.
     */
    const addTaskHandler = async (description) => {
        if (!description) return;

        try {
            const newTask = await addTask(description);
            setTasks((prevTasks) => [newTask, ...prevTasks]);
        } catch (err) {
            console.error('Error adding task:', err);
            setError('Failed to add task');
        }
    };

    /**
     * Delete a task from the list by its ID.
     * @param {number} id - The ID of the task to delete.
     */
    const deleteTaskHandler = async (id) => {
        try {
            await deleteTask(id);
            setTasks((prevTasks) => prevTasks.filter((task) => task.id !== id));
        } catch (err) {
            console.error('Error deleting task:', err);
            setError('Failed to delete task');
        }
    };

    return {
        tasks,
        error,
        addTaskHandler,
        deleteTaskHandler,
    };
};