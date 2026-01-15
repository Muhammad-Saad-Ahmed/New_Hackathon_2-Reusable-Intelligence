"use client"
import { useAuth } from '@/lib/auth';
import Link from 'next/link';

export default function Header() {
  const { user, signOut, isSignedIn } = useAuth();

  return (
    <header className="bg-white shadow">
      <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8 flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-900">Todo App</h1>
        <div>
          {isSignedIn ? (
            <div className="flex items-center space-x-4">
              <span>Hello, {user?.name || user?.email}!</span>
              <button
                onClick={() => signOut()}
                className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
              >
                Sign Out
              </button>
            </div>
          ) : (
            <Link href="/login">
              <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Sign In
              </button>
            </Link>
          )}
        </div>
      </div>
    </header>
  );
}