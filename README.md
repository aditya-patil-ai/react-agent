# ReAct AI Agent

A simple ReAct (Reasoning + Acting) AI agent built with Python and Groq. 
The project demonstrates how an LLM can reason about a task, select an appropriate tool, observe the result, and continue until it reaches a final answer.

# Overview

This project implements the ReAct agent pattern:

```text
User Question
      ↓
   Thought
      ↓
    Action
      ↓
     Tool
      ↓
  Observation
      ↓
   Thought
      ↓
    Action
      ↓
    Answer
