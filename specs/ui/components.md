# Todo Application - UI Components Specification

## Overview
This document specifies the UI components for the Phase II Todo web application using Next.js 16+ with the App Router.

## Design Principles
- Responsive design for all screen sizes
- Clean, minimalist interface focused on usability
- Consistent styling using a design system
- Accessibility compliance (WCAG 2.1 AA)
- Performance optimization with lazy loading

## Technology Stack
- Next.js 16+ with App Router
- React Components
- Tailwind CSS or similar styling solution
- Client-side state management
- Better Auth integration for authentication UI

## Component Structure

### Layout Components

#### RootLayout
- Global layout wrapper for the entire application
- Includes header, main content area, and footer
- Handles global styles and metadata

#### AuthLayout
- Layout for authentication pages (login, signup)
- Centered form container with branding
- Minimal design focused on authentication flow

### Navigation Components

#### Header
- Application header with logo and navigation
- Authentication status indicator
- User profile dropdown when logged in
- Mobile-responsive hamburger menu

#### Sidebar
- Navigation sidebar for main application
- Links to different sections (All Tasks, Completed, etc.)
- Collapsible on smaller screens

### Authentication Components

#### LoginForm
- Email and password input fields
- Sign in button
- Link to sign up page
- Error message display
- "Remember me" option

#### SignUpForm
- Email, name, and password input fields
- Sign up button
- Link to login page
- Password strength indicator
- Terms and conditions checkbox

### Task Management Components

#### TaskList
- Container for displaying multiple tasks
- Implements infinite scrolling or pagination
- Shows loading states
- Empty state when no tasks exist
- Filtering and sorting controls

#### TaskItem
- Individual task display component
- Checkbox for completion status
- Title and description
- Priority indicator
- Tag display
- Action buttons (edit, delete)
- Visual styling based on completion status

#### TaskForm
- Form for creating or editing tasks
- Title input field (required)
- Description textarea (optional)
- Priority selection dropdown
- Tags input with autocomplete
- Save and cancel buttons
- Validation error display

#### TaskFilter
- Component for filtering tasks
- Status filter (all, completed, incomplete)
- Priority filter (high, medium, low)
- Search input
- Clear filters button

#### TaskSort
- Component for sorting tasks
- Sort by options (title, priority, date created, due date)
- Sort direction (ascending, descending)
- Visual indicator of current sort

### Dashboard Components

#### TaskSummary
- Summary statistics for tasks
- Total tasks count
- Completed tasks count
- Pending tasks count
- Progress visualization

#### QuickAddTask
- Simplified form for quickly adding tasks
- Single input field for task title
- Add button
- Optional due date picker

### Feature Components (Intermediate/Advanced)

#### PrioritySelector
- UI element for selecting task priority
- Visual indicators for different priority levels
- Options: low, medium, high

#### TagManager
- Component for managing task tags
- Tag input with suggestions
- Ability to create new tags
- Tag selection for tasks

#### RecurringTaskForm
- Form for setting up recurring tasks
- Recurrence pattern selection (daily, weekly, monthly, etc.)
- End date option
- Advanced pattern configuration

#### DueDateSelector
- Date and time picker for task due dates
- Time zone handling
- Reminder setting options
- Visual calendar interface

### Utility Components

#### LoadingSpinner
- Generic loading indicator
- Various sizes for different contexts
- Accessible loading state

#### ErrorMessage
- Standardized error message display
- Different severity levels
- Dismissible option

#### ConfirmationDialog
- Modal dialog for confirming destructive actions
- Title, message, and action buttons
- Keyboard accessibility

## Page Structure

### Authentication Pages
- `/login` - Login form page
- `/signup` - Sign up form page

### Main Application Pages
- `/dashboard` - Main dashboard with task overview
- `/tasks` - All tasks view
- `/tasks/completed` - Completed tasks view
- `/tasks/incomplete` - Incomplete tasks view
- `/settings` - User settings and preferences

### API Routes
- `/api/auth/...` - Better Auth routes
- `/api/users/...` - User-related API endpoints
- `/api/tasks/...` - Task-related API endpoints

## Responsive Design

### Mobile (0-768px)
- Single column layout
- Hamburger menu for navigation
- Stacked form elements
- Touch-friendly controls

### Tablet (768px-1024px)
- Two-column layout where appropriate
- Expanded navigation
- Medium-sized form elements

### Desktop (1024px+)
- Multi-column layout
- Full navigation sidebar
- Full-width forms
- Additional information panels

## Accessibility Features
- Semantic HTML structure
- Proper ARIA attributes
- Keyboard navigation support
- Screen reader compatibility
- Sufficient color contrast
- Focus indicators

## State Management
- Client-side state for UI interactions
- Caching for API responses
- Optimistic updates for better UX
- Error boundaries for graceful error handling

## Performance Considerations
- Component lazy loading
- Code splitting
- Image optimization
- Efficient re-rendering
- Caching strategies