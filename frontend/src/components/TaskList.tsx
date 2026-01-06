import { useState, useEffect } from 'react';
import TaskItem from './TaskItem';
import TaskForm from './TaskForm';
import { apiClient } from '@/lib/api';
import { useAuth } from '@/lib/auth';

interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  priority?: string;
  tags?: string[];
  user_id: string;
  created_at: string;
  updated_at: string;
}

export default function TaskList() {
  const { user } = useAuth();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [showForm, setShowForm] = useState(false);
  const [editingTask, setEditingTask] = useState<Task | null>(null);
  const [filters, setFilters] = useState({
    status: 'all', // 'all', 'completed', 'incomplete'
    priority: 'all', // 'all', 'high', 'medium', 'low'
    search: ''
  });

  // Fetch tasks when user changes or filters change
  useEffect(() => {
    if (user) {
      fetchTasks();
    }
  }, [user, filters]);

  const fetchTasks = async () => {
    if (!user) return;

    try {
      const response = await apiClient.getTasks(user.id, {
        status: filters.status !== 'all' ? filters.status : undefined,
        priority: filters.priority !== 'all' ? filters.priority : undefined
      });

      if (response.success && response.data) {
        // The response.data could be an array of tasks or an object with a data property
        let tasksData = Array.isArray(response.data) ? response.data : (response.data as any).data;
        if (!Array.isArray(tasksData)) {
          tasksData = [];
        }

        // Apply search filter client-side
        let filteredTasks = tasksData as Task[];
        if (filters.search) {
          const searchTerm = filters.search.toLowerCase();
          filteredTasks = filteredTasks.filter(task =>
            task.title.toLowerCase().includes(searchTerm) ||
            (task.description && task.description.toLowerCase().includes(searchTerm))
          );
        }

        setTasks(filteredTasks);
      }
    } catch (error) {
      console.error('Error fetching tasks:', error);
    }
  };

  const handleAddTask = async (taskData: { title: string; description?: string; priority?: string; tags?: string[] }) => {
    if (!user) return;

    try {
      const response = await apiClient.createTask(user.id, {
        ...taskData,
        completed: false
      });

      if (response.success) {
        setShowForm(false);
        fetchTasks(); // Refresh the task list
      }
    } catch (error) {
      console.error('Error adding task:', error);
    }
  };

  const handleUpdateTask = async (taskData: { title: string; description?: string; priority?: string; tags?: string[] }) => {
    if (!user || !editingTask) return;

    try {
      // Merge the new task data with the existing task data
      const updatedTaskData = {
        ...editingTask,
        ...taskData
      };

      const response = await apiClient.updateTask(user.id, editingTask.id, updatedTaskData);

      if (response.success) {
        setEditingTask(null);
        fetchTasks(); // Refresh the task list
      }
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  const handleToggleComplete = async (taskId: string, completed: boolean) => {
    if (!user) return;

    try {
      const response = await apiClient.updateTaskCompletion(user.id, taskId, completed);

      if (response.success) {
        fetchTasks(); // Refresh the task list
      }
    } catch (error) {
      console.error('Error updating task completion:', error);
    }
  };

  const handleDeleteTask = async (taskId: string) => {
    if (!user) return;

    if (window.confirm('Are you sure you want to delete this task?')) {
      try {
        const response = await apiClient.deleteTask(user.id, taskId);

        if (response.success) {
          fetchTasks(); // Refresh the task list
        }
      } catch (error) {
        console.error('Error deleting task:', error);
      }
    }
  };

  const handleEditTask = (task: Task) => {
    setEditingTask(task);
    setShowForm(true);
  };

  const handleFilterChange = (filterType: string, value: string) => {
    setFilters(prev => ({
      ...prev,
      [filterType]: value
    }));
  };

  return (
    <div className="mt-6">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-xl font-semibold text-gray-800">Your Tasks</h2>
        <button
          onClick={() => {
            setEditingTask(null);
            setShowForm(true);
          }}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Add Task
        </button>
      </div>

      {/* Filters */}
      <div className="mb-6 p-4 bg-white rounded-lg shadow">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Status</label>
            <select
              value={filters.status}
              onChange={(e) => handleFilterChange('status', e.target.value)}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="all">All</option>
              <option value="incomplete">Incomplete</option>
              <option value="completed">Completed</option>
            </select>
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Priority</label>
            <select
              value={filters.priority}
              onChange={(e) => handleFilterChange('priority', e.target.value)}
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="all">All</option>
              <option value="high">High</option>
              <option value="medium">Medium</option>
              <option value="low">Low</option>
            </select>
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">Search</label>
            <input
              type="text"
              value={filters.search}
              onChange={(e) => handleFilterChange('search', e.target.value)}
              placeholder="Search tasks..."
              className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
        </div>
      </div>

      {/* Add/Edit Task Form */}
      {showForm && (
        <TaskForm
          onSubmit={editingTask ? handleUpdateTask : handleAddTask}
          onCancel={() => {
            setShowForm(false);
            setEditingTask(null);
          }}
          initialData={editingTask || undefined}
        />
      )}

      {/* Task List */}
      <div className="bg-white shadow overflow-hidden sm:rounded-md">
        {tasks.length === 0 ? (
          <div className="text-center py-8">
            <p className="text-gray-500">No tasks found. Add a new task to get started!</p>
          </div>
        ) : (
          <ul className="divide-y divide-gray-200">
            {tasks.map((task) => (
              <TaskItem
                key={task.id}
                task={task}
                onToggleComplete={handleToggleComplete}
                onDelete={handleDeleteTask}
                onEdit={handleEditTask}
              />
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}