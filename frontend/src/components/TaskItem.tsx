import { useState } from 'react';

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

interface TaskItemProps {
  task: Task;
  onToggleComplete: (id: string, completed: boolean) => void;
  onDelete: (id: string) => void;
  onEdit: (task: Task) => void;
}

export default function TaskItem({ task, onToggleComplete, onDelete, onEdit }: TaskItemProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);
  const [editDescription, setEditDescription] = useState(task.description || '');

  const handleSaveEdit = () => {
    onEdit({ ...task, title: editTitle, description: editDescription });
    setIsEditing(false);
  };

  const handleCancelEdit = () => {
    setEditTitle(task.title);
    setEditDescription(task.description || '');
    setIsEditing(false);
  };

  return (
    <li className="px-4 py-4 sm:px-6 flex justify-between items-center">
      {isEditing ? (
        <div className="flex-1">
          <input
            type="text"
            value={editTitle}
            onChange={(e) => setEditTitle(e.target.value)}
            className="w-full border border-gray-300 rounded-md px-2 py-1 mb-2"
          />
          <textarea
            value={editDescription}
            onChange={(e) => setEditDescription(e.target.value)}
            className="w-full border border-gray-300 rounded-md px-2 py-1 mb-2"
            rows={2}
          />
          <div className="flex space-x-2">
            <button
              onClick={handleSaveEdit}
              className="bg-green-500 hover:bg-green-700 text-white font-bold py-1 px-2 rounded text-sm"
            >
              Save
            </button>
            <button
              onClick={handleCancelEdit}
              className="bg-gray-500 hover:bg-gray-700 text-white font-bold py-1 px-2 rounded text-sm"
            >
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <>
          <div className="flex items-center flex-1">
            <input
              type="checkbox"
              checked={task.completed}
              onChange={(e) => onToggleComplete(task.id, e.target.checked)}
              className="h-4 w-4 text-blue-600 rounded"
            />
            <div className="ml-3 flex-1">
              <span className={`block ${task.completed ? 'line-through text-gray-500' : 'text-gray-900'}`}>
                {task.title}
              </span>
              {task.description && (
                <p className={`text-sm ${task.completed ? 'line-through text-gray-400' : 'text-gray-500'}`}>
                  {task.description}
                </p>
              )}
            </div>
            {task.priority && (
              <span className={`ml-2 px-2 py-1 text-xs rounded-full ${
                task.priority === 'high' ? 'bg-red-100 text-red-800' :
                task.priority === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                'bg-green-100 text-green-800'
              }`}>
                {task.priority}
              </span>
            )}
          </div>
          <div className="flex space-x-2">
            <button
              onClick={() => setIsEditing(true)}
              className="text-blue-600 hover:text-blue-900"
            >
              Edit
            </button>
            <button
              onClick={() => onDelete(task.id)}
              className="text-red-600 hover:text-red-900"
            >
              Delete
            </button>
          </div>
        </>
      )}
    </li>
  );
}