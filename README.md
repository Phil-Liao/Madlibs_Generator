# Mad Libs Generator

A fun, interactive Mad Libs game implemented in Python. This command-line application reads a story template, prompts the user for different types of words (nouns, verbs, adjectives, etc.), and then generates a completed, often hilarious, story.

## How to Play

1.  **Prerequisites:** Make sure you have Python 3 installed on your system.
2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Madlibs_Generator.git
    cd Madlibs_Generator
    ```
3.  **Run the game:**
    ```bash
    python main.py
    ```
4.  **Follow the prompts:** The game will ask you to enter various words. Once you've provided all the words, the completed story will be displayed.

## Customizing the Story

You can easily create your own Mad Libs stories!

1.  Open the `story.txt` file.
2.  Write your story, using placeholders in the format `___(PART_OF_SPEECH)___` for the words you want the user to provide. For example: `___(NOUN)___`, `___(VERB)___`, `___(ADJECTIVE)___`.
3.  Save the file, and the game will use your new story.

## Example

Here's an example of what a story template in `story.txt` might look like:

```
It was a ___(ADJECTIVE)___ day, and ___(NAME)___ decided to go to the ___(PLACE)___.
```

The game would then prompt the user:

```
Enter an adjective:
Enter a name:
Enter a place:
```

And generate a story like:

> It was a sunny day, and Alice decided to go to the park.

## Contributing

Contributions are welcome! If you have ideas for new features, find a bug, or want to improve the code, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.