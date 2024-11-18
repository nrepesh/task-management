import axios from 'axios';

const BASE_URL = 'http://localhost:8000'; // Adjust this URL if your backend runs on a different port or host

/**
 * Fetch all tasks from the backend.
 * @returns {Promise<Array>} Array of task objects
 */
export const getTasks = async () => {
    try {
        const response = await axios.get(`${BASE_URL}/tasks`);
        return response.data;
    } catch (error) {
        console.error('Error fetching tasks:', error);
        throw error;
    }
};

/**
 * Add a new task to the backend.
 * @param {string} description - The description of the task
 * @returns {Promise<Object>} The created task object
 */
export const addTask = async (description) => {
    try {
        const response = await axios.post(`${BASE_URL}/tasks`, { description });
        return response.data;
    } catch (error) {
        console.error('Error adding task:', error);
        throw error;
    }
};

/**
 * Delete a task by ID from the backend.
 * @param {number} id - The ID of the task to delete
 * @returns {Promise<Object>} Confirmation message
 */
export const deleteTask = async (id) => {
    try {
        const response = await axios.delete(`${BASE_URL}/tasks/${id}`);
        return response.data;
    } catch (error) {
        console.error('Error deleting task:', error);
        throw error;
    }
};
