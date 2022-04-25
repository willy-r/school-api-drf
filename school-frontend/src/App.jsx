import ListCourses from './components/ListCourses';
import Footer from './components/Footer';

import './App.css';

import logo from './logo.svg';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Courses</h1>
      </header>
      <ListCourses/>
      <Footer/>
    </div>
  );
}

export default App;
