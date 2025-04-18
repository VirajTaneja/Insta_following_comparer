# Insta_following_comparer
A simple Python script to compare your Instagram followers and following lists. It tells you:
-Who you follow but don’t follow you back
-Who follows you but you don’t follow back

How to Get Your Instagram Data
1. Open Instagram on your phone or computer.
2. Go to your Profile.
3. Tap the ☰ (menu) > Your Activity (or Settings) > Download Your Information.
4. Choose what data you want (you can select all or just “Connections”).
5. Choose the destination (e.g., device or email) and request the download.
6. Once it's ready, download the .zip file from the link sent to you.
7. Extract the zip file — inside, you’ll find HTML files including:
    8.   followers_1.html
    9.   following.html
10. Place those files in the same folder as the Python script.

How to Run the Script
1. Install Python dependencies
  run pip install beautifulsoup4 lxml
2. Run the Script
   python compare.py
