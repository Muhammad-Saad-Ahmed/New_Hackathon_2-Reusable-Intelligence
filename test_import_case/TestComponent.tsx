// This is a test file with correct import case
import { Header } from './subfolder/correctfile';

// This import has incorrect case (should be CorrectFile.tsx)
import { SomeComponent } from './subfolder/incorrectfile';

// Another import with incorrect case
import { AnotherComponent } from '../components/tasklist';

export default function TestComponent() {
  return (
    <div>
      <Header />
      <SomeComponent />
      <AnotherComponent />
    </div>
  );
}