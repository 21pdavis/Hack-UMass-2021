import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import MainContents from './components/MainContents';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Navbar />
      </header>
      <MainContents />
      <Footer />
      
    </div>
  );
}

export default App;
