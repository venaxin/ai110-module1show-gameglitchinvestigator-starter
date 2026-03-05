# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1. The Hints are reversed SOLVED
  2. If i am chnaging the difficulty midgame then the attempts are not resetting SOLVED
  3. Number of attempts are one less than what it should be SOLVED
  4. The new game button isnt working as its supposed to, i had to refresh it 
  5. Submit guess button is glitchy, had to click twice to submit a guess but it still counted two attempts for one input as you can see from the history
  6. Incorrect guess was also being shown as correct, example if i used float 100.1 and the target was 100, it gave me a correct on this which is wrong
  7. It is storing history or displaying history incorrectly not immediately
  8. The range isnt changing according to the difficulty
  9. The last hint from the previous game was still showing when starting a new game SOLVED
  10. On every second guess the hints were wrong because the secret was being compared as a string not a number SOLVED
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
I used Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
