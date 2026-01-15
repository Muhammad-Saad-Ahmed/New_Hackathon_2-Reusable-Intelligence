"use client";

import { useState, useEffect, createContext, useContext, ReactNode } from 'react';
import { useRouter } from 'next/navigation';

const AuthContext = createContext<any>(null);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const checkUser = async () => {
      const token = localStorage.getItem('token');
      if (token) {
        const { success, data, error } = await apiClient.getMe();
        if (success) {
          setUser(data);
        } else {
          console.error('Failed to fetch user data:', error);
          localStorage.removeItem('token');
        }
      }
      setLoading(false);
    };

    checkUser();
  }, []);

  const signin = async (email: string, password: string) => {
    const { success, data, error } = await apiClient.signin(email, password);

    if (success && data.access_token) {
      localStorage.setItem('token', data.access_token);
      
      const { success: meSuccess, data: meData, error: meError } = await apiClient.getMe();
      
      if(meSuccess) {
        setUser(meData);
        router.push('/dashboard');
        return true;
      } else {
        console.error('Failed to fetch user data:', meError);
        // still logged in, but we dont have user data
        // you might want to handle this case differently
        router.push('/dashboard');
        return true;
      }
    }

    console.error('Signin failed:', error);
    return false;
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
