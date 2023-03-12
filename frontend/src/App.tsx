import React, { useEffect, useState } from "react";
import "./App.css";
import { ApiService, Question } from "./rest-api";
import Box from "@mui/material/Box";

function QuestionCard({ question }: { question: Question }) {
  return <Box>{question.text}</Box>;
}

function App() {
  const [questions, setQuestions] = useState<Question[]>([]);
  useEffect(() => {
    ApiService.apiQuestionsList().then((data) => setQuestions(data));
  }, []);

  return (
    <Box className="App">
      {questions.map((question) => (
        <QuestionCard question={question} />
      ))}
    </Box>
  );
}

export default App;
