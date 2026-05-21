import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [todos, setTodos] = useState([]);
  const [text, setText] = useState("");

  const API = import.meta.env.VITE_API_URL;

  const fetchTodos = async () => {
    const res = await axios.get(`${API}/todos`);
    setTodos(res.data);
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  const addTodo = async () => {
    await axios.post(`${API}/todos`, {
      text,
    });

    setText("");
    fetchTodos();
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>FastAPI Todo 🚀</h1>

      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button onClick={addTodo}>
        Add
      </button>

      {todos.map((todo) => (
        <div key={todo.id}>
          {todo.text}
        </div>
      ))}
    </div>
  );
}

export default App;
