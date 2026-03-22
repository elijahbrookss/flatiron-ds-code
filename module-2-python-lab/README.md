# Adventure Game

Text-based adventure game demonstrating user input, conditional logic, and input validation in Python.

## Run

```bash
python adventure_game.py
```

## Structure

```
├── adventure_game.py
└── docs/
    └── flow.md   ← pseudocode and flowchart
```

---

### Discussion Post
For the program structure, I chose to store the available locations in a list (LOCATIONS) and the story text in a dictionary (TEXTS) keyed by those location names. This approach keeps the game logic simple while also making it easy to extend later. If I wanted to add another location, I would only need to add the new location name to the list and provide the corresponding story lines in the dictionary. The rest of the program would continue to work without major changes. I liked this structure because it separates the game’s data from the control flow.

For the story text itself, I tried to write the descriptions in a style inspired by N.K. Jemisin, who is one of my favorite authors. Her writing tends to be immersive and reflective, so I thought it would be a fun way to add a little personality to a simple text-based assignment while still keeping the program logic straightforward.

One challenge I ran into was deciding how to handle input validation. One approach would have been to catch any exception and simply print an “invalid input” message before re-displaying the menu. However, I decided to use explicit validation with conditional checks instead. This approach felt more consistent with the concepts covered in the module and made the control flow clearer.

While working on the program, I also tried to keep a balance between keeping the solution simple and structuring it in a way that could scale later if the game were expanded. The goal wasn’t to over-engineer the solution, but rather to organize the data and logic in a way that would make adding more locations or story paths straightforward.