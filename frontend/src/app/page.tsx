'use client'

import { useRouter } from 'next/navigation';
import { useAuth } from '@/lib/auth';
import { useEffect } from 'react';

export default function Home() {
  const router = useRouter();
  const { isSignedIn, loading } = useAuth();

  useEffect(() => {
    if (!loading && !isSignedIn) {
      router.push('/login');
    } else if (!loading && isSignedIn) {
      router.push('/dashboard');
    }
  }, [isSignedIn, loading, router]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
        <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Loading...
        </h2>
      </div>
    );
  }

  return null; // Will redirect or show dashboard
}
