'use client'

import { useAuth } from '@/lib/auth';
import Header from '@/components/Header';
import TaskList from '@/components/TaskList';

export default function Home() {
  const { isSignedIn } = useAuth();

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
        {isSignedIn ? (
          <TaskList />
        ) : (
          <div className="text-center py-10">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Please sign in to access your tasks</h2>
          </div>
        )}
      </main>
    </div>
  );
}