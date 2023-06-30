import os
import sys
import inquirer
import dotenv
dotenv.load_dotenv()

from gpt_handler import *
from spotify_handler import *
from inquiries import *





token = os.environ.get("api-token")

def main():
    main_promt = [
        inquirer.List('choices',
                      message="Choose Mode",
                      choices=['Simple (Bands)', 'Advanced (Mood, adjectives...)'],
                      ),
    ]

    _ = inquirer.prompt(main_promt)

    if _['choices'] == 'Simple (Bands)':
        promt_bands()

    if _['choices'] == 'Advanced (Mood, adjectives...)':
        print("advanced")


if __name__ == '__main__':
    main()

