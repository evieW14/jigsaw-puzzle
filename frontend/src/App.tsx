import {useEffect, useState} from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import './App.css'
import {api} from "../api/client.ts";
import Board from "../src/components/Board.tsx"

function App() {
  function getHealth() {
    return api("/health");
  }

  useEffect(() => {
    getHealth().then((data) => {
        console.log(data)
    })
  }, []);

  return (
    <>
      <section id="center">
        <div>
          <h1>Get started</h1>
          <Board />
        </div>
      </section>
      <section id="spacer"></section>
    </>
  )
}

export default App
