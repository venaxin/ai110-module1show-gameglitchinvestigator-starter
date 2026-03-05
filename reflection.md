# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  1. SOLVED The Hints are reversed 
  2. SOLVED If i am chnaging the difficulty midgame then the attempts are not resetting 
  3. SOLVED Number of attempts are one less than what it should be 
  4. SOLVED The new game button isnt working as its supposed to, i had to refresh it, status not reset 
  5. SOLVED Submit guess button is glitchy, had to click twice to submit a guess but it still counted two attempts for one input as you can see from the history, hint not displayed correctly 
  6. SOLVED Incorrect guess was also being shown as correct, example if i used float 100.1 and the target was 100, it gave me a correct on this which is wrong
  7. SOLVED It is storing history or displaying history incorrectly not immediately history not reset on new game
  8. SOLVED The range isnt changing according to the difficulty 
  9. SOLVED The last hint from the previous game was still showing when starting a new game 
  10. SOLVED On every second guess the hints were wrong because the secret was being compared as a string not a number 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
I used Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The number of attempts bug was explained in a correct way 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
when i had manually solved a bug and told it to move that function to logic_utils file it moved the previous unfixed version. but I just realised while typing this, my manual updates didnt get saved on the AI's branch.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested it based on how it failed previously
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
Manual testing was just me trying out different edge cases and then I made Claude code design some test on 
- Did AI help you design or understand any tests? How?
yeah it helped me find bugs within the test itself and helped me design a wide variety of test i could only come up with 10 but it have 37 tests form the obvious to more niche ones which was nice covering a wide area

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
so basically every interaction caused a rerun so the secret number was changing everytime
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? 
so whenever a user clicks a button, types in a text box, any interaction will trigger a full rerun where streamlit reruns the entire python script from top to bottom
- What change did you make that finally gave the game a stable secret number?
I added certain conditions which had to be true in order for the secret to change, like pressing new game, changing difficulty, and another one where by default it only runs on first load
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Having a running doc ready to look back at and keep things in track, and i liked that the code claude used a separate branch and performed the chnages there and i had to make a pr and verify everything and then merge it which is very safe
- What is one thing you would do differently next time you work with AI on a coding task?
I realised i can do it in a faster way if i prompt AI better
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It is drastically better, like having a juiced up coworker guru whos teaming up with me to solve problems
