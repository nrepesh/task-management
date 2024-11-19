import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

/**
 * Fetch all tasks from the backend.
 * Makes a GET request to the /tasks endpoint to retrieve the list of tasks.
 * @returns {Promise<Array>} Array of task objects from the backend
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
 * Sends a POST request to the /tasks endpoint with the task description in the request body.
 * @param {string} description - The description of the new task
 * @returns {Promise<Object>} The created task object returned from the backend
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
 * Makes a DELETE request to the /tasks/:id endpoint to delete the specified task.
 * @param {number} id - The ID of the task to delete
 * @returns {Promise<Object>} A confirmation message from the backend
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
