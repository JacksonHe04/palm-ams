// src/apis/students.js
import http from '../utils/http';

export const getStudents = async () => {
  try {
    const response = await http.get('/api/students/');
    return response.data;
  } catch (error) {
    console.error('Error fetching students:', error);
    throw error;
  }
};
