# HQ-Bot
An easy way to cheat the popular trivia game using Google Cloud Vision OCR



# How to run:
1. Get credentials (API Key for Cloud Vision OCR, service account key json file)
2. Create an automator script like so:

\tITEM 1: Run shell script
cd /PATH/TO/DIRECTORY
rm bots.png

\tITEM 2: Take screenshot
- Interactive
- Choose selection
- Save to /PATH/TO/DIRECTORY/bots.png

\tITEM 3: Run shell script\n
cd /PATH/TO/DIRECTORY\n
export GOOGLE_APPLICATION_CREDENTIALS=[Path to service account key.json]\n
/path/to/python/interpreter runner.py

\tITEM 4: View results

3. Run script, hit OK on prompt for screenshot. SS everything below phone carrier info and above 'view comments'
4. Profit
