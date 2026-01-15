import type { Metadata } from 'next'
// import { Inter } from 'next/font/google'
import './globals.css'
import { AuthProvider, authClient } from '@/lib/auth' // <--- Added authClient import

// const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Todo Application',
  description: 'A full-featured todo application with user authentication',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body /*className={inter.className}*/>
        <AuthProvider authClient={authClient}> {/* <--- Added authClient prop */}
          {children}
        </AuthProvider>
      </body>
    </html>
  )
}
