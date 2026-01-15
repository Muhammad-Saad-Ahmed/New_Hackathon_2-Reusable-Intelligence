'use client';

// Import AuthUIProvider from the newly installed UI package.
import { createAuthClient } from 'better-auth/react';
import { AuthUIProvider } from '@daveyplate/better-auth-ui'; // <--- New import
import { useMemo } from 'react';

export const authClient = createAuthClient({
  // baseURL: process.env.NEXT_PUBLIC_AUTH_SERVER_URL || "http://localhost:3000/api/auth",
  // It's crucial to configure this for a real application.
  // For now, we'll let better-auth infer, or assume a local setup.
});

// Destructure useSession from the authClient instance
const { useSession } = authClient;

// Create a custom useAuth hook that matches the expected interface in dashboard/page.tsx and login/page.tsx
export function useAuth() {
  const { data: session, isPending, error, refetch } = useSession();

  // Memoize the returned object to prevent unnecessary re-renders
  const authState = useMemo(() => {
    const user = session?.user || null;
    const isSignedIn = !!user; // Convert user object presence to a boolean

    return {
      user,
      isSignedIn,
      isPending, // Expose loading state
      error,
      refetch,
      signin: authClient.signIn, // Expose signIn function
      signOut: authClient.signOut, // Expose signOut function
    };
  }, [session, isPending, error, refetch]);

  return authState;
}

// Export AuthUIProvider aliased as AuthProvider
export { AuthUIProvider as AuthProvider }; // <--- Changed export
