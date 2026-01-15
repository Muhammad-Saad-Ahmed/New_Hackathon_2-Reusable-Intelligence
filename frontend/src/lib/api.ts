// Base URL for the API, with robust handling for different environments
let apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';

// Ensure the API URL is correctly formatted with the /api/v1 prefix
if (!apiUrl.endsWith('/api/v1')) {
  if (apiUrl.endsWith('/')) {
    apiUrl = `${apiUrl}api/v1`;
  } else {
    apiUrl = `${apiUrl}/api/v1`;
  }
}

const API_URL = apiUrl;

const getAuthToken = () => {
  if (typeof window === 'undefined') {
    return null;
  }
  return localStorage.getItem('token');
};

const handleResponse = async (response: Response) => {
  if (response.ok) {
    const data = await response.json();
    return { success: true, data };
  } else {
    const error = await response.json().catch(() => ({ detail: 'An unknown error occurred' }));
    return { success: false, error: error.detail || 'API request failed' };
  }
};

export const apiClient = {
  async getTasks(userId: string, filters?: { status?: string; priority?: string }) {
    const token = getAuthToken();
    const query = new URLSearchParams();
    if (filters?.status) {
      query.append('status', filters.status);
    }
    if (filters?.priority) {
      query.append('priority', filters.priority);
    }

    try {
      const response = await fetch(`${API_URL}/${userId}/tasks?${query.toString()}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      });
      return await handleResponse(response);
    } catch (error) {
      return { success: false, error: 'Network error or server is down' };
    }
  },

  async createTask(userId: string, taskData: { title: string; description?: string; priority?: string; tags?: string[], completed: boolean }) {
    const token = getAuthToken();
    try {
      const response = await fetch(`${API_URL}/${userId}/tasks`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ ...taskData, user_id: userId }),
      });
      return await handleResponse(response);
    } catch (error) {
      return { success: false, error: 'Network error or server is down' };
    }
  },

  async updateTask(userId: string, taskId: string, taskData: any) {
    const token = getAuthToken();
    try {
      const response = await fetch(`${API_URL}/${userId}/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ ...taskData, user_id: userId }),
      });
      return await handleResponse(response);
    } catch (error) {
        return { success: false, error: 'Network error or server is down' };
    }
  },

  async updateTaskCompletion(userId: string, taskId: string, completed: boolean) {
    const token = getAuthToken();
    try {
      const response = await fetch(`${API_URL}/${userId}/tasks/${taskId}/complete`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ completed }),
      });
      return await handleResponse(response);
    } catch (error) {
      return { success: false, error: 'Network error or server is down' };
    }
  },

  async deleteTask(userId: string, taskId: string) {
    const token = getAuthToken();
    try {
      const response = await fetch(`${API_URL}/${userId}/tasks/${taskId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      });
      return await handleResponse(response);
    } catch (error) {
      return { success: false, error: 'Network error or server is down' };
    }
  },

  async signin(email: string, password: string) {
    try {
      const response = await fetch(`${API_URL}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ email: email, password: password }),
      });
      return await handleResponse(response);
    } catch (error) {
      return { success: false, error: 'Network error or server is down' };
    }
  },

  async getMe() {
    const token = getAuthToken();
    try {
      const response = await fetch(`${API_URL}/auth/me`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
      });
      return await handleResponse(response);
    } catch (error) {
      return { success: false, error: 'Network error or server is down' };
    }
  },

  async signup(userData: {name: string, email: string, password: string}) {
    try {
      const response = await fetch(`${API_URL}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData),
      });
      return await handleResponse(response);
    } catch (error) {
      return { success: false, error: 'Network error or server is down' };
    }
  }
};