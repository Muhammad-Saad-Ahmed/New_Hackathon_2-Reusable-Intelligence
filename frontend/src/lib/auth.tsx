"use client";

import { useState, useEffect, createContext, useContext, ReactNode } from 'react';
import { useRouter } from 'next/navigation';

const AuthContext = createContext<any>(null);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    // Check for a token or user session
    const token = localStorage.getItem('token');
    if (token) {
      // In a real app, you'd validate the token with the backend
      // and fetch user data.
      // For now, we'll just simulate a logged-in user.
      setUser({ email: 'test@example.com', name: 'Test User', id: 1 });
    }
    setLoading(false);
  }, []);

  const signin = (email: string, token: string) => {
    localStorage.setItem('token', token);
    // In a real app, you'd fetch user data from the backend here
    setUser({ email, name: 'User', id: 1 });
    router.push('/dashboard');
  };

  const signout = () => {
    localStorage.removeItem('token');
    setUser(null);
    router.push('/login');
  };

  const value = {
    user,
    loading,
    signin,
    signout,
    isSignedIn: !loading && user,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  return useContext(AuthContext);
};
