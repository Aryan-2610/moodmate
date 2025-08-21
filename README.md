🌟 MoodMate – Daily Mood Tracker with Sidebar

MoodMate is a minimal web app that analyzes your daily mood from text input, plays a corresponding Spotify playlist, displays a quote, and keeps track of your mood history in a sidebar.


🔹 Features

Mood Detection: Uses a BERT-based sentiment analysis model to classify moods as Happy, Sad, or Neutral.
Spotify Integration: Automatically plays a playlist based on the detected mood.
Quotes: Shows a short quote corresponding to the mood.
Mood History Sidebar: Displays the last 10 mood entries with timestamp and original text.
Minimal UI: Textarea input with a “That’s it” button.


🔹 Sample Inputs

1️⃣ Sad Example:
"I got bullied at school today. Some classmates were laughing at me in the hallway. I tried to ignore it, but it really hurt my feelings. During lunch, I stayed by myself. On the way home, I kept thinking about what happened. It made me feel lonely and upset for the rest of the day."
2️⃣ Happy Example:
"I got a job offer today. I have been waiting for this opportunity for weeks. I spent the morning checking my email constantly. When I saw the message, I smiled and told my family. I spent the afternoon planning how to start this new chapter. Everything feels exciting and new."
3️⃣ Neutral Example:
"I went to the park this afternoon. The weather was nice, and a few people were walking their dogs. I sat on a bench and watched the birds for a while. Later, I walked around the playground. Nothing unusual happened, but it was calm and quiet. I headed home in the evening."


🔹 Installation
1. Clone the repository:
git clone <your-repo-url>
cd MoodMate

2. Create a Python virtual environment (recommended):

python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt
